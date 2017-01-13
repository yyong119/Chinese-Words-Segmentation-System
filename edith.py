# -*- coding: UTF-8 -*-
#-----------------------------#
#Team Name: MacroHard
#Members: Zhenlin Qi
#         Zheyu Shi
#         Yong Mao
#All Rights Reserved
#It's a demo for CWSS
#-----------------------------#

import pickle
import fileh
import __main__
import modulechange
from re import *
from string import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter.messagebox import *
from helph import*
from segfunc import *
from segfunc2 import *
import time

def Edit_a_File(root, nBar):

    global save
    global back
    global inwin
    global Undo

    filedir = askopenfilename()
    filer = open(filedir, 'r')
    data = filer.readlines()
    filer.close()

    def savefile():

        filew = open(filedir, 'w')
        text_t = inwin.get(0.0, END)
        filew.write(text_t)
        filew.close()

        __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'The file is edited' + '\n')
        __main__.logfile.write('        File location ' + filedir + '\n')

        showinfo(title = 'Chinese Words Segment System', message = 'File has been saved successfully!')

    if __main__.state != 'main':
        modulechange.UpAndDown(2)
        
    __main__.nnBar.update_idletasks()
    modulechange.mix()
    __main__.state = 'edit'

    inwin = Text(nBar, undo = True, autoseparators = False, bg = 'lightyellow', width = 60,height = 14, font = ('华文新魏'))
    inwin.grid(row = 1, column = 1, sticky = W)

    data1 = ''
    for i in data:
        data1 += i
    inwin.insert(END, data1)

    def callback(event):

        global inwin
        inwin.edit_separator()

    inwin.bind("<Key>", callback)

    def Undot():

        global inwin

        x = inwin.get(1.0, END)
        if len(x) == 1:
            showinfo(title = 'Error', message = 'There\'s no letter!')
            return
        inwin.edit_undo()

    style = Style()
    style.map("C.TButton",
    foreground = [('pressed', 'red'), ('active', 'blue')],
    background = [('pressed', 'red'), ('active', 'white')])
    style.configure("C.TButton", background = 'lightgreen')

    save = Button(nBar, text = 'Save', style = 'C.TButton', command = savefile)
    save.grid(row = 1, column = 3)

    Undo = Button(nBar, text = 'Undo', style = 'C.TButton', command = Undot)
    Undo.grid(row = 1, column = 2)

    back = Button(nBar, text = 'Back', style = 'C.TButton', command = lambda: modulechange.mix(2, True))
    back.grid(row = 2, column = 2, sticky = W)


