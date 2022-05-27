"""
Calculate the total cost of tile it would take to cover a floor plan of width and height,
 using a cost entered by the user.
"""


def cost_calculator(list_of_floor_params):
    return list_of_floor_params[0]*list_of_floor_params[1]*list_of_floor_params[2]


def main():
    """Floor cost calculator"""
    print("Welcome to floor cost calculator!")
    while True:
        command_1 = input("Please enter 'quit' if you finished or 'continue' for price calculation:")
        if command_1 == 'quit':
            break
        elif command_1 == 'continue':
            list_of_floor_params = []
            for name in ["length", "width", "cost"]:
                while True:
                    command_2 = input(f"Please enter {name}:")
                    if not command_2.isdigit():
                        print("Please enter some digital value!")
                    else:
                        list_of_floor_params.append(float(command_2))
                        break
            print("Total price is " + str(cost_calculator(list_of_floor_params)) + "$")
        else:
            print("I don't understand you. Please use available commands.")


if __name__ == '__main__':
    main()
