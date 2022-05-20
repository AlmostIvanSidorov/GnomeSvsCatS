"""
Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.
"""
from math import pi


def calculate_pi_func(n):
    """Return PI number to the n-th decimal place
    :param n: number of decimal to return
    :type n: int
    :return: PI with n decimal places
    :rtype: str
    """
    return f"{pi:.{n}f}"


def main():
    """
    Console function only for if __name__ == '__main__': section. No return or input
    """
    print("Welcome to Pi Calculator. In the shell below Enter the Number of digits upto which the value"
          "PI should be calculated. 'quit' command can be used for exit")

    while True:
        N = input("Input your number or 'quit' command:")

        if N == 'quit':
            break
        if not N.isdigit():
            print("You didn't enter a number. Try again")
        else:
            if int(N) > 50:
                print("Number must be lower than 51")
            elif int(N) < 2:
                print("Your number must be higher than 1")
            else:
                print(calculate_pi_func(int(N)))


if __name__ == '__main__':
    main()
