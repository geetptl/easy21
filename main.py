from easy21 import e21

if __name__ == '__main__':
    game = e21.Game()
    print(game)
    for i in range(2):
        print(game.state)
        game.step(action=e21.Action.HIT)
        if game.state.is_game_over:
            print(game)
            exit(1)

    game.step(action=e21.Action.STICK)

    for i in range(4):
        print(game.state)
        game.step(action=e21.Action.HIT)
        if game.state.is_game_over:
            print(game)
            exit(1)

    game.step(action=e21.Action.STICK)
    print(game)

    print("exiting...")
