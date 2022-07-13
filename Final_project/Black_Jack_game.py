from Simple_Card_War_Game import Player
import random

"""
Black Jack game
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
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
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

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.all_cards:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()

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
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def main():
    #   Create deck
    play_game = True
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    deck.shuffle()

    while play_game:
        player_choice_1 = input("Do you want to play a game?:")
        if len(deck.all_cards) < 10:
            deck = Deck()
            deck.shuffle()
            print(len(deck.all_cards))
            print("Deck shuffled!!!")
        if player_choice_1 == "Yes":
            player_hand.cards, player_hand.value, player_hand.aces = [], 0, 0
            dealer_hand.cards, dealer_hand.value, dealer_hand.aces = [], 0, 0

            for i in range(0, 2):
                player_hand.add_card(deck.deal_one())
                dealer_hand.add_card(deck.deal_one())

            player_hand.adjust_for_ace()
            dealer_hand.adjust_for_ace()

            print("Your cards:")
            for card in player_hand.cards:
                print("Player:", card)
            print(f"You sum value:{player_hand.value}")
            for card in dealer_hand.cards[:len(dealer_hand.cards)-1]:
                print("Dealer:", card)
            if player_hand.value == 21:
                print("You Win")
                break
            player_choice_2 = "No"
            while player_choice_2 != "Yes":
                player_choice_2 = input("Check? ")
                if player_choice_2 == "Yes":
                    if player_hand.value > dealer_hand.value:
                        print("Dealer hand:", dealer_hand.value)
                        print("You Win")
                        break
                    else:
                        print("Dealer hand:", dealer_hand.value)
                        print("You Loose")
                        break

                elif player_choice_2 == "No":
                    if dealer_hand.value < 17:
                        dealer_hand.add_card(deck.deal_one())
                        dealer_hand.adjust_for_ace()
                        if dealer_hand.value > 21:
                            print("Dealer hand:", dealer_hand.value)
                            print("You Win")
                            break
                    player_hand.add_card(deck.deal_one())
                    player_hand.adjust_for_ace()
                    print("Your cards:")
                    for card in player_hand.cards:
                        print("Player:", card)
                    print(f"You sum value:{player_hand.value}")
                    if player_hand.value > 21:
                        print("You Loose")
                        break
                    elif player_hand.value == 21:
                        print("You Win")
                        break
                    for card in dealer_hand.cards[:len(dealer_hand.cards) - 1]:
                        print("Dealer:", card)

                else:
                    print("You drunk!")

        elif player_choice_1 == "No":
            play_game = False
        else:
            print("I don't understand you")


if __name__ == "__main__":
    main()
