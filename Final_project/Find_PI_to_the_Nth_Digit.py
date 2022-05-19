import math

# Tasks:
# Input Nth digits
# Calculate PI
# Output result


def calculate_pi_func(N):
    pi = 3
    number = 2
    pi_old = 0
    while pi - pi_old > 1/(pow(10, (N+4))):
        pi_old = pi
        pi = pi + 4/(number*(number+1)*(number+2))-4/((number+4)*(number+3)*(number+2))
        number = number + 4
    return pi


def shell():
    """
    Console function only for if __name__ == '__main__': section. No return or input
    """
    print("Welcome to Pi Calculator. In the shell below Enter the Number of digits upto which the value"
          "PI should be calculated. 'quit' command can be used for exit")

    while True:
        N = input("Input some number or 'quit' command:")

        if N == 'quit':
            break
        if not N.isdigit():
            print("You didn't enter a number. Try again")
        else:
            print(calculate_pi_func(int(N)))


if __name__ == '__main__':
    shell()
