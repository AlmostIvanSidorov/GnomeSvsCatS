"""
Implement two types of sorting algorithms: Merge sort and bubble sort
"""


def buble_sort(user_list, i=0):
    """Func for bubble sort"""
    if len(user_list) == 1 or len(user_list) == 2:
        return user_list
    else:
        return sorted(user_list)


def merge_sort(user_list):
    """Func for merge sort"""
    if len(user_list) == 1 or len(user_list) == 2:
        return user_list
    else:
        return sorted(user_list)


def main():
    """
    Some shell to choose kind of sort and input list to sort
    :return:
    """
    print("Welcome to sorting list program")
    while True:
        print("If you want to sort some list print 'sort' else print 'quit'")
        user_command_1 = input("Please enter command: ")
        if user_command_1 == 'quit':
            print("Bye! Have a good day!")
            break
        elif user_command_1 == 'sort':
            user_list = []
            while True:
                user_command_2 = input("Please select type of sorting bubble(1) or merge(2): ")
                if user_command_2 == "1":
                    while True:
                        user_number = input("Please input a number for your list or 'end' command for list end: ")
                        if user_number == 'end':
                            print(buble_sort(user_list))
                            break
                        if not user_number.isdigit():
                            print("Please enter integer number")
                        else:
                            user_list.append(int(user_number))
                    break
                elif user_command_2 == "2":
                    while True:
                        user_number = input("Please input a number for your list or 'end' command for list end: ")
                        if user_number == 'end':
                            print(merge_sort(user_list))
                            break
                        if not user_number.isdigit():
                            print("Please enter integer number")
                        else:
                            user_list.append(user_number)
                    break
                else:
                    print("Please choose 1 or 2")

        else:
            print("I don't understand you:(")


if __name__ == "__main__":
    main()

