import pickle
import jieba
from re import *
from string import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter.messagebox import *
from helph import*
from segfunc import *
from fileh import *

global inwin
global pbutton
global sbutton
global sbutton2
global product
global back
global fbutton
global sl
global sl2
global sl3
global lb
global senteces
global sentencelist
global save

def deletemodule():

    save.grid_forget()
    inwin.grid_forget()
    inwin.delete(0.0, END)
    pbutton.grid_forget()
    sbutton.grid_forget()
    sbutton2.grid_forget()
    product.grid_forget()
    product.delete(0.0, END)
    back.grid_forget()
    fbutton.grid_forget()
    sl.grid_forget()
    sl2.grid_forget()
    sl3.grid_forget()
    lb.grid_forget()
    lb.delete(0, END)

def Edit_a_File(root,nBar):

    filedir = askopenfilename()
    filer = open(filedir, 'r')
    data = filer.readlines()
    filer.close()

    def deletemodule():
        save.grid_forget()
        inwin.grid_forget()
        inwin.delete(0.0, END)
        back.grid_forget()

    def savefile():
        filew = open(filedir, 'w')
        filew.write(inwin.get(0.0, END))
        filew.close()
        showinfo(title='Chinese Words Segment System', message='File has been saved successfully!')

    inwin = Text(nBar)
    inwin.grid(row=1, column=1, sticky=W)
    if type(data) == list:
        inwin.insert(END, data[0])

    global save
    save = Button(nBar, text='Save', command=savefile)
    save.grid(row=1, column=2, sticky=W)

    back = Button(nBar, text='Back', command=deletemodule)
    back.grid(row=2, column=2, sticky=W)

def Input_a_Sentence(root,nBar,sentences,sentencelist):

    def deletemodule():

        inwin.grid_forget()
        inwin.delete(0.0, END)
        pbutton.grid_forget()
        sbutton.grid_forget()
        sbutton2.grid_forget()
        product.grid_forget()
        product.delete(0.0, END)
        back.grid_forget()
        fbutton.grid_forget()
        sl.grid_forget()
        sl2.grid_forget()
        sl3.grid_forget()
        lb.grid_forget()
        lb.delete(0, END)

    def takeapart():
        global sentencelist
        sentence = inwin.get(0.0, END)
        sentencelist = split('，', sentence)
        lb.delete(0, END)
        for item in sentencelist:
            lb.insert(END, item)

    def toproduct():
        global sentencelist
        product.delete(0.0, END)
        for i in range(len(sentencelist)):
            if lb.selection_includes(i):
                sentences[i] = sentencelist[i].replace('\n', '')
                if sentences[i] != '':
                    product.insert(END, '  第' + str(i + 1) + '句：' + seg(sentences[i]))

    def toproduct2():
        global sentencelist
        product.delete(0.0, END)
        for i in range(len(sentencelist)):
            if lb.selection_includes(i):
                sentences[i] = sentencelist[i].replace('\n', '')
                if sentences[i] != '':
                    product.insert(END, '  第' + str(i + 1) + '句：' + " ".join(jieba.cut(sentences[i])))

    def tofile():
        filedir = askopenfilename()
        file = open(filedir, 'w')
        toproduct()
        file.write(product.get(0.0, END))
        file.close()
        showinfo(title='Chinese Words Segment System', message='File has been saved successfully!')

    inwin = Text(nBar)
    inwin.grid(row=1, column=1)

    sl = Scrollbar(nBar, orient=VERTICAL)
    sl.set(0.5, 1)
    sl.grid(row=1, column=2, sticky=NS)
    inwin.configure(yscrollcommand=sl.set)
    sl.configure(command=inwin.yview)

    product = Text(nBar)
    product.grid(row=1, column=5)

    pbutton = Button(nBar, text='take apart the sentences', command=takeapart)
    pbutton.grid(row=3, column=1)

    blank1 = Label(nBar)
    blank1.grid(row=2, column=3)

    sbutton = Button(nBar, text='Segment the sentence==>', command=toproduct)
    sbutton.grid(row=3, column=3)

    sbutton2 = Button(nBar, text='Segment Pro==>', command=toproduct2)
    sbutton2.grid(row=4, column=3)

    blank2 = Label(nBar)
    blank2.grid(row=2, column=3)

    fbutton = Button(nBar, text='Segment and save into file', command=tofile)
    fbutton.grid(row=5, column=3)

    blank3 = Label(nBar, text='     ')
    blank3.grid(row=4, column=2, sticky=NS)

    sl2 = Scrollbar(nBar, orient=VERTICAL)
    sl2.set(0.5, 1)
    sl2.grid(row=1, column=6, sticky=NS)
    product.configure(yscrollcommand=sl2.set)
    sl2.configure(command=product.yview)

    back = Button(nBar, text='Back', command=deletemodule)
    back.grid(row=3, column=5)

    lb = Listbox(nBar, selectmode=MULTIPLE)
    lb.grid(row=1, column=3, sticky=NS)

    sl3 = Scrollbar(nBar, orient=HORIZONTAL)
    sl3.set(0.5, 1)
    sl3.grid(row=2, column=3, sticky=EW)
    lb.configure(yscrollcommand=sl3.set)
    sl3.configure(command=lb.xview)
