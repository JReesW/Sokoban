from mothic import Game
from scenes import MainMenuScene


if __name__ == '__main__':
    game = Game(
        starting_scene=MainMenuScene,
        caption='SOKOBAN'
    )

    while True:
        game.frame()
