import imp
import pygame
from tkinter import Image, PhotoImage, Label, Button, Tk,messagebox
from threading import Thread
from random import choice
import random
pygame.mixer.init()
your_turn=True
computer_turn=False
count=0
window_closed=False
game_over=False

def bgMusic():
    pygame.mixer.music.load("m1.mp3")
    pygame.mixer.music.play()
def onclc():
    touch=pygame.mixer.Sound("m2.wav")
    pygame.mixer.Sound.play(touch)
bgMusic()

def on_closing():
    global window_closed
    window_closed=True
    root.destroy()
        
def show_result(a):
    if a=='win':
        messagebox.showinfo(a,'Congratulation!.. You Won The Match.')
    elif a=='lose':
        messagebox.showinfo(a,'You Lose The Match.')
    elif a=='tie':
        messagebox.showinfo(a,'There is a Tie.')
def check_win():
    global game_over
    if True:
        if grid_1.cget('image')=='pyimage2' and grid_2.cget('image')=='pyimage2' and grid_3.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                game_over=True
            elif your_image==round:
                show_result('lose')
                game_over=True
        elif grid_1.cget('image')=='pyimage2' and grid_4.cget('image')=='pyimage2' and grid_7.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                game_over=True
            elif your_image==round:
                show_result('lose')
                game_over=True
        elif grid_1.cget('image')=='pyimage2' and grid_5.cget('image')=='pyimage2' and grid_9.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                game_over=True
            elif your_image==round:
                show_result('lose')
                game_over=True
        elif grid_2.cget('image')=='pyimage2' and grid_5.cget('image')=='pyimage2' and grid_8.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                game_over=True
            elif your_image==round:
                show_result('lose')
                game_over=True
        elif grid_3.cget('image')=='pyimage2' and grid_6.cget('image')=='pyimage2' and grid_9.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                game_over=True
            elif your_image==round:
                show_result('lose')
                game_over=True
        elif grid_3.cget('image')=='pyimage2' and grid_5.cget('image')=='pyimage2' and grid_7.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                game_over=True
            elif your_image==round:
                show_result('lose')
                game_over=True
        elif grid_4.cget('image')=='pyimage2' and grid_5.cget('image')=='pyimage2' and grid_6.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                game_over=True
            elif your_image==round:
                show_result('lose')
                game_over=True
        elif grid_7.cget('image')=='pyimage2' and grid_8.cget('image')=='pyimage2' and grid_9.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                game_over=True
            elif your_image==round:
                show_result('lose')
                game_over=True
        
        elif grid_1.cget('image')=='pyimage3' and grid_2.cget('image')=='pyimage3' and grid_3.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                game_over=True
            elif your_image==cross:
                show_result('lose')
                game_over=True
        elif grid_1.cget('image')=='pyimage3' and grid_4.cget('image')=='pyimage3' and grid_7.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                game_over=True
            elif your_image==cross:
                show_result('lose')
                game_over=True
        elif grid_1.cget('image')=='pyimage3' and grid_5.cget('image')=='pyimage3' and grid_9.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                game_over=True
            elif your_image==cross:
                show_result('lose')
                game_over=True
        elif grid_2.cget('image')=='pyimage3' and grid_5.cget('image')=='pyimage3' and grid_8.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                game_over=True
            elif your_image==cross:
                show_result('lose')
                game_over=True
        elif grid_3.cget('image')=='pyimage3' and grid_6.cget('image')=='pyimage3' and grid_9.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                game_over=True
            elif your_image==cross:
                show_result('lose')
                game_over=True
        elif grid_3.cget('image')=='pyimage3' and grid_5.cget('image')=='pyimage3' and grid_7.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                game_over=True
            elif your_image==cross:
                show_result('lose')
                game_over=True
        elif grid_4.cget('image')=='pyimage3' and grid_5.cget('image')=='pyimage3' and grid_6.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                game_over=True
            elif your_image==cross:
                show_result('lose')
                game_over=True
        elif grid_7.cget('image')=='pyimage3' and grid_8.cget('image')=='pyimage3' and grid_9.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                game_over=True
            elif your_image==cross:
                show_result('lose')
                game_over=True
        elif(count==9):
            show_result('tie')
            game_over=True
        elif(your_turn!=True):
            compa_data()
clicked1 = False
clicked2 = False
clicked3 = False
clicked4 = False
clicked5 = False
clicked6 = False
clicked7 = False
clicked8 = False
clicked9 = False
def compa_data():
    global list1,a,clicked1,clicked2,clicked3,clicked4,clicked5,clicked6,clicked7,clicked8,clicked9,your_turn,computer_turn,count,game_over
    list1=[1,2,3,4,5,6,7,8,9]
    c=0
    while c==0 and game_over==False:
        a=random.choice(list1)
        if(a==1 and clicked1 == False):
            grid_1.config(image=computer_image)
            clicked1 = True
            your_turn=True
            computer_turn=False
            count+=1
            onclc()
            c+=1
            Thread(target=check_win).start()
        elif(a==2 and clicked2 == False):
            grid_2.config(image=computer_image)
            clicked2 = True
            your_turn=True
            computer_turn=False
            count+=1
            onclc()
            c+=1
            Thread(target=check_win).start()
        elif(a==3 and clicked3 == False):
            grid_3.config(image=computer_image)
            clicked3 = True
            your_turn=True
            computer_turn=False
            count+=1
            onclc()
            c+=1
            Thread(target=check_win).start()
        elif(a==4 and clicked4 == False):
            grid_4.config(image=computer_image)
            clicked4 = True
            your_turn=True
            computer_turn=False
            count+=1
            onclc()
            c+=1
            Thread(target=check_win).start() 
        elif(a==5 and clicked5 == False):
            grid_5.config(image=computer_image)
            clicked5 = True
            your_turn=True
            computer_turn=False
            count+=1
            onclc()
            c+=1
            Thread(target=check_win).start()   
        elif(a==6 and clicked6== False):
            grid_6.config(image=computer_image)
            clicked6 = True
            your_turn=True
            computer_turn=False
            count+=1
            onclc()
            c+=1
            Thread(target=check_win).start()
        elif(a==7 and clicked7 == False):
            grid_7.config(image=computer_image)
            clicked7 = True
            your_turn=True
            computer_turn=False
            count+=1
            onclc()
            c+=1
            Thread(target=check_win).start()
        elif(a==8 and clicked8 == False):
            grid_8.config(image=computer_image)
            clicked8 = True
            your_turn=True
            computer_turn=False
            count+=1
            onclc()
            c+=1
            Thread(target=check_win).start()
        elif(a==9 and clicked9 == False):
            grid_9.config(image=computer_image)
            clicked9 = True
            your_turn=True
            computer_turn=False
            count+=1
            onclc()
            c+=1
            Thread(target=check_win).start()
        
