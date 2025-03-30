import random
BOARD = [['|o|','|o|','|o|'],['||','|x|','| |'],['||','| |','|x|']]


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
        return False


def choose_field():
    row = int(input("Please indicate the number of row (from 1 to 3): " ))
    column = int(input("Please indicate the number of column(from 1 to 3): " ))
    return row, column


def check_field_occupied(row, column):
    while BOARD[row - 1][column - 1] == '|x|' or BOARD[row - 1][column - 1] == '|o|':
        print('Sorry, this field is occupied, please choose different field')
        row = int(input("Please indicate the number of row (from 1 to 3) and column(from 1 to 3): "))
        column = int(input("Please indicate the number of row (from 1 to 3) and column (from 1 to 3): "))


def insert_circle_or_cross(x_turn, row, column):
    if x_turn:
        BOARD[row - 1][column - 1] = '|x|'
    else:
        BOARD[row - 1][column - 1] = '|o|'


def win_game():
    for i in range(len(BOARD)):
        for j in range(len(BOARD[i])):
            if BOARD[i][j] == '|o|':
                print('Circle wins the game!')
                win = 'circle'
                return win
            if BOARD[i][j] == '|x|':
                print('Cross wins the game!')
                win = 'cross'
                return win
            if BOARD[j][i] == '|x|':
                print('Cross wins the game!')
                win = 'cross'
                return win
            if BOARD[j][i] == '|o|':
                print('Circle wins the game!')
                win = 'circle'
                return win


    if BOARD[0][0] == '|o|' and BOARD[1][1] == '|o|' and BOARD[2][2] == '|o|':
        win = 'circle'
        print('Circle wins the game!')
    elif BOARD[0][0] == '|x|' and BOARD[1][1] == '|x|' and BOARD[2][2] == '|x|':
        win = 'cross'
        print('Cross wins the game!')
    else:
        win = 0
    return win


def game():
    print("Welcome in the game tic_tac_toe!")
    print("Below you see our board: ")
    print_board()
    x_turn = choose_start_player()
    while win_game() != 0:
        row, column = choose_field()
        check_field_occupied(row, column)
        insert_circle_or_cross(x_turn, row, column)
        print_board()
        x_turn = False


win_game()



