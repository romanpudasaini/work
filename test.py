#   fabbinanci series

num = int(input("input the number:"))
n1,n2=0,1
count=0
if num <= 0:
    print("enter grater than 1")
elif num == 1:
    print(n1)
else:
    while count < num :
        print(n1)
        sum = n1+n2
        n1 = n2
n = int(input('Enter length of the pattern: '))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print( )   


# n = int(input('ENter length of the pattern: '))

# for i in range(n):
#     for j in range(2*(n-i)):  # first loop for empty space
#         print(' ',end='')

#     for j in range(i+1):   #second loop for printing *
#         print('*',end=' ')

#     print()



# n = int(input('Enter length of the pattern: '))
# for i in range(n):
#      for j in range(n-i):
#          print("*",end=" ")
#      print()    



# TIK TAC TOE

# board = [[" " for i in range(3)] for j in range(3)]

# def draw_board():
#     print("  0 1 2")
#     for i, row in enumerate(board):
#         print(i, *row)

# def get_move(player):
#     while True:
#         try:
#             x = int(input("Enter the row (0-2) for player {}: ".format(player)))
#             y = int(input("Enter the column (0-2) for player {}: ".format(player)))
#             if x in range(3) and y in range(3) and board[x][y] == " ":
#                 board[x][y] = player
#                 return
#             else:
#                 print("Invalid move, try again")
#         except ValueError:
#             print("Invalid input, try again")

# def has_won(player):
#     # check rows
#     for row in board:
#         if row == [player, player, player]:
#             return True
#     # check columns
#         if board[0][col] == player and board[1][col] == player and board[2][col] == player:
#             return True
#     # check diagonals
#     if board[0][0] == player and board[1][1] == player and board[2][2] == player:
#         return True
#     if board[0][2] == player and board[1][1] == player and board[2][0] == player:
#         return True
#     return False

# def main():
#     while True:
#         draw_board()
#         get_move("X")
#         if has_won("X"):
#             print("X has won!")
#             break
#         draw_board()
#         get_move("O")
#         if has_won("O"):
#             print("O has won!")
#             break

# main()






# # LUDO
# import random

# # Constants
# NUM_PLAYERS = 4
# NUM_PIECES_PER_PLAYER = 4

# # The board is a 4x4 grid of squares
# BOARD_SIZE = 4

# # Each square has a number, representing the number of spaces a player's piece should move
# # For example, if a player rolls a 4 and lands on a square with value 2, the player's piece should move 2 spaces
# SQUARES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

# # A player's pieces are represented by a list of integers, where each integer represents the position of the piece on the board
# # For example, [1, 3, 15, 19] means that the player has one piece on the first square, one piece on the third square, etc.
# POSITIONS = [[1, 3, 15, 19], [5, 7, 21, 23], [9, 11, 25, 27], [13, 17, 29, 31]]

# # The index of the player's list in POSITIONS represents the player's number
# # For example, POSITIONS[0] is the list of positions for player 0


# def roll_die():
#     """Returns a random number between 1 and 6"""
#     return random.randint(1, 6)


# def move_piece(player, piece, roll):
#     """Moves the given piece for the given player by the given number of spaces"""
#     position = POSITIONS[player][piece]
#     position += roll
#     if position > 53:
#         position -= 53
#     POSITIONS[player][piece] = position


# def main():
#     """Plays a game of Ludo"""
#     turn = 0  # The number of the player whose turn it is
#     while True:
#         print(f"Player {turn}'s turn")
#         roll = roll_die()
#         print(f"Roll: {roll}")
#         valid_choices = []
#         for i, position in enumerate(POSITIONS[turn]):
#             if position == 0:  # If the piece is in the starting area
#                 valid_choices.append(i)
#             elif SQUARES[position - 1] == roll:  # If the player rolled the number on the square they are on
#                 valid_choices.append(i)
#         if valid_choices:  # If the player has any valid moves
#             print(f"Valid choices: {valid_choices}")
#             choice = int(input("Choose a piece to move: "))
#             while choice not in valid_choices:
#                 print("Invalid choice, try again")
#                 choice = int(input("Choose a piece to move: "))
#             move_piece(turn, choice, roll)
#         else:
#             print("No valid moves")
#         turn = (turn + 1) % NUM_PLAYERS  # Advance to the next player's turn


# if __name__ == "__main__":
#     main()
