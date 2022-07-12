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

    deck.shuffle()

    while play_game:
        player_choice_1 = input("Do you want to play a game?:")
        if len(deck.all_cards) < 10:
            deck = Deck()
            deck.shuffle()
            print(len(deck.all_cards))
            print("Deck shuffled!!!")
        if player_choice_1 == "Yes":
            player_hand.cards = []
            player_hand.value = 0
            player_hand.aces = 0

            player_hand.add_card(deck.deal_one())
            player_hand.add_card(deck.deal_one())
            player_hand.adjust_for_ace()

            print("Your cards:")
            for card in player_hand.cards:
                print(card)
            print(f"You sum value:{player_hand.value}")

            if player_hand.value == 21:
                print("You Win")
                break
            player_choice_2 = input("Do you need a card? ")
            while player_choice_2 != "Yes":
                if player_choice_2 == "No":
                    print("Chicken!")
                    break
                print("You drunk?")
                player_choice_2 = input("Do you need a card? ")

            while player_choice_2 == "Yes":
                player_hand.add_card(deck.deal_one())
                player_hand.adjust_for_ace()
                print("Your cards: ")
                for card in player_hand.cards:
                    print(card)
                print(f"You sum value:{player_hand.value}")
                if player_hand.value > 21:
                    print("You Loose")
                    break
                elif player_hand.value == 21:
                    print("You Win")
                    break
                player_choice_2 = input("Do you need a card? ")
                while player_choice_2 != "Yes":
                    if player_choice_2 == "No":
                        print("Chicken!")
                        break
                    print("You drunk?")
                    player_choice_2 = input("Do you need a card? ")

        elif player_choice_1 == "No":
            play_game = False
        else:
            print("I don't understand you")


if __name__ == "__main__":
    main()
