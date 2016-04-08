def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):
    print('Checking if ' + player + ' is a winner...')
    if theBoard.get('top-L') == theBoard.get('top-M') == theBoard.get('top-R') == turn:
        return True
    elif theBoard.get('mid-L') == theBoard.get('mid-M') == theBoard.get('mid-R') == turn:
        return True
    elif theBoard.get('low-L') == theBoard.get('low-M') == theBoard.get('low-R') == turn:
        return True
    elif theBoard.get('top-L') == theBoard.get('mid-L') == theBoard.get('low-L') == turn:
        return True
    elif theBoard.get('top-M') == theBoard.get('mid-M') == theBoard.get('low-M') == turn:
        return True
    elif theBoard.get('top-R') == theBoard.get('mid-R') == theBoard.get('low-R') == turn:
        return True
    elif theBoard.get('top-L') == theBoard.get('mid-M') == theBoard.get('low-R') == turn:
        return True
    elif theBoard.get('top-R') == theBoard.get('mid-M') == theBoard.get('low-L') == turn:
        return True
        
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9):
        printBoard(board)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        board[move] = turn
        if( checkWinner(board, 'X') ):
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ):
            print('O wins!')
            break
    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)
    
