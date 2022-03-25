"""
Name: Cade Atkins
tictactoe.py
"""

def count():
    result = 9
    for num in range(result):
        result = result -1
    return result

def check(board):
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for num in board:
        if [board[0+num] , board[1+num] , board[2+num]] in soln:
            return True
        else:
            return False


def moves():
    position = input("What position would you like to be in(1-9): ")
    character = input("x's or o's: ")
    return position and character


def build_board():
    board = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    ]
    return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    for pos in board:
        if position == pos:
            return True
        else:
            return False


def fill_spot(board, position, character):
    for pos in board:
        if position != pos:
            board.replace(pos, character)
        else:
            pass


def winning_game(board):
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for win in board:
        if win in soln:
            return True
        else:
            return False


def game_over(board):
    if winning_game(board):
        return True
    elif not winning_game(board):
        for check in board:
            if check != int():
                return False
            else:
                pass
    elif count() == 0:
        return True
    else:
        return False


def get_winner(board):
    odds = [1, 3, 5, 7, 9]
    if game_over(board):
        if check(board):
            if count() in odds:
                return print("Game winner is X's")
            elif count() not in odds:
                return print("Game winner is O's")
    else:
        return print("Game is tied")



def play(board):
    key = board
    while count() > 0:
        continue
    if count() == 0:
        return get_winner(board)


def main():
    counts = count()
    board = build_board()
    char = ['x','o']
    for num in counts:
        print_board(board)
        for i in range(2):
            position = input("Where would you like to move(1-9): ")
            character = char[i - 1]
            if is_legal(board, position):
                fill_spot(board, position, character)
            else:
                position = input("Choose an available position instead: ")
                if is_legal(board, position):
                    fill_spot(board, position, character)
                else:
                    pass
            if is_legal(board, position):
                try:
                    if winning_game(board):
                        get_winner(board)
                    else:
                        pass
                except None:
                    continue
    return


if __name__ == '__main__':
    main()
