from tkinter import*
from tkinter.ttk import *

def Instructions():
    help1 = Tk()
    help1.geometry('600x400')
    help1.title('Instructions')
    help1.wm_attributes('-topmost', 1)
    frame = Frame(help1)
    frame.pack(fill=X)
    context = Label(frame,
                    text=
                    '''                        Instrcutions Here:
                     Chinese word segmentation system made by
                     Zhenlin Qi, Zheyu Shi, Yong Mao
                     1、In File menu, there're two submenus,
                         the first is used to open a local file
                         the second is to quit the software.
                     2、In Edit menu, there're two submenus,
                         the first is used to edit a local file
                         the second is to input sentences by hand.
                     3、In Help menu, there're two submenus,
                         the first is used to show instructions
                         the second is to show copyright.
                         ''', font=('Verdana', 12))
    context.grid(row=0)
    back = Button(frame, text='Back', command=help1.destroy)
    back.grid(row=1)
    help1.mainloop()

def Copyright():
    help2 = Tk()
    help2.geometry('600x400')
    help2.title('Copyright')
    help2.wm_attributes('-topmost', 1)
    frame = Frame(help2)
    frame.pack(fill=X)
    context = Label(frame,
                    text=
                    '''                        Made by
                     Zhenlin Qi, Zheyu Shi, Yong Mao
                     https://github.com/yyong119/
                     Chinese-Words-Segmentation-System
                     Copyright © 2016 - 2016 MacroHard.
                     All Rights Reserved
                         ''', font=('Verdana', 12, 'bold'))
    context.grid(row=0)
    back = Button(frame, text='Back', command=help2.destroy)
    back.grid(row=1)
    help2.mainloop()
