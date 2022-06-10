"""
The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).
"""


def sieve_of_eratosthenes(user_n):
    """Sieve of Eratosthenes algorithm func
    """
    list = []
    final_list = []
    list_buffer = []
    for i in range(2, user_n + 1):
        list.append(i)

    x = list.pop(0)

    while len(list) != 0:
        for i in range(len(list)):
            if list[i] % x == 0:
                list_buffer.append(list[i])
        final_list.append(x)
        for number in list_buffer:
            list.remove(number)
        x = list.pop(0)
        list_buffer = []

    final_list.append(x)

    return final_list


def main():
    print("Welcome to The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller"
          " primes (below 10 million or so).")
    while True:
        user_number = input("Please enter your number or 'quit' to end program:")
        if user_number == 'quit':
            break
        if not user_number.isdigit():
            print("Please enter integer number")
        else:
            print(sieve_of_eratosthenes(int(user_number)))


if __name__ == '__main__':
    main()
