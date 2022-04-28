# Prove: Developer - Solo Code Submission
# Created by Hunter Heuser

# runs program
def main():
    player = next_player("")
    board = game_board()
    while not (has_winner(board) or match_draw(board)):
        display_board(board)
        player_move(player, board)
        player = next_player(player)
    display_board(board)
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

# determine if the match is a draw
def match_draw(board):
    for tile in range(9):
        if board[tile] != "x" and board[tile] != "o":
            return False
    return True 

# check for winner
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

# allow a player to choose a tile
def player_move(player, board):
    tile = int(input(f"{player}'s turn to choose a sqaure (1-9): "))
    board[tile - 1] = player

# next player's turn
def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

# run main function
if __name__ == "__main__":
    main()