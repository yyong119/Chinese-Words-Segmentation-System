# -*- coding: UTF-8 -*-
#-----------------------------#
#It's a demo for User Interface
#Team Name: MacroHard
#Members: Zhenlin Qi
#         Zheyu Shi
#         Yong Mao
#All Rights Reserved
#It's a demo for CWSS
#-----------------------------#

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
from edith import *

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

root = Tk()
root.wm_attributes('-alpha',0.85)
root.wm_attributes('-topmost',1)

canvas=Canvas(root,width=1500,height=400,bg='red')
im=PhotoImage(file='hackathon.png')
canvas.create_image(1000,300,image=im)
canvas.pack(side=BOTTOM)

mBar = Frame(root)
mBar.pack(fill=X)
nBar=Frame(root)
nBar.pack(fill=X)

def makeFileMenu():
    global sentencelist
    sentencelist=['']
    sentences=['']*100

    File = Menubutton(mBar, text='File')
    File.pack(side=LEFT)

    File.menu = Menu(File)

    File.menu.choices = Menu(File.menu)

    File.menu.add_command(label='OpenFile',command=lambda:Open_File(root,nBar,sentences,sentencelist))
    File.menu.add_command(label='Exit',command=quit)

    File['menu'] = File.menu

    return File

def makeEditMenu():
    global sentencelist
    sentencelist=['']
    sentences=['']*100

    Edit = Menubutton(mBar, text='Edit')
    Edit.pack(side=LEFT)

    Edit.menu = Menu(Edit)

    Edit.menu.choices = Menu(Edit.menu)

    Edit.menu.add_command(label='Edit a file',command=lambda: Edit_a_File(root,nBar))
    Edit.menu.add_command(label='Input sentences',command=lambda: Input_a_Sentence(root,nBar,sentences,sentencelist))

    Edit['menu'] = Edit.menu

    return Edit

def makeSegmentationMenu():
    def Segment_Sentences():
        return
    def Into_a_File():
        return
    Segmentation = Menubutton(mBar, text='Segmentation')
    Segmentation.pack(side=LEFT)

    Segmentation.menu = Menu(Segmentation)

    Segmentation.menu.choices = Menu(Segmentation.menu)

    Segmentation.menu.add_command(label='Segment sentences',command=Segment_Sentences)
    Segmentation.menu.add_command(label='Into a file',command=Into_a_File)

    Segmentation['menu'] = Segmentation.menu

    return Segmentation

def makeLexiconMenu():

    def Load_Lexicon():
        return

    def Add_Lexicon():
        return

    def Modify_Lexicon():
        return

    def Delete_Lexicon():
        return

    Lexicon = Menubutton(mBar, text='Lexicon')
    Lexicon.pack(side=LEFT)

    Lexicon.menu = Menu(Lexicon)

    Lexicon.menu.choices = Menu(Lexicon.menu)

    Lexicon.menu.add_command(label='Load the Lexicon',command=Load_Lexicon)
    Lexicon.menu.add_command(label='Add a new word into the Lexicon',command=Add_Lexicon)
    Lexicon.menu.add_command(label='Modify a word in the Lexicon',command=Modify_Lexicon)
    Lexicon.menu.add_command(label='Delete a word in the Lexicon',command=Delete_Lexicon)

    Lexicon['menu'] = Lexicon.menu

    return Lexicon

def makeRuleMenu():

    def Load_Rule():
        return

    def Add_Rule():
        return

    def Modify_Rule():
        return

    def Delete_Rule():
        return

    Rule = Menubutton(mBar, text='Rule')
    Rule.pack(side=LEFT)

    Rule.menu = Menu(Rule)

    Rule.menu.choices = Menu(Rule.menu)

    Rule.menu.add_command(label='Load the Rule Library',command=Load_Rule)
    Rule.menu.add_command(label='Add a new Rule into the Library',command=Add_Rule)
    Rule.menu.add_command(label='Modify a Rule in the Library',command=Modify_Rule)
    Rule.menu.add_command(label='Delete a Rule in the Library',command=Delete_Rule)

    Rule['menu'] = Rule.menu

    return Rule

def makeHelpMenu():
    Help = Menubutton(mBar, text='Help')
    Help.pack(side=LEFT)

    Help.menu = Menu(Help)

    Help.menu.choices = Menu(Help.menu)

    Help.menu.add_command(label='Instructions about the system',command=Instructions)
    Help.menu.add_command(label='Copyright information',command=Copyright)

    Help['menu'] = Help.menu

    return Help

def main():
    File = makeFileMenu()
    mBar.tk_menuBar(File)

    Edit = makeEditMenu()
    mBar.tk_menuBar(Edit)

    Segmentation=makeSegmentationMenu()
    mBar.tk_menuBar(Segmentation)

    Lexicon=makeLexiconMenu()
    mBar.tk_menuBar(Lexicon)

    Rule=makeRuleMenu()
    mBar.tk_menuBar(Rule)

    Help=makeHelpMenu()
    mBar.tk_menuBar(Help)

    label1=Label(nBar,text='')
    label1.grid(row=10,column=1)
    label2=Label(nBar,text='')
    label2.grid(row=10,column=2)
    label3=Label(nBar,text='')
    label3.grid(row=10,column=3)

    # photo = PhotoImage(file='hackathon.png')
    # label = Label(image=photo)
    # label.image = photo
    # label.pack(fill=BOTH)
    root.geometry('1500x1000')
    root.title(''.join(jieba.cut('Chinese Word Segmentation System')))
    root.iconname('')
    root.resizable(False,False)
    root.mainloop()

main()
