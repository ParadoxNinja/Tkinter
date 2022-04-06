from cgitb import text
from tkinter import *

from setuptools import Command

def multiply():
    answer = float(e1Value.get())*float(e2Value.get())
    t1.insert(END,answer)

w = Tk()
b1 = Button(w,text= "Execute",command=multiply)
b1.grid(row=0,column = 1)

e1Value = StringVar()
e2Value = StringVar()
e1 = Entry(w,textvariable=e1Value)
e2 = Entry(w,textvariable=e2Value)
e1.grid(row= 1, column=2)
e2.grid(row= 2, column=2)

t1 = Text(w,height=1, width=20)
t1.grid(row=1,column=4)

w.mainloop()