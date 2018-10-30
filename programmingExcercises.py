#############################theory quesition###########################################################################
"""
1. a True The second player will play optimally, and so is perfectly predictable up to ties. Knowing which of two equally
good moves the opponent will make does not change the value of the game to the first player's move.
b. False . In a partially observable game, knowing the second play's move tells the first player additional information
about the game state that would otherwise be available only to the second player.
c. False. Backgammon is a game of chance, and the opponent may consistently roll much better dice. The correct statement
is that the expected winnings are optimal.

2 constraint : A constraint is a restriction on the possible values of two or more variables.
backtracking search : Backtracking search is a kind of depth- first search. For a certain search tree, backtracking and
DFS, the main difference is that backtracking method is not in the solution process . The complete tree structure is
preserved, while the depth-first search records the complete search tree/
arc consistency: A directed arc from variable A to variable B in a CSP is ar consistent if, for every value in the currents
domain of A, there is some consistent value of B.
Backjumpting: Backjumping is a way of making backtracking search more efficient,by jumping back more than one level when
a dead end is reached.
Min-conflicts is a heuristic for use with local search on CSP problems. The heuristic says that when given a variable to
modify. choose the value that conflicts with the fewest number of other variables
cycle cutset A cycle cutset is a set of variables which when removed from the constraint graph make it acyclic when the
variable of a cycle cutset are instantiated the remainder of the CSP can be solved in lineat time.

3.The most constrained variable makes sense because it chooses a variable that is likely to cause a failure, and it is
more efficient to fall as early as possible. The least constraining value heuristic makes sense because it allow ot allows
the most chances for future assignments to avoid conflict.

4 This procedure will give incorrecct results. Mathematically, the procedure amounts to assuming that averaging that
commutes with min and max, which it does not. Intuitively, the choices made by each player in the deterministic trees are
based on full knowledge of future dice rolls, and bear no necessary relationship to the moves made without such knowledge

"""







#######################################practice 3-1#####################################################################

import random

your_number = input("Please enter the integer number you guess it is :  (0 to 100)")
your_number = int(your_number)
system_number = random.randint(0,100)
while your_number != system_number:
    if your_number> system_number and your_number<=system_number*10:
        print("You guess high!")
        your_number = input("Please enter another number you guess closer:")
        your_number = int(your_number)
    elif your_number> system_number*10:
        print("You guess too much high!")
        your_number = input("Please enter another number you guess closer:")
        your_number = int(your_number)
    elif your_number < system_number and your_number>= system_number/10:
        print("You guess low!")
        your_number = input("Please enter another number you guess closer:")
        your_number = int(your_number)
    elif your_number < system_number/10:
        print("You guess too much low!")
        your_number = input("Please enter another number you guess closer:")
        your_number = int(your_number)
if system_number == your_number:
    print("You guess correctly! Congratulations!")
print("The number is : "+str(system_number))



#######################################practice 3-2#####################################################################
import random

print("There are 3 numbers, please Guess what it is.")
print("The clue I gave is:")
print("When I say:  \t                 It means:")
total_error = "Error"
right_number = "Only the number is correct"
correct = "Absolutely right"
print(total_error +"\t                         The 3 numbers are not in the mystical numbers")
print(right_number +"\t     The number is correct but the position is not")
print(correct + "\t             Numbers are right and positions are too")
print("Now there are 3 numbers, you have 10 chance to guess it.")
print()
print()
number = random.sample(range(1,10),3)

your_number = input("Please enter 3 different numbers together:")
while len(your_number)!= 3 or your_number[0]== your_number[1] or your_number[1] == your_number[2] or your_number[0] == your_number[2]:
    your_number = input("Error!! Please enter 3 different number:")

anser = []
for i in range(len(your_number)):
    if int(your_number[i]) == number[i]:
        anser.append(correct)

    elif int(your_number[i]) in number and int(your_number[i])!= number[i]:
      anser.append(right_number)
    elif int(your_number[i]) not in number:
      anser.append(total_error)
n = 0
while n < 10:
    if anser != [correct,correct,correct]:
        print(anser)
        your_number = input("You answer is not correct please reenter one:")
        while len(your_number) != 3 or your_number[0] == your_number[1] or your_number[1] == your_number[2] or \
                your_number[0] == your_number[2]:
            your_number = input("Error!! Please enter 3 different number:")
        anser = []
        for i in range(len(your_number)):
            if int(your_number[i]) == number[i]:
                anser.append(correct)

            elif int(your_number[i]) in number and int(your_number[i]) != number[i]:
                anser.append(right_number)
            elif int(your_number[i]) not in number:
                anser.append(total_error)
        n += 1
    else:

        print("You answer is correct! Congratulations!")
        print(number)
        break
