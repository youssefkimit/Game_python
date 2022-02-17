from tkinter import *
import random

def check():
    for i in range(3):
        if b[i][0]['text']==b[i][1]['text']==b[i][2]['text'] and not b[i][0]['text']=="":
            b[i][0].config(bg="green")
            b[i][1].config(bg="green")
            b[i][2].config(bg="green")
            return True
    for i in range(3):
        if b[0][i]['text']==b[1][i]['text']==b[2][i]['text'] and not b[0][i]['text']=="":
            b[0][i].config(bg="green")
            b[1][i].config(bg="green")
            b[2][i].config(bg="green")
            return True
    if b[0][0]['text']==b[1][1]['text']==b[2][2]['text'] and not b[1][1]['text']=="":
            b[0][0].config(bg="green")
            b[1][1].config(bg="green")
            b[2][2].config(bg="green")
            return True
    if b[0][2]['text']==b[1][1]['text']==b[2][0]['text'] and not b[1][1]['text']=="":
            b[0][2].config(bg="green")
            b[1][1].config(bg="green")
            b[2][0].config(bg="green")
            return True
    return False

def fill():
    for i in range(3):
        for j in range(3):
            if b[i][j]['text']=="":
                return False
    for i in range(3):
      for j in range(3):
        b[i][j].config(bg="yellow")
    return True

def affiche(i,j):
    global p
    if b[i][j]['text']=="" and not check():
        if p==pl[0]:
            b[i][j]['text']=p
            if not check() and not fill():
                p=pl[1]
                label.config(text= p + " turn ")
            elif check():
                label.config(text=" WIN ")
            elif fill():
                label.config(text=" Tie ! :")

        elif p == pl[1]:
            b[i][j]['text'] = p
            if not check() and not fill():
                p = pl[0]
                label.config(text=p + " turn ")
            elif check():
                label.config(text=" WIN ")
            elif fill():
                label.config(text=" Tie ! :")


def restart():
    global b
    for i in range(3):
        for j in range(3):
            b[i][j].config(text="",bg="#F0F0F0")

    p = random.choice(pl)
    label.config(text=p + " turn ")

window=Tk()
window.title=("Tic-Tac-Toe")
pl=["O","X"]
p=random.choice(pl)
b=[[0,0,0],[0,0,0],[0,0,0]]
label=Label(window,text= p + " turn ",font=('Arial',40),bg="green",width=30,height=2)
label.pack(side="top")
button1=Button(text="restart",font=('Arial',20),command=restart)
button1.pack(side="top")
frame=Frame(window)
frame.pack()

for i in range(3):
    for j in range(3):
        b[i][j]=Button(frame,text="",width="7",height="2", font=('Arial', 20),command=lambda row=i,column=j: affiche(row,column))
        b[i][j].grid(row=i,column=j)



window.mainloop()