import random
#------Board class------
print("BINGO GAME")
class Board:
    def __init__ (self):
        self.position={}
        self.playBoard=[
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
        self.bingo={
            "row":[0,0,0,0,0],
            "col":[0,0,0,0,0],
            "diag":[0,0]
        }
        self.createBoard()
    
    def createBoard(self):        #create board by assigning random values
        choices=[i for i in range(1,26)]
        for i in range(5):
            for j in range(5):
                choice=random.choice(choices)
                self.playBoard[i][j]=choice
                choices.pop(choices.index(choice))
                self.position[choice]=(i,j)
        
    def updateBoard(self,val):         #updating the board based on the value
        x,y=self.position[val]
        self.playBoard[x][y]='X'
        self.updateBingo(x,y)
        
    def updateBingo(self,x,y):        #check for bingo value, i.e the bingo value                        will be incremented by one
        self.bingo["row"][x]+=1
        self.bingo["col"][y]+=1
        if x==y==2:
            self.bingo["diag"][0]+=1
            self.bingo["diag"][1]+=1
        elif x==y:
            self.bingo["diag"][0]+=1
        elif x+y==4:
            self.bingo["diag"][1]+=1
    
    def checkBingo(self):  #bingo check , if it assigns 5 thn stop the game and print who wins.
        return 5 in self.bingo["row"] or 5 in self.bingo["col"] or 5 in self.bingo["diag"]
        
        
#----------player class----------       
class Player(Board):    #board is passed to the player class.and initialised with the name.
    def __init__(self,name):
        self.name=name
        self.board=Board()
        
    def updatePlayerBoard(self,val):  #board has to be updated for each value
        self.board.updateBoard(val)
        
    def checkBingo(self):             #bingo check is done.
        return self.board.checkBingo()
        
        
#--------Game class-----------        
class Game:
    def displayBoard(self,player1,player2): #display the board of each player
        board1=player1.board.playBoard
        board2=player2.board.playBoard
        print("Player1"+"                          "+"Player2")
        for i in range(5):
            for j in board1[i]:
                if j=='X':
                    print(f" {j}",end=" ")
                elif j>9:
                    print(j,end=" ")
                else:
                    print(f"0{j}",end=" ")
            print(" "*10,end=" ")
            for j in board2[i]:
                if j=='X':
                    print(f" {j}",end=" ")
                elif j>9:
                    print(j,end=" ")
                else:
                    print(f"0{j}",end=" ")
            print()
        print()

#creating the game object        
game=Game()
player1=Player(name="player1")   #two players are created
player2=Player(name="player2")
game.displayBoard(player1,player2)   #displays the initial board status

#till match ends , the input is accepted    
while(True):
    val = int(input(f"{player1.name}'s turn : "))   #gets input value
    player1.updatePlayerBoard(val)         #updates the board
    player2.updatePlayerBoard(val)
    game.displayBoard(player1,player2)     #display the board

    if player1.checkBingo() and player2.checkBingo():  #bingo check 
        print("DRAW")
        break
    if player1.checkBingo():
        print(f"{player1.name} WON")
        break
    if player2.checkBingo():
        print(f"{player2.name} WON")
        break
    
    #for player2
    val = int(input(f"{player2.name}'s turn : "))
    player1.updatePlayerBoard(val)
    player2.updatePlayerBoard(val)
    game.displayBoard(player1,player2)

    if player1.checkBingo() and player2.checkBingo():
        print("DRAW")
        break
    if player1.checkBingo():
        print(f"{player1.name} WON")
        break
    if player2.checkBingo():
        print(f"{player2.name} WON")
        break
