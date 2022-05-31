from logging import root
from tkinter import DISABLED, Button,Canvas,Tk
from turtle import bgcolor
from PIL import Image,ImageTk
from os import system
from threading import Thread
import tkinter.font as font
from playsound import playsound

root=Tk()
root.title("Tic Tac Toe")
root.geometry("1920x1080")
canvas1 = Canvas( root, width = 1920,height = 1080)
canvas1.pack(fill = "both", expand = True)
img=Image.open("bg.jpg")
resized_image= img.resize((1920,1080), Image.ANTIALIAS)
bg=ImageTk.PhotoImage(resized_image)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")
def run_app():
    canvas1.itemconfig(2,state="hidden")
    system("python single.py")
def run_app1():
    canvas1.itemconfig(2,state="hidden")
    system("python client.py")
    #one machine should have server.py in system() functin in this function to run multi player.
buttonFont = font.Font(family='Helvetica', size=12, weight='bold')
splayer = Button(root, text = "SINGLE PLAYER",width=30,height=3,command=Thread(target=run_app).start,font=buttonFont).place(x = 630, y = 270)
mplayer = Button(root, text = "MULTI PLAYER",width=30,height=3,command=Thread(target=run_app1).start,font=buttonFont).place(x = 630, y = 360)
root.mainloop()