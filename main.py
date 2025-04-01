from mothic import Game, flags


if __name__ == '__main__':
    game = Game(
        starting_scene="MainMenuScene",
        caption='SOKOBAN',
        display_flags=flags.RESIZABLE
    )

    game.start()
