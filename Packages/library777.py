def sum_local(a, b):
    return a+b

def main():
    print(sum_local(1, 2))

    print(sum_local((3, 2), (2, 3)))

if __name__ == "__main__":
    main()
