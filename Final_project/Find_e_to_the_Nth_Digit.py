"""
Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go.
"""
from math import e


def calculating_e(decimal_number):
    """
    Function to generate e up to that many decimal places were entered.
    :param decimal_number: number of decimal places
    :type: int
    :return: e up to that many decimal places were entered
    :rtype: str
    """
    return f"{e:.{decimal_number}f}"


def shell():
    print("Welcome to e calculator please enter how "
          "many many decimal places you want to see:")

    while True:
        decimal_number = input("Enter decimal places or 'quit' command:")

        if decimal_number == 'quit':
            break
        if not decimal_number.isdigit():
            print("Please enter an integer number or 'quit' command")

        else:
            if int(decimal_number) > 50:
                print("Sorry, your integer must be lower then 51")
            elif int(decimal_number) < 2:
                print("Sorry, your integer must be higher then 1")
            else:
                print(calculating_e(int(decimal_number)))


if __name__ == '__main__':
    shell()