def Input_a_Sentence(root, nBar, sentences, sentencelist):

    def takeapart():

        global sentencelist

        sentence = inwin.get(0.0, END)
        sentencelist = split('[，。：“”！？]', sentence)
        lb.delete(0, END)

        for item in sentencelist:
            if item != '':
                lb.insert(END, item)

        for i in range(len(sentencelist)):
            lb.itemconfig(i, fg = "blue")
            if not i%2:
                lb.itemconfig(i, bg = "#f0f0ff")


    def toproduct():

        global sentencelist

        product.delete(0.0, END)
        for i in range(len(sentencelist)):
            if lb.selection_includes(i):
                sentences[i] = sentencelist[i].replace('\n', '')
                if sentences[i] != '':
                    product.insert(END, '第' + str(i + 1) + '句：' + seg(sentences[i]) + '\n')
        __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Shi\'s algorithm is activated' + '\n')

    def toproduct1():

        global sentencelist

        product.delete(0.0, END)
        for i in range(len(sentencelist)):
            if lb.selection_includes(i):
                sentences[i] = sentencelist[i].replace('\n', '')
                if sentences[i] != '':
                    product.insert(END, '第' + str(i + 1) + '句：' + seg2(sentences[i]) + '\n')
        __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Qi\'s algorithm is activated' + '\n')

    def dtoproduct():

        product.delete(0.0, END)
        ss=inwin.get(0.0, END).replace('\n', '')
        product.insert(END, seg(ss))
        __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Shi\'s algorithm is activated' + '\n')

    def dtoproduct1():

        product.delete(0.0, END)
        ss=inwin.get(0.0, END).replace('\n', '')
        product.insert(END, seg2(ss))
        __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Qi\'s algorithm is activated' + '\n')

    def tofile():

        targetfiledir = askopenfilename()
        targetfile = open(targetfiledir, 'w')
        toproduct()
        targetfile.write(product.get(0.0, END))
        targetfile.close()

        showinfo(title = 'Chinese Words Segment System', message = 'File has been saved successfully!')
        __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Segment result is saved into a file' + '\n')

    def tofile2():

        targetfiledir = askopenfilename()
        targetfile = open(targetfiledir, 'w')
        targetfile.write(product.get(0.0, END))
        targetfile.close()

        showinfo(title = 'Chinese Words Segment System', message = 'File has been saved successfully!')
        __main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Segment result is saved into a file' + '\n')


    global inwin
    global pbutton
    global sbutton
    global sbutton1
    global sbutton2
    global product
    global back
    global fbutton
    global fbutton2
    global sl
    global sl2
    global sl3
    global lb
    global save
    global Undo
    global dsbutton
    global dsbutton1
    global dsbutton2

    try:
        __main__.label3.grid_forget()
    except:
        pass

    if __main__.state != 'main':
        modulechange.UpAndDown(2)
    __main__.nnBar.update_idletasks()
    modulechange.mix()
    __main__.state = 'edit'

    inwin = Text(nBar, width = 35, height = 13, bg = 'lightyellow', font = ('华文新魏'))
    inwin.grid(row = 1, column = 1)

    sl = Scrollbar(nBar, orient = VERTICAL)
    sl.set(0.5, 1)
    sl.grid(row = 1, column = 2, sticky = NS)
    inwin.configure(yscrollcommand = sl.set)
    sl.configure(command = inwin.yview)

    product = Text(nBar, width = 35, height = 13, bg = 'lightpink', font = ('华文新魏'))
    product.grid(row = 1, column = 5)


    style = Style()
    style.map("C.TButton",
    foreground = [('pressed', 'red'), ('active', 'blue')],
    background = [('pressed', 'black'), ('active', 'white')])

    pbutton = Button(nBar, text = 'take apart the sentences', style = 'C.TButton', command = takeapart)
    pbutton.grid(row = 3, column = 1)

    blank1 = Label(nBar)
    blank1.grid(row = 2, column = 3)

    sbutton = Button(nBar, text = 'Segment the sentence ==>', style = 'C.TButton', command = toproduct)
    sbutton.grid(row = 3, column = 3)

    sbutton1 = Button(nBar, text = 'Segment the sentence2==>', style = 'C.TButton', command = toproduct1)
    sbutton1.grid(row = 4, column = 3)

    blank = Label(nBar)
    blank.grid(row = 2, column = 1)

    dsbutton = Button(nBar, text = 'Segment directly ==>', style = 'C.TButton', command = dtoproduct)
    dsbutton.grid(row = 4, column = 1)

    dsbutton1 = Button(nBar, text = 'Segment directly2==>', style = 'C.TButton', command = dtoproduct1)
    dsbutton1.grid(row = 5, column = 1)

    blank2 = Label(nBar)
    blank2.grid(row = 2, column = 3)

    fbutton = Button(nBar, text = 'Segment chosen sentences into file', style = 'C.TButton', command = tofile)
    fbutton.grid(row = 5, column = 3)

    blank3 = Label(nBar, text = '     ')
    blank3.grid(row = 4, column = 2, sticky = NS)

    sl2 = Scrollbar(nBar, orient = VERTICAL)
    sl2.set(0.5, 1)
    sl2.grid(row = 1, column = 6, sticky = NS)
    product.configure(yscrollcommand = sl2.set)
    sl2.configure(command = product.yview)

    fbutton2 = Button(nBar, text = 'Save result into file', style = 'C.TButton', command = tofile2)
    fbutton2.grid(row = 3, column = 5)

    back = Button(nBar, text = 'Back', style = 'C.TButton', command = lambda: modulechange.mix(2))
    back.grid(row = 4, column = 5)

    lb = Listbox(nBar, width = 30, height = 13, selectmode = MULTIPLE, bg = 'lightgreen', font = ('华文新魏'))
    lb.grid(row = 1, column = 3, sticky = NS)

    sl3 = Scrollbar(nBar, orient = HORIZONTAL)
    sl3.set(0.5, 1)
    sl3.grid(row = 2, column = 3, sticky = EW)
    lb.configure(yscrollcommand = sl3.set)
    sl3.configure(command = lb.xview)
