from pygame.locals import *
from rectangle import Rectangle
from  gameStarter import GameStarter
from snake import Snake

if __name__ == '__main__':
    gameWidth = 640
    gameHeight = 400

    game = GameStarter(gameWidth, gameHeight)

    wallColor = (155, 103, 60)
    wallThickness = 15

    topWall = Rectangle((0, 0), (gameWidth, wallThickness), wallColor)
    rightWall = Rectangle((gameWidth - wallThickness, 0), (wallThickness, gameHeight), wallColor)
    bottomWall = Rectangle((0, gameHeight - wallThickness), (gameWidth, wallThickness), wallColor)
    leftWall = Rectangle((0, 0), (wallThickness, gameHeight), wallColor)
    textures = [topWall, rightWall, bottomWall, leftWall]

    snakeColor = (255, 0, 0)
    snake = Snake((gameWidth / 2, gameHeight / 2), snakeColor)
    movableObjects = [snake]

    game.set_textures(textures)
    game.set_moveable_objects(movableObjects)
    game.start()
