"""
Have the program find prime numbers until the user chooses to stop asking for the next one.
"""


def prime_factor_generator(n):
    """
     Prime Factorizer function
    :param n: insert number for prime factorization
    :return: list of prime numbers of which insert number consist
    :rtype:List
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors.append(i)
            break
    if n > 1:
        factors.append(n)
    return factors


def main():
    """
    Prime number generator.
    """
    print("Welcome to prime number generator!")
    current_number = 2
    while True:
        input_value = input("Would You like to see next prime number?(Y/N):")
        if input_value == 'N':
            break
        elif input_value == 'Y':
            print(prime_factor_generator(current_number)[0])
            current_number += 1
            while len(prime_factor_generator(current_number)) != 1:
                current_number += 1
        else:
            print("Sorry I dont't understand you, please enter Y or N")


if __name__ == '__main__':
    main()
