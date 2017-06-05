from board import Board
from bot import Bot
from funcs import userMakeMove, get_valid_input

# Init game board
GameBoard = Board()

# Welcome the user
print("----------------Welcome to Tic-Tac-Toe Game!-------------------------")
print("In this game you will be playing with a bot")

# Ask user to pick turn
print("X - make a move first")
user_turn = get_valid_input("Please, pick your turn: 'X' or 'O' and type your choice here: ", "xoXO").upper()
print(GameBoard)

# Handle user pick and make the first move
if user_turn == "X":
    # Create a bot
    bot = Bot("O")
    # User makes the first move
    userMakeMove(user_turn, GameBoard)
    bot.decision_tree.set_initial_root(GameBoard)
else:
    # Create a bot
    bot = Bot("X")
    # Bot makes the first move
    bot.decision_tree.set_initial_root(GameBoard)
    bot.make_first_move(GameBoard)

print("Last move: ", GameBoard._lastMove)
print(GameBoard)

if GameBoard._lastMove[0] != user_turn:
    userMakeMove(user_turn, GameBoard)
    bot.decision_tree.set_initial_root(GameBoard)
    print("Last move: ", GameBoard._lastMove)
    print(GameBoard)


# launch the game loop
while not GameBoard.check_winner():
    if GameBoard._lastMove[0] == user_turn:
        bot.make_move(GameBoard)
        print("Last move: ", GameBoard._lastMove)
        print(GameBoard)
    else:
        userMakeMove(user_turn, GameBoard)
        print("Last move: ", GameBoard._lastMove)
        print(GameBoard)

print("\n                ", GameBoard.check_winner(),  "won the game!")
