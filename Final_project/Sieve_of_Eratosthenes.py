"""
The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).
"""


def sieve_of_eratosthenes(user_n):
    """Sieve of Eratosthenes algorithm func
    """
    list = []
    for i in range(2, user_n+1):
        list.append(i)
    return list


def main():
    print("Welcome to The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller"
          " primes (below 10 million or so).")
    while True:
        user_number = input("Please enter your number or 'quit' to end program:" )
        if user_number == 'quit':
            break
        if not user_number.isdigit():
            print("Please enter integer number")
        else:
            print(sieve_of_eratosthenes(int(user_number)))


if __name__ == '__main__':
    main()
