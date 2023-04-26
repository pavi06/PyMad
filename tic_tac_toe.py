#getting input from user
def getInput(board):
    x,y=map(int,input("Enter row and col Position(1-3): ").split())
    if board[x-1][y-1]=='-':
        board[x-1][y-1]=currPlayer
    else:
        print("Oops! Already Used")
        getInput(board)

#Printing the board
def printBoard(board):
    print("-------Board-----")
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j],end="|")
        print()
  
#Horizontal check  
def checkHorizontal(board):
    global winner
    for i in range(3):
        k=board[i][0]
        c=1
        if k=='X' or k=='O':
            for j in range(1,3):
                if board[i][j]==k:
                    c+=1
            if c==3:
                winner=k
                return True
    return False

def checkVertical(board):
    global winner
    for i in range(3):
        k=board[0][i]
        c=1
        if k=='X' or k=='O':
            for j in range(1,3):
                if board[j][i]==k:
                    c+=1
            if c==3:
                winner=k
                return True
    return False

def checkDiagleft(board):
    global winner
    i=0
    k=board[0][0]
    c=0
    if k=='X' or k=='O':
        while(i<3 and board[i][i]==k):
            c+=1
            i+=1
        if c==3:
            winner=k
            return True
    return False

def checkDiagright(board):
    global winner
    i,j=2,2
    k=board[2][2]
    c=0
    if k=='X' or k=='O':
        while(i>=0 and j>=0 and i+j==3 and board[i][i]==k):
            c+=1
            i-=1
            j-=1
        if c==3:
            winner=k
            return True
    return False

def checkTie(board):
    global game
    c=0
    for i in range(3):
        for j in range(3):
            if board[i][j] != '-':
                c+=1
    if c==9:
        printBoard(board)
        print("Its a tie!!")
        game=False
    
def switchPlayer():
    global currPlayer
    if currPlayer=='X':
        currPlayer='O'
    else:
        currPlayer='X'
        
def checkWin(board):
    global game
    if checkHorizontal(board) or checkVertical(board) or checkDiagleft(board) or checkDiagright(board):
        printBoard(board)
        print(f"The winner is {winner}")
        game=False

#Main Program        
print("Tic Tac Toe")
#board creation
board=[['-']*3 for i in range(3)]
currPlayer='X'
winner=''
game=True


while(game):
    printBoard(board)
    getInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
