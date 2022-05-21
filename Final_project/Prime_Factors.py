"""
Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""


def prime_factors(n):
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
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def main():
    print("Welcome to Prime Factorizer program! :)")

    while True:
        insert_number = input("Pleas insert an integer number or 'quit' command:")
        if insert_number == 'quit':
            break
        elif not insert_number.isdigit():
            print("Please enter an integer number!")
        else:
            if int(insert_number) < 2:
                print("Sorry number value must be more than 2(")
            else:
                print(prime_factors(int(insert_number)))


if __name__ == "__main__":
    main()
