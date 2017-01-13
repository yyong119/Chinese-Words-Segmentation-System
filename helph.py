# -*- coding: UTF-8 -*-
#-----------------------------#
#Team Name: MacroHard
#Members: Zhenlin Qi
#         Zheyu Shi
#         Yong Mao
#All Rights Reserved
#It's a demo for CWSS
#-----------------------------#

import os
import threading
import __main__
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter.messagebox import *
from segfunc import *

def Instructions():

    help1 = Tk()
    help1.geometry('600x460')
    help1.title('Instructions')
    help1.iconbitmap('logo.ico')
    help1.wm_attributes('-topmost', __main__.configdata['topmosthelp'])

    frame = Frame(help1)
    frame.pack(fill=X)

    def cmd(command):

        os.system(command)

    def showmore():

        direction = os.getcwd()
        targetfile = '\程序说明文档.pdf'
        fulldirection = 'start ' + direction + targetfile
        __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'help file is loaded' +'\n')
        __main__.logfile.write('        location of the file: ' + direction + targetfile + '\n')
        help1.destroy()
        cmd(fulldirection)
        cmd('exit')

    context = Label(frame,
                    text = 
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

                     4、In Improve menu, the submenu is used to
                         correct the mistakes that we make when you
                         run the segment system
                         ''', font = ('Verdana', 12))

    style = Style()
    style.map("C.TButton",
    foreground = [('pressed', 'red'), ('active', 'blue')],
    background = [('pressed', 'black'), ('active', 'white')])

    context.grid(row = 0)

    mi = Button(frame, text = 'More information', style = 'C.TButton',command = showmore)
    mi.grid(row = 1)

    blank = Label(frame)
    blank.grid(row = 2)

    back = Button(frame, text = 'Back', style = 'C.TButton', command = help1.destroy)
    back.grid(row = 3)

    help1.mainloop()

def Copyright():

    help2 = Tk()
    help2.geometry('600x300')
    help2.title('Copyright')
    help2.iconbitmap('logo.ico')
    help2.wm_attributes('-topmost', __main__.configdata['topmosthelp'])

    frame = Frame(help2)
    frame.pack(fill = X)

    context = Label(frame,
                    text = 
                    '''      
                                Made by

                     Zhenlin Qi, Zheyu Shi, Yong Mao

                     https://github.com/yyong119/

                     Chinese-Words-Segmentation-System

                     Copyright © 2016 - 2016 MacroHard.

                     All Rights Reserved
                         ''', font = ('Verdana', 12))

    style = Style()
    style.map("C.TButton",
    foreground = [('pressed', 'red'), ('active', 'blue')],
    background = [('pressed', 'black'), ('active', 'white')])

    context.grid(row = 0)
    __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Copyright information is loaded' + '\n')

    back = Button(frame, text = 'Back', style = 'C.TButton',command = help2.destroy)
    back.grid(row = 1)

    help2.mainloop()

def ApplyIt(HelpImprove,s):

    if s != '\n':
        if check(s[0:len(s)-1]):
            file = open('msr.txt', 'a')
            file.write(s)
            file.close()
            __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'One improvment is made' + '\n')

            __main__.logfile.write('        '+s[0:len(s)-1] + ' is added' + '\n')
            HelpImprove.destroy()
            showinfo(title = 'Feedback', message = 'Thanks for your help')
        else:
            showinfo(title = 'Are you kidding!', message = 'Don\'t fool me, I know you\'re tricking me!')
    else:
        showinfo(title = 'Error', message = 'The text is empty')


def HelpImprove():

    HelpImprove = Tk()
    HelpImprove.title('Feedback about problems')
    HelpImprove.wm_attributes('-topmost', __main__.configdata['topmosthelp'])
    HelpImprove.iconbitmap('logo.ico')

    frame = Frame(HelpImprove)
    frame.pack(fill = X)

    text = Text(frame, width = 60, height = 5, font = ('Verdana',12))
    text.grid(row = 0, column = 0)
    text.insert(END,'''Here\'s an example:\n这是  我们  的  分词  系统\nNote: two blanks between each word''')

    style = Style()
    style.map("C.TButton",
    foreground = [('pressed', 'red'), ('active', 'blue')],
    background = [('pressed', 'black'), ('active', 'white')])

    buttons = Button(frame, text = 'Send it!', style = 'C.TButton',command = lambda: ApplyIt(HelpImprove,text.get(0.0,END)))
    buttons.grid(row = 1, column = 0, sticky = W)
    
    buttonb = Button(frame, text = 'Back', command = HelpImprove.destroy)
    buttonb.grid(row = 1, column = 0, sticky = E)

    HelpImprove.mainloop()
