import abc
import pygame

class DrawableObject():
    color = (0, 0, 0)

    @abc.abstractmethod
    def draw(self, surface: pygame.Surface):
        pass

    def set_color(self, color: tuple[int, int, int]):
        self.color = color