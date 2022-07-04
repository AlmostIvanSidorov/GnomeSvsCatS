def count_substring(string, sub_string):
    count = 0
    s = string
    for count_loop in range(len(string)-len(sub_string)+1):
        if s.startswith(sub_string):
            count += 1
        s = s[1:]
    return print(count)


def main():
    """Some users shell"""
    count_substring(input("Please enter string: "), input("Please enter substring: "))


if __name__ == '__main__':
    main()
