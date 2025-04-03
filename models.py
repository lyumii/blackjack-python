import random

class Deck:
    def __init__(self):
        suites = ['♠', '♥', '♦', '♣']
        card_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
        self.cards = []
        

        for suite in suites:
            for value, points in card_values.items():
                new_card = f"{value} {suite}"
                self.cards.append({"card": new_card, "value": points})
        random.shuffle(self.cards)
    
    def deal_to_player(self, playercards):
        print(f"{"-" * 50}\n"
              "PLAYER DRAWS:\n"
              f"{"-" * 50}\n")
        drawn_cards = [self.cards[0], self.cards[1]]
        for card in drawn_cards:
            print(card["card"])
            if card["card"].startswith("A"):
                ace_choice = input(f"You drew an Ace ({card['card']})! Would you like it to count as:\n"
                                "1. 1\n"
                                "2. 11\n"
                                "Choice: ")
                if ace_choice.strip() == "1":
                    card["value"] = 1
                else:
                    card["value"] = 11

            playercards.append(card)

        total = 0
        for card in playercards:
            total += int(card["value"])

        print(total)

        self.cards = self.cards[2:]
        

    def deal_to_dealer(self, dealercards, reveal=False):
        print(f"{"-" * 50}\n"
              "DEALER DRAWS:\n" 
              f"{"-" * 50}")
        print(self.cards[0]["card"])
        if reveal:
            print(self.cards[1]["card"])
        print(f"{"-" * 50}")
        dealercards.append(self.cards[0])
        dealercards.append(self.cards[1])
        self.cards = self.cards[2:]
    
class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.available_cards = self.deck.cards

    def start(self):
        print(f"{"=" * 50}\n"
              f"{"NEW GAME OF BLACKJACK":^40}\n"
              f"{"=" * 50}\n")
        self.deck.deal_to_player(self.player.playercards)
        self.deck.deal_to_dealer(self.dealer.dealercards)
    
    def player_turn(self):
        player_choice = input("Would you like to draw or stand?\n"
                              "1. Draw\n"
                              "2. Stand\n"
                              "Choice: ")
        if player_choice.lower().strip() in ["1", "draw"]:
            self.deck.deal_to_player(self.player.playercards)
            total = 0
            for card in self.player.playercards:
                total += int(card["value"])
            print(self.player.playercards)
            if total == 21:
                print(f"{"*" * 40}\n"
                      "BLACKJACK! CONGRATULATIONS!! YOU WON!!! 🥳🥳\n"
                      f"{"*" * 40}")
            elif total > 21:
                print(f"{"*" * 40}\n"
                      "BUST! YOU LOSE! 😭😵\n"
                      f"{"*" * 40}")
            else:
                self.player_turn()
        if player_choice.lower().strip() in ["2", "stand"]:
            self.dealer_turn(total)

    def dealer_turn(self, player_total):
        self.deck.deal_to_dealer(reveal=True)
        dealer_total = 0
        for card in self.dealer.dealercards:
            dealer_total += int(card["value"])
        print(self.deck.dealercards)
        if dealer_total == 21:
            print(f"{"*" * 40}\n"
                      "DEALER GOT BLACKJACK ! YOU LOSE! 😭😵\n"
                      f"{"*" * 40}")
        elif dealer_total > 21:
            print(f"{"*" * 40}\n"
                      "DEALER GOT BUSTED! CONGRATULATIONS!! YOU WON!!! 🥳🥳\n"
                      f"{"*" * 40}")
        elif dealer_total < 17:
            self.dealer_turn(player_total)
        else: 
            if dealer_total > player_total:
                print(f"{"*" * 40}\n"
                      "YOU LOSE! 😭😵\n"
                      f"{"*" * 40}")
            else: 
                print(f"{"*" * 40}\n"
                      "BLACKJACK! CONGRATULATIONS!! YOU WON!!! 🥳🥳\n"
                      f"{"*" * 40}")
        

class Player:
    def __init__(self):
        self.playercards = []
    

class Dealer:
    def __init__(self):
        self.dealercards = []
