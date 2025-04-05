import random

EMPTY_FIELD = ' '
ROW_NUMBER = 3
COLUMN_NUMBER = 3
CROSS = 'x'
CIRCLE = 'o'
board = [[EMPTY_FIELD for _ in range(COLUMN_NUMBER)] for _ in range(ROW_NUMBER)]


def print_board() -> None:
    for i in board:
        print(f"|{i[0]}| |{i[1]}| |{i[2]}|")


def choose_start_player() -> str:
    current_player = random.choice([CIRCLE, CROSS])
    print(f"Player {current_player} can start the game")
    return current_player


def get_validated_input() -> tuple:
    row, column = None, None
    while True:
        numbers = input("Please indicate number of row and column with no spaces (from 1 to 3), example: 3 1:  ").split()
        if len(numbers) != 2:
            print("Please enter two numbers separated by space")
            continue
        try:
            row = int(numbers[0])
            column = int(numbers[1])
        except ValueError:
            print("Values must be numbers")
            continue
        if not (1 <= row <= 3 and 1 <= column <= 3):
            print("This number is out of range. Please give correct number")
            continue
        if board[row - 1][column - 1] != EMPTY_FIELD:
            print('Sorry, this field is occupied, please choose different field')
            continue
        break
    return row, column


def insert_mark(current_player, row, column) -> None:
    board[row - 1][column - 1] = CROSS if current_player == CROSS else CIRCLE


def check_if_win()-> str | None:
    for i in range(COLUMN_NUMBER):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY_FIELD:
            return board[0][i]
    for i in range(ROW_NUMBER):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY_FIELD:
            return board[i][0]
    for i in range(3):
        if board[0][0] == board[1][1] == board[2][2] != EMPTY_FIELD:
            return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0] != EMPTY_FIELD:
            return board[0][2]
    return None


def change_player(current_player):
    return CIRCLE if current_player == CROSS else CROSS


def run_game():
    print("Welcome in the game tic_tac_toe!")
    print("Below you see our board: ")
    print_board()
    current_player = choose_start_player()
    while check_if_win() is None:
        row, column = get_validated_input()
        insert_mark(current_player, row, column)
        print_board()
        current_player = change_player(current_player)
    print(f'Congratulations for player {check_if_win()}!')


run_game()