def set_image1():
    global clicked1
    global your_turn,count,computer_turn,game_over
    if clicked1 != True and your_turn==True and game_over==False:
        grid_1.config(image=your_image)
        clicked1 = True
        your_turn=False
        computer_turn=True
        count+=1
        onclc()
        Thread(target=check_win).start()

def set_image2():
    global clicked2
    global your_turn,count,computer_turn
    if clicked2 != True and your_turn==True and game_over==False:
        grid_2.config(image=your_image)
        clicked2 = True
        your_turn=False
        computer_turn=True
        count+=1
        onclc()
        Thread(target=check_win).start()

def set_image3():
    global clicked3,count,computer_turn
    global your_turn
    if clicked3 != True and your_turn==True and game_over==False:
        grid_3.config(image=your_image)
        clicked3 = True
        your_turn=False
        computer_turn=True
        count+=1
        onclc()
        Thread(target=check_win).start()
def set_image4():
    global clicked4,count,computer_turn
    global your_turn
    if clicked4 != True and your_turn==True and game_over==False:
        grid_4.config(image=your_image)
        clicked4 = True
        your_turn=False
        computer_turn=True
        count+=1
        onclc()
        Thread(target=check_win).start()
def set_image5():
    global clicked5,count
    global your_turn
    global computer_turn
    if clicked5 != True and your_turn==True and game_over==False:
        grid_5.config(image=your_image)
        clicked5 = True
        your_turn=False
        computer_turn=True
        count+=1
        onclc()
        Thread(target=check_win).start()
def set_image6():
    global clicked6,count,computer_turn   
    global your_turn
    if clicked6 != True and your_turn==True and game_over==False:
        grid_6.config(image=your_image)
        clicked6 = True
        your_turn=False
        computer_turn=True
        count+=1
        onclc()
        Thread(target=check_win).start()
def set_image7():
    global clicked7,count,computer_turn
    global your_turn
    if clicked7 != True and your_turn==True and game_over==False:
        grid_7.config(image=your_image)
        clicked7 = True
        your_turn=False
        computer_turn=True
        count+=1
        onclc()
        Thread(target=check_win).start()
def set_image8():
    global clicked8,count,computer_turn
    global your_turn
    if clicked8 != True and your_turn==True and game_over==False:
        grid_8.config(image=your_image)
        clicked8 = True
        your_turn=False
        computer_turn=True
        count+=1
        onclc()
        Thread(target=check_win).start()
def set_image9():
    global clicked9,count,computer_turn
    global your_turn
    if clicked9 != True and your_turn==True and game_over==False:
        grid_9.config(image=your_image)
        clicked9 = True
        your_turn=False
        computer_turn=True
        count+=1
        onclc()
        Thread(target=check_win).start()


root = Tk()
root.geometry('685x685')
root.title("SIngle player")

bg = PhotoImage(file='chex1.png')
bg_lable = Label(root, image=bg)
bg_lable.place(x=0, y=0)

cross = PhotoImage(file='image_thumbnai1.png')
round = PhotoImage(file='image1_thumbnai1.png')
defualt = PhotoImage(file='default.png')
your_image = choice([round, cross])
if your_image == round:
    computer_image = cross
elif your_image == cross:
    computer_image = round
grid_1 = Button(root, image=defualt, command=set_image1, bd=0)
grid_1.place(x=20, y=23)
grid_2 = Button(root, image=defualt, command=set_image2, bd=0)
grid_2.place(x=255, y=23)
grid_3 = Button(root, image=defualt, command=set_image3, bd=0)
grid_3.place(x=490, y=23)
grid_4 = Button(root, image=defualt, command=set_image4, bd=0)
grid_4.place(x=20, y=255)
grid_5 = Button(root, image=defualt, command=set_image5, bd=0)
grid_5.place(x=260, y=255)
grid_6 = Button(root, image=defualt, command=set_image6, bd=0)
grid_6.place(x=490, y=255)
grid_7 = Button(root, image=defualt, command=set_image7, bd=0)
grid_7.place(x=20, y=480)
grid_8 = Button(root, image=defualt, command=set_image8, bd=0)
grid_8.place(x=260, y=480)
grid_9 = Button(root, image=defualt, command=set_image9, bd=0)
grid_9.place(x=490, y=480)
grids=[grid_1,grid_2,grid_3,grid_4,grid_5,grid_6,grid_7,grid_8,grid_9]
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
