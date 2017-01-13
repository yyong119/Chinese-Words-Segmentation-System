# -*- coding: UTF-8 -*-
#-----------------------------#
#Team Name: MacroHard
#Members: Zhenlin Qi
#         Zheyu Shi
#         Yong Mao
#All Rights Reserved
#It's a demo for CWSS
#-----------------------------#

import threading
import pickle
import time
import __main2__
import segfunc
import segfunc2
from segmenth import *
from string import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter.messagebox import *
from helph import*
from fileh import *
from edith import *
from lexiconh import *
import os

state = 'main'
labellist=[0 for i in range (12)]
imlist=[0 for i in range(12)]
logfile = open('CWSS.log', 'w')
configfile = open('configuration.ini', 'r')
configdata = {}
temp = configfile.readlines()
configfile.close()
for i in range(len(temp)):
    tempc = temp[i].split('\'')
    configdata[tempc[1]] = tempc[3]

logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Loading configuration OK' + '\n')


print('CWSS starts at ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']'+ 'CWSS starts' + '\n')

root = Tk()
root.wm_attributes('-alpha', configdata['transparent'])
root.wm_attributes('-topmost', configdata['topmostmain'])

mBar = Frame(root)
mBar.pack(fill = X)

nnBar = Frame(root)
nnBar.pack(fill = X)

nBar = Frame(root)
nBar.pack(fill = X)

im = PhotoImage(file = configdata['picture1'])
label1 = Label(nnBar, image = im)
label1.grid(row = 0, column = 0) 

im2 = PhotoImage(file = configdata['picture2'])
label2 = Label(nnBar, image = im2)
label2.grid(row = 2, column = 0)

for i in range(12):
	imlist[i] = PhotoImage(file = configdata['gif'+str(i)])
	labellist[i] = Label(nnBar, image = imlist[i])
	labellist[i].grid(row = 1, column = 0)
	# nnBar.update_idletasks()

logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Loading UI OK' + '\n')

def makeFileMenu():

    global sentencelist

    sentencelist = ['']
    sentences = ['']*1000

    File = Menubutton(mBar, text = 'File')
    File.pack(side = LEFT)

    File.menu = Menu(File, tearoff = 0, bg = 'lightgreen')

    File.menu.choices = Menu(File.menu)

    File.menu.add_command(label = 'OpenFile', command = lambda:Open_File(root, nBar, sentences, sentencelist))
    File.menu.add_command(label = 'Exit', command = quit)

    File['menu'] = File.menu

    return File

def makeEditMenu():

    global sentencelist

    sentencelist = ['']
    sentences = ['']*1000

    Edit = Menubutton(mBar, text = 'Edit')
    Edit.pack(side = LEFT)

    Edit.menu = Menu(Edit, tearoff = 0, bg = 'lightblue')

    Edit.menu.choices = Menu(Edit.menu)

    Edit.menu.add_command(label = 'Edit a file', command = lambda: Edit_a_File(root, nBar))
    Edit.menu.add_command(label = 'Input sentences', command = lambda: Input_a_Sentence(root, nBar, sentences, sentencelist))

    Edit['menu'] = Edit.menu

    return Edit

def makeSegmentationMenu():

    Segmentation = Menubutton(mBar, text = 'Segmentation')
    Segmentation.pack(side = LEFT)

    Segmentation.menu = Menu(Segmentation, tearoff=0, bg='lightyellow')

    Segmentation.menu.choices = Menu(Segmentation.menu)

    Segmentation.menu.add_command(label = 'Segment and save into new file', command = Segment_Sentences)
    Segmentation.menu.add_command(label = 'Segment and replace the old file', command = Segment_Sentences2)

    Segmentation['menu'] = Segmentation.menu

    return Segmentation

def makeLexiconMenu():

	Lexicon = Menubutton(mBar, text = 'Lexicon')
	Lexicon.pack(side = LEFT)

	Lexicon.menu = Menu(Lexicon, tearoff = 0, bg = 'lightyellow')

	Lexicon.menu.choices = Menu(Lexicon.menu)

	Lexicon.menu.add_command(label = 'Load&Modify&Delete the Lexicon', command = Load_Lexicon)
	Lexicon.menu.add_command(label = 'Add a new word into the Lexicon', command = Add_Lexicon)
	Lexicon.menu.add_command(label = 'Update it', command = updatef)

	Lexicon['menu'] = Lexicon.menu

	return Lexicon

# def makeRuleMenu():

#     def Load_Rule():

#         return

#     def Add_Rule():

#         return

#     def Modify_Rule():

#         return

#     def Delete_Rule():

#         return

#     Rule = Menubutton(mBar, text='Rule')
#     Rule.pack(side=LEFT)

#     Rule.menu = Menu(Rule, tearoff=0,bg='lightyellow')

#     Rule.menu.choices = Menu(Rule.menu)

#     Rule.menu.add_command(label='Load the Rule Library',command=Load_Rule)
#     Rule.menu.add_command(label='Add a new Rule into the Library',command=Add_Rule)
#     Rule.menu.add_command(label='Modify a Rule in the Library',command=Modify_Rule)
#     Rule.menu.add_command(label='Delete a Rule in the Library',command=Delete_Rule)

#     Rule['menu'] = Rule.menu

#     return Rule

def makeHelpMenu():

    Help = Menubutton(mBar, text = 'Help')
    Help.pack(side = LEFT)

    Help.menu = Menu(Help, tearoff = 0, bg = 'lightpink')

    Help.menu.choices = Menu(Help.menu)

    Help.menu.add_command(label = 'Instructions about the system', command = Instructions)
    Help.menu.add_command(label = 'Copyright information', command = Copyright)

    Help['menu'] = Help.menu

    return Help

def makeImproveMenu():

    Improve = Menubutton(mBar, text = 'Improve')
    Improve.pack(side = LEFT)

    Improve.menu = Menu(Improve, tearoff = 0, bg = 'lightgreen')

    Improve.menu.choices = Menu(Improve.menu)

    Improve.menu.add_command(label = 'Help us imporve it', command = HelpImprove)

    Improve['menu'] = Improve.menu

    return Improve

def main():

    File = makeFileMenu()
    mBar.tk_menuBar(File)

    Edit = makeEditMenu()
    mBar.tk_menuBar(Edit)

    Segmentation = makeSegmentationMenu()
    mBar.tk_menuBar(Segmentation)

    Lexicon = makeLexiconMenu()
    mBar.tk_menuBar(Lexicon)

    # Rule = makeRuleMenu()
    # mBar.tk_menuBar(Rule)

    Help = makeHelpMenu()
    mBar.tk_menuBar(Help)

    Improve = makeImproveMenu()
    mBar.tk_menuBar(Improve)

    root.geometry(configdata['dpi'] + configdata['xe'] + configdata['ye'])
    root.title(configdata['title'])
    root.iconname('')
    root.iconbitmap('logo.ico')
    root.resizable(False,False)
    print('Now Loading matrices')
    logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'Loading matrices' + '\n')


    threading.thread=[]

    t = threading.Thread(name = 'ViceThread', target = __main2__.showw)
    threading.thread.append(t)
    t.start()

    t1 = threading.Thread(name = 'Thread2', target = segfunc2.daoru_gailv)
    threading.thread.append(t1)
    t1.start()

    t2 = threading.Thread(name = 'Thread2', target = segfunc.load)
    threading.thread.append(t2)
    t2.start()
    
    root.mainloop()
    logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'CWSS exits' + '\n')
    logfile.close()

main()