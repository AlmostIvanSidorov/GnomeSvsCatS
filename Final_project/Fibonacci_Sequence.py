"""
Enter a number and have the program
generate the Fibonacci sequence to that number or to the Nth number.
"""


def fibanacci_sequence_gen(N):
    """Generate the Fibonacci sequence to the Nth number.
    :param N: how many numbers you want to see
    :type: int
    :return: list of numbers
    :type: List
    """
    fibanacci_sequence = [0,1]

    if N == 1:
        fibanacci_sequence = [0]
    elif N == 2:
        fibanacci_sequence = [0, 1]
    else:
        for N in range(2,N):
            fibanacci_sequence.append((fibanacci_sequence[-1]+fibanacci_sequence[-2]))

    return fibanacci_sequence


def main():
    """Fibonacci sequence calculator
    """
    print("Welcome to Fibonacci sequence calculator!")
    while True:
        N = input("Enter how many numbers you want to see or 'quit' command:")

        if N == 'quit':
            break

        if not N.isdigit() or int(N) == 0:
            print("Please enter positive integer number")

        else:
            print(fibanacci_sequence_gen(int(N)))


if __name__ == '__main__':
    main()
