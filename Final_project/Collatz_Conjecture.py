"""
Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
 If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
"""


def func(n):
    """
    Function for the following process:
    If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
    :return: number of steps
    """
    step = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
            step += 1

        elif n % 2 != 0:
            n = n * 3 + 1
            step += 1
    return step


def main():
    print("Welcome!")

    while True:
        user_number = input("Hello please enter you integer number or aa 'quit' command:")
        if user_number == 'quit':
            print('Have a good day!')
            break
        if not user_number.isdigit():
            print("Please enter an integer number")
        else:
            steps = func(int(user_number))
            print(f"Collatz Conjecture operation took {steps} steps")


if __name__ == "__main__":
    main()
