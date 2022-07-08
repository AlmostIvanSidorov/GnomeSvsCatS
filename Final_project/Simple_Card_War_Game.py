import random
import pdb


"""
A simplified version of the game war. 
Two players will each start off with half the deck, then they each remove a card, compare which card has the highest value, and the player
 with the higher card wins both cards. In the event of a time
"""

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}


class Card:
    """return some card"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


def main():
    # Game Logic

    # New players
    player_one = Player("Ivan")
    player_two = Player("Ira")

    # Create and shuffle deck
    new_deck = Deck()
    new_deck.shuffle()
    for x in range(int(len(new_deck.all_cards) / 2)):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    # Game

    game_on = True
    round_number = 0

    while game_on:

        round_number += 1
        print(f"Round {round_number}")

        if len(player_one.all_cards) == 0:
            print(f"{player_one.name}! You LOSE!")
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print(f"{player_two.name}! You LOSE!")
            game_on = False
            break

        # Start a new round and reset current cards "on the table"
        player_one_cards_on_table = [player_one.remove_one()]
        player_two_cards_on_table = [player_two.remove_one()]

        at_war = True
        while at_war:
            if (
                player_one_cards_on_table[-1].value
                > player_two_cards_on_table[-1].value
            ):
                player_one.add_cards(player_two_cards_on_table)
                player_one.add_cards(player_one_cards_on_table)
                at_war = False

            elif (
                player_one_cards_on_table[-1].value
                < player_two_cards_on_table[-1].value
            ):
                player_two.add_cards(player_two_cards_on_table)
                player_two.add_cards(player_one_cards_on_table)
                at_war = False
            else:
                print("WAR!")
                if len(player_one.all_cards) < 5:
                    print(f"{player_one.name}! You LOSE!")
                    game_on = False
                    break

                elif len(player_two.all_cards) < 5:
                    print(f"{player_two.name}! You LOSE!")
                    game_on = False
                    break
                else:
                    for num in range(5):
                        player_one_cards_on_table.append(player_one.remove_one())
                        player_two_cards_on_table.append(player_two.remove_one())


if __name__ == "__main__":
    main()
