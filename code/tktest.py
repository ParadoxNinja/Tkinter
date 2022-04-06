from cgitb import text
from tkinter import *

from setuptools import Command

def multiplication():
    answer = float(e1Value.get())*float(e2Value.get())
    t1.insert(END,answer)

def division():
    answer = float(e1Value.get())/float(e2Value.get())
    t1.insert(END,answer)

def addition():
    answer = float(e1Value.get())+float(e2Value.get())
    t1.insert(END,answer)

def subtraction():
    answer = float(e1Value.get())-float(e2Value.get())
    t1.insert(END,answer)

def clearing():
    t1.delete(1.0,END)

w = Tk()

multiply = Button(w,text= "Multiply",command=multiplication)
multiply.grid(row=0,column = 0)

divide = Button(w,text= "Divide",command=division)
divide.grid(row=1,column = 0)

add = Button(w,text= "Add",command=addition)
add.grid(row=2,column = 0)

sub = Button(w,text= "Subtract",command=subtraction)
sub.grid(row=3,column = 0)

clear = Button(w,text="Clear", command=clearing)
clear.grid(row=3,column=3)


e1Value = StringVar()
e2Value = StringVar()
e1 = Entry(w,textvariable=e1Value)
e2 = Entry(w,textvariable=e2Value)
e1.grid(row= 1, column=2)
e2.grid(row= 2, column=2)

t1 = Text(w,height=1, width=20)
t1.grid(row=1,column=3)

w.mainloop()