import random


game_board = """
{} | {} | {}
---------
{} | {} | {}
---------
{} | {} | {}
"""


def display_board(board):
    print(game_board.format(*board))


def ask_player_name():
    player1 = input("Player 1, what's your name? \n")
    player2 = input("Player 2, what's your name? \n")

    return player1, player2


# Function that selects randomly which is thr first player
def choose_first():
    return random.randint(1, 2)


# Function that saves the input player
def player_marker(player1):

    available_choices = ['X', 'O']

    # While the result is not X or O, it keeps asking for the correct input.
    while True:
        if (player1 := input(f'{first_player}, please select X or O: ')) not in available_choices:
            print(f'\nSorry {first_player}, but you did not select X or O. Please try again.')
        else:
            player2 = 'X' if player1 == 'O' else 'O'
            return player1, player2


# Function that receives the user choice 'X' or 'O' and position 1-9 and updates the board
def place_marker(board, marker, position):

    board[position-1] = marker

    display_board(board)

    return board


def player_position(board, name):

    position = 0

    while True:

        try:
            position = int(input(f'{name}, please choose a position (1-9): '))
        except ValueError:
            print(f'\nSorry {name}, but you did not select a position between 1 and 9. Please try again.')
            continue

        # Check if the input position is a digit between 1 and 9
        if not 1 <= position <= 9:
            print(f'\nSorry {name}, but you did not select a position between 1 and 9. Please try again.')
            continue

        # Check if the position is not available taken
        if board[position-1] != ' ':
            print(f'\nSorry {name}, but that position is already taken. Please try again.')
            continue
        else:
            break

    return position


# Function that checks if the player has won. Returns True if yes.
def win_check(board, marker):

    # Check diagonals
    if board[0] == marker and board[4] == marker and board[8] == marker:
        return True
    if board[2] == marker and board[4] == marker and board[6] == marker:
        return True

    # Check horizontal positions
    if board[0] == marker and board[1] == marker and board[2] == marker:
        return True
    if board[3] == marker and board[4] == marker and board[5] == marker:
        return True
    if board[6] == marker and board[7] == marker and board[8] == marker:
        return True

    # Check vertical positions
    if board[0] == marker and board[3] == marker and board[6] == marker:
        return True
    if board[1] == marker and board[4] == marker and board[7] == marker:
        return True
    if board[2] == marker and board[5] == marker and board[8] == marker:
        return True

    return False


# Function that checks if the board is full. Returns True if full, False otherwise.
def full_board_check(board):
    print(board)
    for position in board:
        # The board is not full. There is at least one position available.
        if position == ' ':
            return False

    # The board is full.
    return True


# Function that asks the player if they want to play again and returns True if they want
def replay():

    choice = ' '
    available_choices = ['Y', 'N']

    while True:
        choice = input('Would you like to play again? Please select Y or N: \n')

        if choice not in available_choices:
            print('Sorry, but you did not select Y or N. Please try again.')
        elif choice == 'Y':
            return True
        else:
            return False


# MAIN

print('Welcome to Tic Tac Toe Game!')

# Show the board index positions
positions_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
display_board(positions_board)

# Begin the game with an empty board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

playing = True
game_on = True

while playing:

    # Randomly selecting which player is playing first
    p1_name, p2_name = ask_player_name()
    if choose_first() == 1:
        first_player = p1_name
        second_player = p2_name
        print(f"\n{p1_name} is playing first.")
    else:
        first_player = p2_name
        second_player = p1_name
        print(f"\n{p2_name} is playing first.")

    # The first player chooses the marker X or O
    first_marker, second_marker = player_marker(first_player)

    while game_on:
        # FIRST PLAYER'S TURN
        # First Player chooses the position to place the marker
        first_position = player_position(board, first_player)
        # The board is updated
        board = place_marker(board, first_marker, first_position)
        # Check if the first player has won the game
        if win_check(board, first_marker):
            print(f'Congratulations, {first_player}! You won!\n')
            if replay():
                board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                break
            else:
                playing = False
                break

        # Check if all the positions are completed
        if full_board_check(board):
            print('GAME OVER')
            if replay():
                board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                break
            else:
                playing = False
                break

        # SECOND PLAYER'S TURN
        second_position = player_position(board, second_player)
        board = place_marker(board, second_marker, second_position)
        if win_check(board, second_marker):
            print(f'Congratulations, {second_player}! You won!\n')
            if replay():
                board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                break
            else:
                playing = False
                break

        # Check if all the positions are completed
        if full_board_check(board):
            print('GAME OVER')
            if replay():
                board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                break
            else:
                playing = False
                break

# if __name__ == '__main__':
#    main()
