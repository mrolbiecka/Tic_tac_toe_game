import random
BOARD = [['| |','| |','| |'],['| |','| |','| |'],['| |','| |','| |']]


def print_board():
    for i in BOARD:
        print(*i)


def choose_start_player():
    random_number = random.randint(1,2)
    if random_number == 1:
        print("Player x can start the game")
        return True
    else:
        print("Player o can start the game")


def choose_field():
    row = int(input("Please indicate the number of row (from 1 to 3): " ))
    column = int(input("Please indicate the number of column(from 1 to 3): " ))
    return row, column


def check_field_occupied(row, column):
    while BOARD[row][column] == '|x|' or BOARD[row][column] == '|o|':
        print('Sorry, this field is occupied, please choose different field')
        row = int(input("Please indicate the number of row (from 1 to 3) and column(from 1 to 3): "))
        column = int(input("Please indicate the number of row (from 1 to 3) and column (from 1 to 3): "))


def insert_circle_or_cross(x_turn, row, column):
    if x_turn:
        BOARD[row][column] = '|x|'
    else:
        BOARD[row][column] = '|o|'

def game():
    print("Welcome in the game tic_tac_toe!")
    print("Below you see our board: ")
    print_board()
    choose_start_player()
    row, column = choose_field()
    check_field_occupied(row, column)


    for x in range(9):
        pass

game()



