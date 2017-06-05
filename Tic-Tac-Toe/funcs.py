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
    print("\nIt's your turn to make a move!")
    coord = input("Please type the coord below - first row, then col: ")
    coord = [int(i) for i in coord.split()]
    coord = (coord[0], coord[1])
    print(coord)
    if coord in board.availible_cells:
        if board.put(user_turn, coord):
            pass
        else:

            print("Your move is not valid, please, try again.\n")
            userMakeMove(user_turn, board)
    else:
        print("Your move is not valid, please, try again.")
        userMakeMove(user_turn, board)
