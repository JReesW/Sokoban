from mothic import Game, flags


if __name__ == '__main__':
    game = Game(
        starting_scene="MainMenuScene",
        caption='SOKOBAN',
        display_flags=flags.RESIZABLE | flags.SCALED | flags.FULLSCREEN,
        surface_size=(960, 540),
        screen_size=(1440, 810)
    )

    game.start()
