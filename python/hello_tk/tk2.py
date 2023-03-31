from tkinter import *

def run(window):
    # myButton.pack()
    # myButton = Button(window, text='H e l l o', command=hello)
    # f f g g h j k kl l 
    # mytext = Text()
    # mytext.pack()
    frame_style = {
        ' s u n k e n ': SUNKEN,
        ' f l a t ': FLAT,
        ' r i d g e ': RIDGE,
        ' g r o o v e ': GROOVE,
        ' r a i s e d ': RAISED
    }

    colours = ['red', 'green', 'blue', 'yellow', 'purple']
    i = 0
    for relief_style, reliefs in frame_style.items():
        frame = Frame(master=window, 
                      width=200, height=100, background=colours[i])
        i += 1
        frame.pack(fill=BOTH,side = LEFT)
        label = Label(master=frame, text=relief_style)
        # label.pack()

