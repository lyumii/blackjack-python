from models import Game

while True:
    game = Game()
    game.start()
    game.player_turn()

    replay = input("Would you like to play again? (y/n): ").strip().lower()
    if replay != "y":
        print("Thanks for playing! 🃏")
        break