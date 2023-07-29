from easy21 import e21

if __name__ == '__main__':
    print("Starting game...")
    game_instance = e21.Game()
    while game_instance.is_players_turn:
        print("Current state >", game_instance.state)
        action = input("Enter action > ")
        if action.lower() == "hit":
            action_ = e21.Action.HIT
        elif action.lower() == "stick":
            action_ = e21.Action.STICK
        else:
            raise ValueError("Invalid input")
        game_instance.step(action_)

    if not game_instance.is_game_over:
        game_instance.step(action=None)

    print(game_instance)
