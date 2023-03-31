from tkinter import *
from myutils import *
from numpy import random

def run(window):
    for i in range(3):
        for j in range(3):
            cell = Frame(master=window,width=100,height=100,bg=myrgb(i*100+50,j*100,50),relief='solid',borderwidth=1)
            cell.grid(row=i, column=j,padx=3,pady=3)
            for k in range(3):
                for l in range(3):
                    subcell = Frame(master=cell,width=33,height=33,bg=myrgb(i*100+20*k,j*100+20*l,50+50*k-25*l),relief='solid',borderwidth=1)
                    subcell.grid(row=k, column=l,padx=1,pady=1)
                    label = Label(master=subcell,text= str(int(random.random()*2)))
                    # f'({i},{j})'
                    label.place(x=10,y=10)
            
            
    