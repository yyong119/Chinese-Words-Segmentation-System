# -*- coding: UTF-8 -*-
#-----------------------------#
#Team Name: MacroHard
#Members: Zhenlin Qi
#         Zheyu Shi
#         Yong Mao
#All Rights Reserved
#It's a demo for CWSS
#-----------------------------#

import time
import __main__
from tkinter import *
from tkinter.messagebox import *

def showw():

	root2 = Tk()
	root2.wm_attributes('-alpha', __main__.configdata['main2transparent'])
	root2.wm_attributes('-topmost', __main__.configdata['main2topmost'])

	showinfo(title = 'Chinese Word Segmentation System',
		message = 'Welcome to Chinese Word Segmentation System made by Macrohard')
	
	root2.destroy()
	root2.mainloop()

def showupdating():

	showinfo(title = 'Update Lexicon', message = 'The Update process is running background now!')