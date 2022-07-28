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
    label.pack()


root = Tk()
#Screen Resolution
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
#Program position
x = width/2 - 300
y = height/2 - 300
#Create a title
root.title("Gerador Euromilhões")
root.geometry("%dx%d+%d+%d"%(300,300,x,y))
root.resizable(False,False)
#Create a button

button = Button(root,text="Gerar",command= lambda: printCode())
button.pack()
#Loop the program 
root.mainloop()