import pygame as pg
import random

cell = 10
FrameX = 500
FrameY = 500
title = "Game"


class frame:
    white = (255, 255, 255)
    black = (0, 0, 0)

    def __init__(self, title, pixelX, pixelY):
        self.pixelX = pixelX
        self.pixelY = pixelY
        pg.init()
        pg.display.set_caption(title)
        self.caption = pg.display.set_mode((pixelX, pixelY))

    def update(self, position):
        self.caption.fill(self.black)
        for point in position:
            pg.draw.rect(self.caption, self.white, pg.Rect(point[0], point[1], cell, cell))
        pg.display.update()

    def quit(self):
        pg.quit()


class snake:

    def __init__(self, bodyLen):
        self.head = [FrameX / 2, FrameY / 2]
        self.bodyLen = bodyLen
        self.bodyPos = []
        for i in range(self.bodyLen):
            self.bodyPos.append([self.head[0] - i * cell, self.head[1]])

    def getBodyPos(self):
        return self.bodyPos

    def control(self, key, grow=False):
        if key == 0:  # up
            self.head[1] -= cell
        elif key == 1:  # right
            self.head[0] += cell
        elif key == 2:  # left
            self.head[0] -= cell
        elif key == 3:  # down
            self.head[1] += cell
        self.bodyPos.insert(0, list(self.head))
        if not grow:
            self.bodyPos.pop()
        return self.bodyPos

    def die(self):
        print("head" , self.head , "body", self.bodyPos)
        if self.head[0] >= 500 or self.head[1] >= 500 or self.head[0] <= 0 or self.head[1] <= 0:
            return True
        elif self.head in self.bodyPos[1:]:
            return True
        else:
            return False


class fruit:
    def __init__(self):
        self.position = []

    def generate(self):
        self.position = [[random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]]
        return self.position

    def getPos(self):
        return self.position


if __name__ == '__main__':
    frame = frame(title, FrameX, FrameY)
    snake = snake(5)
    fruit = fruit()
    key = 0
    initPos = snake.getBodyPos() + fruit.generate()
    frame.update(initPos)
    clock = pg.time.Clock()
    while 1:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    key = 0
                elif event.key == pg.K_RIGHT:
                    key = 1
                elif event.key == pg.K_LEFT:
                    key = 2
                elif event.key == pg.K_DOWN:
                    key = 3
                elif event.key == pg.K_ESCAPE:
                    frame.quit()
        clock.tick(5)
        fruitPos = fruit.getPos()
        snakePos = snake.getBodyPos()
        if fruitPos[0] in snakePos:
            fruit.generate()
            snake.control(key, True)
        else:
            snake.control(key)
        objPos = fruitPos + snakePos
        if snake.die():
            frame.quit()
        frame.update(objPos)
