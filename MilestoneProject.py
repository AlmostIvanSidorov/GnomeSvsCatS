def display_board(board):
    board = board
    print(board[7], '|', board[8], '|', board[9])
    print('--', '---', '--')
    print(board[4], '|', board[5], '|', board[6])
    print('--', '---', '--')
    print(board[1], '|', board[2], '|', board[3])


def user_choice():
    choice = 'WRONG'
    acceptable_range = range(1, 10)

    while choice.isdigit() == False or int(choice) not in acceptable_range:

        choice = input("Please enter a number (1-9): ")

        if choice.isdigit() == False:
            print("Sorry that is not digit!")

        elif int(choice) not in acceptable_range:
            print("Choice is not in range")


def player_choice():
    player1 = "WRONG"
    while player1 != 'X' and player1 != 'O':
        player1 = input("Chose your side X or O: ")

        if player1 != 'X' and player1 != 'O':
            print("You can choose only X or Y")
        elif player1 == "X":
            print("Player1 plays as X ")
            player1_marker = "X"
            player2_marker = "O"
        elif player1 == "O":
            print("Player1 plays as O ")
            player1_marker = "O"
            player2_marker = "X"




def clear_display():
    print("\n"*100)



print('Welcome to Tic Tac Toe!')

# while True:
# Set the game up here
player_choice()

# pass

# while game_on:
# Player 1 Turn


# Player2's turn.

# pass

# if not replay():
# break

