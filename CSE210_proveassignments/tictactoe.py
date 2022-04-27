# Prove: Developer - Solo Code Submission
# Created by Hunter Heuser

# runs program
def main():
   print() 

# the game board
def game_board():
    board = []
    for tile in range(9):
        board.append(tile + 1)
    return board

# display the board
def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]} ")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]} ")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    # space between the board and terminal
    print()
