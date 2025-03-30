import random
BOARD = [['| |','| |','| |'],['| |','| |','| |'],['| |','| |','| |']]


def print_board():
    for i in BOARD:
        print(*i)


def choose_start_player():
    random_number = random.randint(1,2)
    if random_number == 1:
        print("Player x can start the game")
        current_player = 'x'
    else:
        print("Player o can start the game")
        current_player ='y'
    return current_player


def choose_field():
    row = int(input("Please indicate the number of row (from 1 to 3): " ))
    column = int(input("Please indicate the number of column (from 1 to 3): " ))
    return row, column


def check_field_occupied(row, column):
    while BOARD[row - 1][column - 1] == '|x|' or BOARD[row - 1][column - 1] == '|o|':
        print('Sorry, this field is occupied, please choose different field')
        row = int(input("Please indicate the number of row (from 1 to 3) and column(from 1 to 3): "))
        column = int(input("Please indicate the number of row (from 1 to 3) and column (from 1 to 3): "))


def insert_circle_or_cross(current_player, row, column):
    if current_player == 'x':
        BOARD[row - 1][column - 1] = '|x|'
    else:
        BOARD[row - 1][column - 1] = '|o|'



def win_game():
    who_won = 0
    if BOARD[0][0] == BOARD[1][0] == BOARD[2][0] != '| |':
        who_won = BOARD[0][0]
    elif BOARD[0][1] == BOARD[1][1] == BOARD[2][1] != '| |':
        who_won = BOARD[0][1]
    elif BOARD[0][2] == BOARD[1][2] == BOARD[2][2] != '| |':
        who_won = BOARD[0][2]

    elif BOARD[0][0] == BOARD[0][1] == BOARD[0][2] != '| |':
        who_won = BOARD[0][0]
    elif BOARD[1][0] == BOARD[1][1] == BOARD[1][2] != '| |':
        who_won = BOARD[1][0]
    elif BOARD[2][0] == BOARD[2][1] == BOARD[2][2] != '| |':
        who_won = BOARD[2][0]

    elif BOARD[0][0] == BOARD[1][1] == BOARD[2][2] != '| |':
        who_won = BOARD[0][0]
    elif BOARD[0][2] == BOARD[1][1] == BOARD[2][0] != '| |':
        who_won = BOARD[0][2]
    return who_won


def change_player(current_player):
    if current_player == 'x':
        current_player ='o'
    else:
        current_player = 'x'
    return current_player


def game():
    print("Welcome in the game tic_tac_toe!")
    print("Below you see our board: ")
    print_board()
    current_player = choose_start_player()
    while win_game() == 0:
        row, column = choose_field()
        check_field_occupied(row, column)
        insert_circle_or_cross(current_player, row, column)
        print_board()
        current_player = change_player(current_player)
    print(f'Congratulations for player {win_game()[1]}!')

game()


