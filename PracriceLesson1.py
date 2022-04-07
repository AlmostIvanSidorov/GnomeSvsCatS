
def user_choice():

    choice = 'WRONG'
    acceptable_range = range(0, 10)

    while choice.isdigit() == False or int(choice) not in acceptable_range:

        choice = input("Please enter a number (1-9): ")

        if choice.isdigit() == False:
            print("Sorry that is not digit!")

        elif int(choice) not in acceptable_range:
            print("Choice is not in range")


    return int(choice)

result = user_choice()

print(result)