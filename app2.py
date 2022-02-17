import random
from tkinter import *
window=Tk()
window.title=("Calculatrice")
window.config(bg="lightblue")
window.geometry("1000x1000")
e=""
e_l=StringVar()
label=Label(window,bg="#fff",width=70,height=5,textvariable=e_l,font=('Arial', 20))
label.pack()
frame2=Frame(window)
frame2.pack()
x=1
a=["*","-","+","=","/","."]


def b(x):
    global e
    e= e + str(x)
    e_l.set(e)

def equal():
   global e
   try:
       x=str(eval(e))
       e_l.set(x)
       e=x
   except ZeroDivisionError:
       e_l.set("you cannot divise by 0")
       e=""
   except SyntaxError:
       e_l.set("entrer un nombre")
       e = ""

def clear():
    global e
    e=""
    e_l.set(e)


button=Button(frame2,bg="#365",width=7,height=2,text=1,font=('Arial',20),command=lambda :b(1))
button.grid(row=0,column=0)

button = Button(frame2, bg="#365", width=7, height=2, text=2, font=('Arial', 20),command=lambda :b(2))
button.grid(row=0,column=1)

button = Button(frame2, bg="#365", width=7, height=2, text=3, font=('Arial', 20),command=lambda :b(3))
button.grid(row=0,column=2)

button = Button(frame2, bg="#365", width=7, height=2, text="*", font=('Arial', 20),command=lambda :b("*"))
button.grid(row=0,column=3)

button = Button(frame2, bg="#365", width=7, height=2, text=4, font=('Arial', 20),command=lambda :b(4))
button.grid(row=1,column=0)

button = Button(frame2, bg="#365", width=7, height=2, text=5, font=('Arial', 20),command=lambda :b(5))
button.grid(row=1,column=1)

button=Button(frame2,bg="#365", width=7, height=2, text=6, font=('Arial', 20),command=lambda :b(6))
button.grid(row=1,column=2)


button=Button(frame2,bg="#365",width=7,height=2,text="-",font=('Arial',20),command=lambda :b("-"))
button.grid(row=1,column=3)

button = Button(frame2, bg="#365", width=7, height=2, text=7, font=('Arial', 20),command=lambda :b(7))
button.grid(row=2,column=0)

button = Button(frame2, bg="#365", width=7, height=2, text=8, font=('Arial', 20),command=lambda :b(8))
button.grid(row=2,column=1)

button = Button(frame2, bg="#365", width=7, height=2, text=9, font=('Arial', 20),command=lambda :b(9))
button.grid(row=2,column=2)

button = Button(frame2, bg="#365", width=7, height=2, text="+", font=('Arial', 20),command=lambda :b("+"))
button.grid(row=2,column=3)

button = Button(frame2, bg="#365", width=7, height=2, text=0, font=('Arial', 20),command=lambda :b(0))
button.grid(row=3,column=0)

button = Button(frame2, bg="#365", width=7, height=2, text=".", font=('Arial', 20),command=lambda :b("."))
button.grid(row=3,column=1)

button = Button(frame2, bg="#365", width=7, height=2, text="=", font=('Arial', 20),command=lambda :equal())
button.grid(row=3,column=2)

button = Button(frame2, bg="#365", width=7, height=2, text="/", font=('Arial', 20),command=lambda :b("/"))
button.grid(row=3,column=3)

button=Button(window,bg="#365", width=7, height=2, text="clear", font=('Arial', 20),command=lambda :clear())
button.pack()


window.mainloop()