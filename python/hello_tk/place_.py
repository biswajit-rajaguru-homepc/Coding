
from tkinter import *

def run(window):
    frame = Frame(master=window,width=400,height=400,background='#003040')
    frame.pack()
    l1= Label(master=frame,text="I am at 0,0",fg='#00ff00',bg='#0030f0',borderwidth=1)
    l1.place(x=100,y=100)
    
    
    
    