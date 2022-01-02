from drawableObject import DrawableObject
import pygame

class Rectangle(DrawableObject):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], color: tuple[int, int, int] = None) -> None:
        self.x, self.y = position 
        self.width, self.height = size

        if color != None:
            self.color = color

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))