from gameboard import *
from player import *


print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board

board = GameBoard() 

# Create a new Player called played starting at position 3,2

played = Player(3, 2)
        
while True:
    board.printBoard(played.rowPosition, played.columnPosition)
    selection = input("Make a move: ")
    # TODO
    isValid = GameBoard.checkMove(board, testRow=played.rowPosition, testColumn=played.columnPosition)
    isWinner = GameBoard.checkWin(played, playerRow=played.rowPosition, playerColumn=played.columnPosition)
    # Move the player through the board

    if selection == 'w' and isValid == True:
        Player.moveUp(played, rowPosition = played.rowPosition-1)
        if  isWinner == True:
            break
    elif selection == 's' and isValid == True:
        Player.moveDown(played, rowPosition= played.rowPosition+1)
        if isWinner == True:
            break
    elif selection == 'a' and isValid == True:
        Player.moveLeft(played, columnPosition= played.columnPosition-1)
        if isWinner == True:
            break
    elif selection == 'd' and isValid == True:
        Player.moveRight(played, columnPosition= played.columnPosition+1)
        if isWinner == True:
            break
    else:
        print("Try again!")

        # Check if the player has won, if so print a message and break the loop!
