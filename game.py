from board import Board
from bot import Bot


GameBoard = Board()


def get_valid_input(input_str, valid_options):
    """
    (str), (str) -> (str)
    This function gets data from user
    :param input_str: a msg that will be displayed to user when asking for data
    :param valid_options: all valid options of data
    :return: (str) - user's option
    """
    input_str += " ({}) ".format(", ".join(valid_options))
    resp = input(input_str)
    while resp.lower() not in valid_options:
        resp = input(input_str)
    return resp

def displayBoard(board):
    s = "\n"
    s += "                    0     1     2\n\n"
    for i in range(3):
        for j in range(3):
            if j == 1:
                s += "|  " + str(board._field[i][j]) + "  |"
            elif j == 0:
                s += "               " + str(i) + "    " + str(board._field[i][j]) + "  "
            else:
                s += "  " + str(board._field[i][j]) + " "
        if i < 2:
            s += "\n                  ------------------\n"
    print(s)

def userMakeMove(user_turn, board):
    valid_coords = ([0, 0], [0, 1], [0, 2], [1, 0],
                        [1, 1], [1, 2], [2, 0], [2, 1], [2, 2])
    print("It's your turn to make a move!")
    coord = input("Please type the coord below - first row, then col: ")
    coord =[int(i) for i in coord.split()]
    if coord in valid_coords:
        if board.put(user_turn, coord):
            pass
        else:
            print("Your move is not valid, please, try again.\n")
            userMakeMove(user_turn, board)
    else:
        print("Your move is not valid, please, try again.")
        userMakeMove(user_turn, board)



print("----------------Welcome to Tic-Tac-Toe Game!-------------------------")
print("In this game you will be playing with a bot")

print("X - make a move first")
user_turn = get_valid_input("Please, pick your turn: 'X' or 'O' and type your choice here: ", "xoXO").upper()

displayBoard(GameBoard)

turn_counter = 0

if user_turn == "X":
    bot = Bot("O")
    userMakeMove(user_turn, GameBoard)
    print("Last move: ", GameBoard._lastMove)
    displayBoard(GameBoard)

else:
    bot = Bot("X")
    bot.make_move(GameBoard)
    print("Last move: ", GameBoard._lastMove)
    displayBoard(GameBoard)

while not GameBoard.check_winner():
    if GameBoard._lastMove[0] == user_turn:
        bot.make_move(GameBoard)
        print("Last move: ", GameBoard._lastMove)
        displayBoard(GameBoard)
    else:
        userMakeMove(user_turn, GameBoard)
        print("Last move: ", GameBoard._lastMove)
        displayBoard(GameBoard)

print("\n", GameBoard.check_winner(), "won the game!")
