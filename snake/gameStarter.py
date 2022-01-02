import pygame
from pygame.constants import KEYDOWN

from snake import Snake
clock = pygame.time.Clock()

class GameStarter:

    def __init__(self, width: int, height: int) -> None:
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = width, height

    def initialize(self): 
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self._display_surf.fill((255, 255, 255))
        self._running = True

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            for obj in self._movable_objects:
                if type(obj) is Snake:
                    obj.move(event.scancode)

        if event.type == pygame.QUIT:
            self._running = False

    def set_textures(self, textures): 
        self._textures = textures

    def set_moveable_objects(self, movableObjects):
        self._movable_objects = movableObjects

    def loop(self):
        for obj in self._movable_objects:
            obj.update()

    def render(self):
        self.clear()

        for tex in self._textures:
            tex.draw(self._display_surf)

        for movableObject in self._movable_objects:
            movableObject.draw(self._display_surf)

        pygame.display.flip()

    def clear(self):
        self._display_surf.fill((255, 255, 255))

    def stop(self): 
        pygame.quit()

    def start(self):
        if self.initialize() == False:
            self._running = False

        while (self._running):
            clock.tick(60)
            for event in pygame.event.get():
                self.handle_input(event)
            self.loop()
            self.render()
        self.stop()