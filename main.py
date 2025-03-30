import random

EMPTY_FIELD = ' '
ROW_NUMBER = 3
COLUMN_NUMBER = 3
CROSS = 'x'
CIRCLE = 'o'
board = [[EMPTY_FIELD for _ in range(COLUMN_NUMBER)] for _ in range(ROW_NUMBER)]


def print_board():
    for i in board:
        print(f"|{i[0]}| |{i[1]}| |{i[2]}|")


def choose_start_player():
    current_player = random.choice([CIRCLE, CROSS])
    print(f"Player {current_player} can start the game")
    return current_player


def choose_field():
    row = int(input("Please indicate the number of row (from 1 to 3): " ))
    column = int(input("Please indicate the number of column (from 1 to 3): " ))
    while board[row - 1][column - 1] != EMPTY_FIELD:
        print('Sorry, this field is occupied, please choose different field')
        row = int(input("Please indicate the number of row (from 1 to 3): "))
        column = int(input("Please indicate the number of column (from 1 to 3): "))
    return row, column


def insert_mark(current_player, row, column):
    board[row - 1][column - 1] = CROSS if current_player == CROSS else CIRCLE


def check_if_win():
    who_won = 0
    if board[0][0] == board[1][0] == board[2][0] != EMPTY_FIELD:
        who_won = board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] != EMPTY_FIELD:
        who_won = board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] != EMPTY_FIELD:
        who_won = board[0][2]

    elif board[0][0] == board[0][1] == board[0][2] != EMPTY_FIELD:
        who_won = board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] != EMPTY_FIELD:
        who_won = board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] != EMPTY_FIELD:
        who_won = board[2][0]

    elif board[0][0] == board[1][1] == board[2][2] != EMPTY_FIELD:
        who_won = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY_FIELD:
        who_won = board[0][2]
    return who_won


def change_player(current_player):
    return CIRCLE if current_player == CROSS else CROSS


def run_game():
    print("Welcome in the game tic_tac_toe!")
    print("Below you see our board: ")
    print_board()
    current_player = choose_start_player()
    while check_if_win() == 0:
        row, column = choose_field()
        insert_mark(current_player, row, column)
        print_board()
        current_player = change_player(current_player)
    print(f'Congratulations for player {check_if_win()}!')


run_game()
