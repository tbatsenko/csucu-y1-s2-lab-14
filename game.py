from board import Board


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
                s += "               " + str(i) + "     " + str(board._field[i][j]) + " "
            else:
                s += " " + str(board._field[i][j]) + " "
        if i < 2:
            s += "\n                  ------------------\n"
    print(s)




print("----------------Welcome to Tic-Tac-Toe Game!-------------------------")
print("In this game you will be playing with a bot")

print("X - make a move first")
user_turn = get_valid_input("Please, pick your turn: 'X' or 'O' and type your choice here: ", "xoXO").upper()

if user_turn == "X":
    bot_turn = "O"
else:
    bot_turn = "X"



displayBoard(GameBoard)
