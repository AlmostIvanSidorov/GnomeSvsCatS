from Simple_Card_War_Game import *


class MixinPlayer(Player):

    def skill(self):
        if self.name == "Ivan":
            print("No Luck just Skill!")
        else:
            print("Only Luck helps you!")


def main():
    player = MixinPlayer(input("Enter your name player:"))
    print(player.name)
    player.skill()


if __name__ == "__main__":
    main()
