from tkinter import *

Root = Tk()
canvas = Canvas(Root, width = 500, height = 500, bg = "white")
canvas.pack()

Score = 0

J = canvas.create_text(100, 100, text=("Score", Score), font=("Comic Sans", 50))

def change():
    global Score
    Score += 1
    J = canvas.create_text(100, 100, text=("Score", Score), font = ("Comic Sans", 50))

def changee():
    canvas.delete(J)
    print("del")

def do():
    change()
    changee()

B = Button(canvas, text = "change it", command = do)
B.place(x = 300, y = 300)