from Simple_Card_War_Game import *


class MixinPlayer(Player):

    def skill(self):
        if self.name == "Ivan":
            print("No Luck just Skill!")
        else:
            print("Only Luck helps you!")


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        pass


def main():
    player = MixinPlayer(input("Enter your name player:"))
    print(player.name)
    player.skill()
    deck = Deck()
    print(deck)


if __name__ == "__main__":
    main()
