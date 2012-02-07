__author__ = 'harlanhowe'
board = []
turns = 0
start = ("P","P","P"," ","D","D","D") # this will change
solution = ("D","D","D"," ","P","P","P") # this won't.


def resetBoard():
    global board
    board = []
    board.extend(start)
    turns = 0
    
def spaceLocation():
    return board.index(" ")

def isLegalMove(loc):
    space = spaceLocation()
    if (loc<0) or (loc>len(board)-1):
        return False
    if (loc == space - 1) or (loc == space - 2) or (loc == space + 1) or (loc == space + 2):
        return True
    return False # if we haven't returned earlier, then it's a bad move.


def turn():
    global board
    while True:
        try:
            response = (int)(raw_input("Enter the next coin to move."))
        except Exception:
            print ("Please enter a number.")
            printBoard()
        if isLegalMove(response):
            break
        else:
            print ("That is not a legal move.")
            printBoard()

    empty = spaceLocation()
    print "Moving {0} from {1} to {2}".format (board[response],response,empty)
    board[empty] = board[response]
    board[response] = " "

def printBoard():
    output = "|"
    i = 0
    while i<len(board):
        output = output + ("{0}|".format(board[i]))
        i = i + 1
    print output
    print " 0 1 2 3 4 5 6"


def isGameOver():
    i = 0
    while i<len(board):
        if (board[i] != solution [i]):
            return False
        i = i + 1
    return True


def gameLoop():
    turns = 0
    while True:
        printBoard()
        turn()
        turns=turns+1
        if isGameOver():
            break
    printBoard()
    print ("Game over in {0} turns".format(turns))



gameLoop()