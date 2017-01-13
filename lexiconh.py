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
import __main__
import __main2__
import segfunc
import segfunc2
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter.messagebox import *
import os

global inwin
global pbutton
global sbutton
global sbutton1
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
global label3


def Load_Lexicon():

	os.system('start ' + os.getcwd()+'\\' + 'biaozhu_dic01.txt')

def Add_Lexicon():

	def Add_it(s):
		file = open('biaozhu_dic01.txt','a')
		file.write(s)
		file.close()

		__main__.logfile.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']' + 'a word is added to lexicon' + '\n')

		showinfo(title = 'Add_it', message = 'Add it successfully!')

	AddLexicon = Tk()
	AddLexicon.title('Add lexicon')
	AddLexicon.wm_attributes('-topmost', __main__.configdata['topmostlexicon'])
	AddLexicon.iconbitmap('logo.ico')

	frame = Frame(AddLexicon)
	frame.pack(fill = X)

	text = Text(frame, width = 60, height = 5, font = ('Verdana', 12))
	text.insert(END, 'Please input like the example:\n')
	text.insert(END, '(\'翔\', \'M\')3.901790555031348e-05')
	text.grid(row = 0, column = 0)

	style = Style()
	style.map("C.TButton",
	foreground = [('pressed', 'red'), ('active', 'blue')],
	background = [('pressed', 'black'), ('active', 'white')])

	buttons = Button(frame, text = 'Add it!', style = 'C.TButton', command = lambda: Add_it(text.get(0.0,END)))
	buttons.grid(row = 1, column = 0, sticky = W)

	buttonb = Button(frame, text = 'Back', command = AddLexicon.destroy)
	buttonb.grid(row = 1, column = 0, sticky = E)

	AddLexicon.mainloop()

def updatef():

	def updating():

		dir = os.getcwd()
		os.system('start ' + dir + '\\prepare_for_seg.pyw')

	tt1 = threading.Thread(name = 'ViceThread2', target = __main2__.showupdating)
	threading.thread.append(tt1)
	tt1.start()

	tt2 = threading.Thread(name = 'ViceThread3', target = updating)
	threading.thread.append(tt2)
	tt2.start()