if n >= 10 :
    print("You losed.Sorry! The answer is :")
    print(anser)
print("Do you want to play again? (yes or no)")


#######################################practice 3-3#####################################################################

from tkinter import *
root = Tk()

language = ['C','python','php','html','SQL','java']
movie = ['CSS','jQuery','Bootstrap']

list1 = Listbox(root)
list2 = Listbox(root)

for item in language:
    list1.insert(0,item)
for item in movie:
    list2.insert(0,item)

list1.pack()
list2.pack()
root.mainloop()


#######################################practice 3-4#####################################################################


import tkinter
import math
import tkinter.messagebox

class Calculator:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.minsize(280,450)
        self.root.maxsize(280,480)
        self.root.title("Simplified Calculator")
        self.result = tkinter.StringVar()
        self.result.set(0)
        self.lists =[]
        self.ispressign = False
        self.layout()
        self.root.mainloop()

    def layout(self):
        result = tkinter.StringVar()
        result.set(0)
        show_label = tkinter.Label(self.root, bd = 3, bg = "white" , font = ('宋体',30), anchor = "e", textvariable =self.result)
        show_label.place(x = 5,y =20 ,width = 270,height = 80)

        button_mc =tkinter.Button(self.root, text = "MC", command = self.wait)
        button_mc.place(x=5,y=100,width = 50,height = 50)

        button_mr = tkinter.Button(self.root, text="MR", command=self.wait)
        button_mr.place(x=60, y=100, width=50, height=50)

        button_ms = tkinter.Button(self.root, text="MS", command=self.wait)
        button_ms.place(x=115, y=100, width=50, height=50)

        button_mplus = tkinter.Button(self.root, text="M+", command=self.wait)
        button_mplus.place(x=170, y=100, width=50, height=50)

        button_mminus = tkinter.Button(self.root, text="M-", command=self.wait)
        button_mminus.place(x=225, y=100, width=50, height=50)

        button_del = tkinter.Button(self.root, text="←", command=self.dele_one)
        button_del.place(x=5, y=155, width=50, height=50)

        button_ce = tkinter.Button(self.root, text="CE", command=lambda:self.result.set(0) )
        button_ce.place(x=5, y=155, width=50, height=50)

        button_del = tkinter.Button(self.root, text="←", command=self.dele_one)
        button_del.place(x=60, y=155, width=50, height=50)

        button_C = tkinter.Button(self.root, text="C", command=self.sweepress)
        button_C.place(x=115, y=155, width=50, height=50)

        button_pm = tkinter.Button(self.root, text="±", command=self.pm)
        button_pm.place(x=170, y=155, width=50, height=50)

        button_sqr = tkinter.Button(self.root, text="√", command=self.sqr)
        button_sqr.place(x=225, y=155, width=50, height=50)

        button_del = tkinter.Button(self.root, text="←", command=self.dele_one)
        button_del.place(x=5, y=155, width=50, height=50)

        button_seven = tkinter.Button(self.root, text="7", command=lambda: self.pressnum("7"))
        button_seven.place(x=5, y=210, width=50, height=50)

        button_eight = tkinter.Button(self.root, text="8", command=lambda: self.pressnum("8"))
        button_eight.place(x=60, y=210, width=50, height=50)

        button_nine = tkinter.Button(self.root, text="9", command=lambda: self.pressnum("9"))
        button_nine.place(x=115, y=210, width=50, height=50)

        button_division = tkinter.Button(self.root, text="÷", command=lambda :self.presscalculate("/"))
        button_division.place(x=170, y=210, width=50, height=50)

        button_remainder = tkinter.Button(self.root, text="//", command=lambda :self.presscalculate("//"))
        button_remainder.place(x=225, y=210, width=50, height=50)

        button_four = tkinter.Button(self.root, text="4", command=lambda: self.pressnum("4"))
        button_four.place(x=5, y=265, width=50, height=50)


        button_five = tkinter.Button(self.root, text="5", command=lambda: self.pressnum("5"))
        button_five.place(x=60, y=265, width=50, height=50)

        button_six = tkinter.Button(self.root, text="6", command=lambda: self.pressnum("6"))
        button_six.place(x=115, y=265, width=50, height=50)

        button_mutip = tkinter.Button(self.root, text="×", command=lambda :self.presscalculate("×"))
        button_mutip.place(x = 170, y=265, width=50, height=50)

        button_recip = tkinter.Button(self.root, text="1/x", command=lambda: self.ds)
        button_recip.place(x=225, y=265, width=50, height=50)

        button_one = tkinter.Button(self.root, text="1", command=lambda: self.pressnum("1"))
        button_one.place(x=5, y=320, width=50, height=50)

        button_two = tkinter.Button(self.root, text="2", command=lambda: self.pressnum("2"))
        button_two.place(x=60, y=320, width=50, height=50)

        button_three = tkinter.Button(self.root, text="3", command=lambda: self.pressnum("3"))
        button_three.place(x=115, y=320, width=50, height=50)

        button_minus = tkinter.Button(self.root, text="-", command=lambda: self.presscalculate("-"))
        button_minus.place(x=170, y=320, width=50, height=50)

        button_eq = tkinter.Button(self.root, text="=", command=lambda: self.pressequal())
        button_eq.place(x=225, y=320, width=50, height=105)

        button_zero = tkinter.Button(self.root, text="0", command=lambda :self.pressnum("0"))
        button_zero.place(x=5, y=375, width=105, height=50)

        button_point= tkinter.Button(self.root, text=".", command=lambda: self.pressnum("."))
        button_point.place(x=115, y=375, width=50, height=50)

        button_plus = tkinter.Button(self.root, text="+", command=lambda: self.presscalculate())
        button_plus.place(x=170, y=375, width=50, height=50)


    def pressnum(self,num):
        if self.ispressign == False:
            pass
        else:
            self.result.set(0)
            self.ispressign = False
        if num == ".":
            num = "0."
        oldnum = self.result.get()
        if oldnum == "0":
            self.result.set(num)
        else:
            newnum = oldnum + num
            self.result.set(newnum)

    def presscalculate(self,sign):
        num = self.result.get()
        self.lists.append(num)
        self.lists.append(sign)
        self.ispressign = True

    def pressequal(self):
        curnum = self.result.get()
        self.lists.append(curnum)
        calculatestr = ''. join(self.lists)
        endnum = eval(calculatestr)
        self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispressign = True
        self.lists.clear()

    def wait(self):
        tkinter.messagebox.showinfo('','Sorry, This function is still tried to implement. Please wait!')

    def dele_one(self):
        if self.result.get() == '' or self.result.get() == "0":
            self.result.set('0')
            return
        else :
            num = len(self.result.get())
            if num >1 :
                strnum = self.result.get()
                strnum = strnum[0:num-1]
                self.result.set(strnum)
            else:
                self.result.set('0')

    def pm(self):
        strnum = self.result.get()
        if strnum[0] == "-":
            self.result.set(strnum[1:])
        elif strnum[0] != '-' and strnum != "0":
            self.result.set('-' + strnum)


    def ds(self):
        dsnum = 1/int(self.result.get())
        self.result.set(str(dsnum)[:10])
        if self.lists != 0:
            self.ispressign = True
        self.lists.clear()


    def sweepress(self):
        self.lists.clear( )
        self.result.set(0)

    def sqr(self):
        strnum = float(self.result.get())
        endnum = math.sqrt(strnum)
        if str(endnum)[-1] == "0":
            self.result.set(str(endnum)[:-2])
        else:
            self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispressign = True
            self.lists.clear()

