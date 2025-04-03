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
        print(self.cards[0]["card"], self.cards[1]["card"])
        playercards.append(self.cards[0])
        playercards.append(self.cards[1])
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


class Player:
    def __init__(self):
        self.playercards = []
    

class Dealer:
    def __init__(self):
        self.dealercards = []
