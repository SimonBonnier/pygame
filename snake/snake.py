import pygame
from drawableObject import DrawableObject
from direction import Direction

class Snake(DrawableObject):
    def __init__(self, startPosition: tuple[int, int], color: tuple[int, int, int] = None) -> None:
        self.x, self.y = startPosition
        self.width = 15
        self.size = 1
        self.speed = 1
        self.direction = Direction.UP

        if color != None:
            self.color = color

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.width))

    def update(self):
        if self.direction == Direction.UP:
            self.y = self.y - self.speed
        elif self.direction == Direction.Right:
            self.x = self.x + self.speed
        elif self.direction == Direction.Down:
            self.y = self.y + self.speed
        else:
            self.x = self.x - self.speed

    def move(self, scanCode):
        if scanCode == 82:
            self.direction = Direction.UP
        elif scanCode == 79:
            self.direction = Direction.Right
        elif scanCode == 81:
            self.direction = Direction.Down
        else:
            self.direction = Direction.Left