mycalculator = Calculator()

#######################################practice 3-5#####################################################################

from tkinter import *
import time
import random
import _tkinter


tk = Tk()
tk.title("Pinball Game")
canvas = Canvas(tk, width = 800, height = 600, bg = "pink", bd = 0,highlightthickness = 0)
tk.resizable(0,0)
canvas.pack()
tk.update()

class Ball: # Class of Ball
    def __init__(self,canvas,paddle,color): # initialize the ball
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10, 25, 25, fill = color) # draw a ball on the canvas
        self.canvas.move(self.id,240,100) # at the start state the position of ball
        stat = [-3,-2,-1,1,2,3]
        random.shuffle(stat)
        self.x = stat[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3]<= paddle_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y =3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x = -3
class Paddle:
    def __init__(self,canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,150,10,fill = color)
        self.canvas.move(self.id ,400,450)
        self.x = 0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("<Key-Left>",self.turn_left)
        self.canvas.bind_all("<Key-Right>", self.turn_right)
    def turn_left(self,event):
        self.x = -5
    def turn_right(self,event):
        self.x = 5
    def draw(self):
        pos = self.canvas.coords(self.id)
        self.canvas.move(self.id,self.x,0)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
paddle = Paddle(canvas,"blue")
ball = Ball(canvas,paddle,"red")
while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)










