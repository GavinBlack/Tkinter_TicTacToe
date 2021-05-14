# Click Counter
# Demonstrates binding an event with an event handler

from tkinter import *
import random

class Application(Frame):
    """ GUI application""" 
    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        """ Create buttons and labels """

        self.directions = Label(self,text="First player to get 3 in a row")
        self.directions.grid(row=0,column=0,columnspan=3, sticky = W)
        self.next = Button(self,text="Start", command=self.next)
        self.next.grid(row=1,column=1)

    def next(self):
        self.directions.grid_remove()
        self.next.grid_remove()

        self.playGame()

    def playGame(self):
        self.board = []
        self.totalTurns = 0
        self.alreadyUsed = [False] * 9
        self.someoneWon = False
        self.xWins = 0
        self.oWins = 0
        self.name = Label(self,text="Tic Tac Toe")
        self.name.grid(row=0,column=0,columnspan=3)
        self.divider = Label(self,text="-----------------------------")
        self.divider.grid(row=1,column=0,columnspan=3)



        #create the 9 buttons
        self.bttn1 = Button(self,text=" ",width=5,command=self.addToBoard1)
        self.bttn1.grid(row=2,column=0)
        self.bttn2 = Button(self,text=" ",width=5,command=self.addToBoard2)
        self.bttn2.grid(row=2,column=1)
        self.bttn3 = Button(self,text=" ",width=5,command=self.addToBoard3)
        self.bttn3.grid(row=2,column=2)
        self.bttn4 = Button(self,text=" ",width=5,command=self.addToBoard4)
        self.bttn4.grid(row=3,column=0)
        self.bttn5 = Button(self,text=" ",width=5,command=self.addToBoard5)
        self.bttn5.grid(row=3,column=1)
        self.bttn6 = Button(self,text=" ",width=5,command=self.addToBoard6)
        self.bttn6.grid(row=3,column=2)
        self.bttn7 = Button(self,text=" ",width=5,command=self.addToBoard7)
        self.bttn7.grid(row=4,column=0)
        self.bttn8 = Button(self,text=" ",width=5,command=self.addToBoard8)
        self.bttn8.grid(row=4,column=1)
        self.bttn9 = Button(self,text=" ",width=5,command=self.addToBoard9)
        self.bttn9.grid(row=4,column=2)

        #Win label
        self.winLabel = Label(self, text=" ")

        #Show stats
        self.stats = Button(self,text="Stats",width=5,command=self.stats)

        #Wins
        self.xWinsLabel = Label(self,text=" ")
        self.oWinsLabel = Label(self,text=" ")

        #Back button on stats page
        self.back = Button(self,text="Back",width=5,command=self.back)

        #Restart on ttt page
        self.restart = Button(self,text="Restart",width=5,command=self.restart)
 
        self.fillBoard(self.board)

    def stats(self):
        self.bttn1.grid_forget()
        self.bttn2.grid_forget()
        self.bttn3.grid_forget()
        self.bttn4.grid_forget()
        self.bttn5.grid_forget()
        self.bttn6.grid_forget()
        self.bttn7.grid_forget()
        self.bttn8.grid_forget()
        self.bttn9.grid_forget()
        self.winLabel.grid_forget()
        self.stats.grid_forget()

        self.xWinsLabel.grid(row=2,column=1)
        self.xWinsLabel["text"] = "X wins: " + str(self.xWins)
        self.oWinsLabel.grid(row=3,column=1)
        self.oWinsLabel["text"] = "O wins: " + str(self.oWins)
        self.back.grid(row=4,column=1)

    def clearBoard(self):
        self.bttn1["text"] = " "
        self.bttn2["text"] = " "
        self.bttn3["text"] = " "
        self.bttn4["text"] = " "
        self.bttn5["text"] = " "
        self.bttn6["text"] = " "
        self.bttn7["text"] = " "
        self.bttn8["text"] = " "
        self.bttn9["text"] = " "

    def back(self):
        self.xWinsLabel.grid_forget()
        self.oWinsLabel.grid_forget()
        self.back.grid_forget()

        self.bttn1.grid(row=2,column=0)
        self.bttn2.grid(row=2,column=1)
        self.bttn3.grid(row=2,column=2)
        self.bttn4.grid(row=3,column=0)
        self.bttn5.grid(row=3,column=1)
        self.bttn6.grid(row=3,column=2)
        self.bttn7.grid(row=4,column=0)
        self.bttn8.grid(row=4,column=1)
        self.bttn9.grid(row=4,column=2)
        self.restart.grid(row=5,column=1)

        
    def restart(self):
        self.clearBoard()
        self.restart.grid_forget()
        self.winLabel.grid_forget()
        self.board = []
        self.totalTurns = 0
        self.alreadyUsed = [False] * 9
        self.someoneWon = False
        self.fillBoard(self.board)
    
    def checkIfWin(self):
        #top horizontal check
        if ( (self.board[0][0] == "X" and self.board[0][1] == "X" and self.board[0][2] == "X") or
           (self.board[0][0] == "O" and self.board[0][1] == "O" and self.board[0][2] == "O") ):
               self.someoneWon = True  
        #middle horizontal check
        elif ( (self.board[1][0] == "X" and self.board[1][1] == "X" and self.board[1][2] == "X") or
             (self.board[1][0] == "O" and self.board[1][1] == "O" and self.board[1][2] == "O") ):
                 self.someoneWon = True
        #bottom horizontal check
        elif ( (self.board[2][0] == "X" and self.board[2][1] == "X" and self.board[2][2] == "X") or
             (self.board[2][0] == "O" and self.board[2][1] == "O" and self.board[2][2] == "O") ):
                 self.someoneWon = True
        #left vertical check
        elif ( (self.board[0][0] == "X" and self.board[1][0] == "X" and self.board[2][0] == "X") or
             (self.board[0][0] == "O" and self.board[1][0] == "O" and self.board[2][0] == "O") ):
                 self.someoneWon = True
        #middle vertical check
        elif ( (self.board[0][1] == "X" and self.board[1][1] == "X" and self.board[2][1] == "X") or
             (self.board[0][1] == "O" and self.board[1][1] == "O" and self.board[2][1] == "O") ):
                 self.someoneWon = True
        #right vertical check
        elif ( (self.board[0][2] == "X" and self.board[1][2] == "X" and self.board[2][2] == "X") or
             (self.board[0][2] == "O" and self.board[1][2] == "O" and self.board[2][2] == "O") ):
                 self.someoneWon = True
        #diagonal top left to bottom right check
        elif ( (self.board[0][0] == "X" and self.board[1][1] == "X" and self.board[2][2] == "X") or
             (self.board[0][0] == "O" and self.board[1][1] == "O" and self.board[2][2] == "O") ):
                 self.someoneWon = True
        #diagonal top right to bottom left check
        elif ( (self.board[2][0] == "X" and self.board[1][1] == "X" and self.board[0][2] == "X") or
             (self.board[2][0] == "O" and self.board[1][1] == "O" and self.board[0][2] == "O") ):
                 self.someoneWon = True

        if self.someoneWon:
            if self.totalTurns % 2 == 0:
                self.winLabel["text"] = "O's won!"
                self.oWins += 1
            else:
                self.winLabel["text"] = "X's won!"
                self.xWins += 1
            self.winLabel.grid(row=5,column=1)
            self.stats.grid(row=6,column=1)
            
        if not self.someoneWon and self.totalTurns == 9:
            self.winLabel.grid(row=5,column=1)
            self.winLabel["text"] = "Tie!"
            self.restart.grid(row=6,column=1)     

    def addToBoard1(self):
        if self.totalTurns < 9 and not self.alreadyUsed[0] and not self.someoneWon:
            if self.totalTurns % 2 == 0:
                self.bttn1["text"] = "X"
                self.board[0][0] = "X"
            else:
                self.bttn1["text"] = "O"
                self.board[0][0] = "O"
            self.alreadyUsed[0] = True
            self.totalTurns += 1
            self.checkIfWin()
        
    def addToBoard2(self):
        if self.totalTurns < 9 and not self.alreadyUsed[1] and not self.someoneWon:
            if self.totalTurns % 2 == 0:
                self.bttn2["text"] = "X"
                self.board[0][1] = "X"
            else:
                self.bttn2["text"] = "O"
                self.board[0][1] = "O"
            self.alreadyUsed[1] = True
            self.totalTurns += 1
            self.checkIfWin()

    def addToBoard3(self):
        if self.totalTurns < 9 and not self.alreadyUsed[2] and not self.someoneWon:
            if self.totalTurns % 2 == 0:
                self.bttn3["text"] = "X"
                self.board[0][2] = "X"
            else:
                self.bttn3["text"] = "O"
                self.board[0][2] = "O"
            self.alreadyUsed[2] = True
            self.totalTurns += 1
            self.checkIfWin()

    def addToBoard4(self):
        if self.totalTurns < 9 and not self.alreadyUsed[3] and not self.someoneWon:
            if self.totalTurns % 2 == 0:
                self.bttn4["text"] = "X"
                self.board[1][0] = "X"
            else:
                self.bttn4["text"] = "O"
                self.board[1][0] = "O"
            self.alreadyUsed[3] = True
            self.totalTurns += 1
            self.checkIfWin()
        
    def addToBoard5(self):
        if self.totalTurns < 9 and not self.alreadyUsed[4] and not self.someoneWon:
            if self.totalTurns % 2 == 0:
                self.bttn5["text"] = "X"
                self.board[1][1] = "X"
            else:
                self.bttn5["text"] = "O"
                self.board[1][1] = "O"
            self.alreadyUsed[4] = True
            self.totalTurns += 1
            self.checkIfWin()

    def addToBoard6(self):
        if self.totalTurns < 9 and not self.alreadyUsed[5] and not self.someoneWon:
            if self.totalTurns % 2 == 0:
                self.bttn6["text"] = "X"
                self.board[1][2] = "X"
            else:
                self.bttn6["text"] = "O"
                self.board[1][2] = "O"
            self.alreadyUsed[5] = True
            self.totalTurns += 1
            self.checkIfWin()

    def addToBoard7(self):
        if self.totalTurns < 9 and not self.alreadyUsed[6] and not self.someoneWon:
            if self.totalTurns % 2 == 0:
                self.bttn7["text"] = "X"
                self.board[2][0] = "X"
            else:
                self.bttn7["text"] = "O"
                self.board[2][0] = "O"
            self.alreadyUsed[6] = True
            self.totalTurns += 1
            self.checkIfWin()

    def addToBoard8(self):
        if self.totalTurns < 9 and not self.alreadyUsed[7] and not self.someoneWon:
            if self.totalTurns % 2 == 0:
                self.bttn8["text"] = "X"
                self.board[2][1] = "X"
            else:
                self.bttn8["text"] = "O"
                self.board[2][1] = "O"
            self.alreadyUsed[7] = True
            self.totalTurns += 1
            self.checkIfWin()

    def addToBoard9(self):
        if self.totalTurns < 9 and not self.alreadyUsed[8] and not self.someoneWon:
            if self.totalTurns % 2 == 0:
                self.bttn9["text"] = "X"
                self.board[2][2] = "X"
            else:
                self.bttn9["text"] = "O"
                self.board[2][2] = "O"
            self.alreadyUsed[8] = True
            self.totalTurns += 1
            self.checkIfWin()
        

    def fillBoard(self,board):
        empty = []
        for i in range(1,10):
            empty.append("")
            if i % 3 == 0:
                board.append(empty)
                empty = []
            
def main():   
    # main
    root = Tk()
    root.title("Tic-tac-toe")
    root.geometry("150x170")
    app = Application(root)
    root.mainloop()

main()


