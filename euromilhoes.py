from itertools import starmap
from tkinter import *
import random
import array as ar
from turtle import width

def getNumbers():
    number = []
    for i in range(5):
        number.append(random.randint(1,50))
    return number
def getStar():
    star= []
    for i in range(2):
        star.append(random.randint(1,50))
    
    return star
def printCode():
    
    label = Label(root,text="Stars: "+str(getNumbers()) +"Numbers: "+ str(getStar()))
    label.place(x=150,y=150)


root = Tk()
root.config(background="black")
#Screen Resolution
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
#Program position
x = width/2 -  500
y = height/2 - 200
#Create a title
root.title("Gerador Euromilhões")
root.geometry("%dx%d+%d+%d"%(500,200,x,y))
root.resizable(False,False)
#Create a label
label = Label(root,text="Euromilhões number Generator",font=('Arial',20,'bold'),fg='#00FF00',bg='black')
label.place(x=30,y=30)
#Create a button

button = Button(root,text="Gerar",command= lambda: printCode())
button.place(x=230,y=100)
#Loop the program 
root.mainloop()