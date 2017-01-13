# -*- coding: UTF-8 -*-
#-----------------------------#
#Team Name: MacroHard
#Members: Zhenlin Qi
#         Zheyu Shi
#         Yong Mao
#All Rights Reserved
#It's a demo for CWSS
#-----------------------------#

import fileh
import edith
import __main__
import time
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter.messagebox import *

def deletemodule():

	try:
		edith.save.grid_forget()
	except:
		pass
	try:
		edith.back.grid_forget()
	except:
		pass
	try:
		edith.inwin.grid_forget()
	except:
		pass
	try:
		edith.inwin.delete(0.0, END)
	except:
		pass
	try:
		edith.pbutton.grid_forget()
	except:
		pass
	try:
		edith.sbutton.grid_forget()
	except:
		pass
	try:
		edith.sbutton1.grid_forget()
	except:
		pass
	try:
		edith.sbutton2.grid_forget()
	except:
		pass
	try:
		edith.product.grid_forget()
	except:
		pass
	try:
		edith.product.delete(0.0, END)
	except:
		pass
	try:
		edith.back.grid_forget()
	except:
		pass
	try:
		edith.fbutton.grid_forget()
	except:
		pass
	try:
		edith.fbutton2.grid_forget()
	except:
		pass
	try:
		edith.sl.grid_forget()
	except:
		pass
	try:
		edith.sl2.grid_forget()
	except:
		pass
	try:
		edith.sl3.grid_forget()
	except:
		pass
	try:
		edith.lb.grid_forget()
	except:
		pass
	try:
		edith.lb.delete(0, END)
	except:
		pass
	try:
		edith.Undo.grid_forget()
	except:
		pass
	try:
		edith.dsbutton.grid_forget()
	except:
		pass
	try:
		edith.dsbutton1.grid_forget()
	except:
		pass
	try:
		edith.dsbutton2.grid_forget()
	except:
		pass

	try:
		fileh.save.grid_forget()
	except:
		pass
	try:
		fileh.back.grid_forget()
	except:
		pass
	try:
		fileh.inwin.grid_forget()
	except:
		pass
	try:
		fileh.inwin.delete(0.0, END)
	except:
		pass
	try:
		fileh.pbutton.grid_forget()
	except:
		pass
	try:
		fileh.sbutton.grid_forget()
	except:
		pass
	try:
		fileh.sbutton1.grid_forget()
	except:
		pass
	try:
		fileh.sbutton2.grid_forget()
	except:
		pass
	try:
		fileh.product.grid_forget()
	except:
		pass
	try:
		fileh.product.delete(0.0, END)
	except:
		pass
	try:
		fileh.back.grid_forget()
	except:
		pass
	try:
		fileh.fbutton.grid_forget()
	except:
		pass
	try:
		fileh.fbutton2.grid_forget()
	except:
		pass
	try:
		fileh.sl.grid_forget()
	except:
		pass
	try:
		fileh.sl2.grid_forget()
	except:
		pass
	try:
		fileh.sl3.grid_forget()
	except:
		pass
	try:
		fileh.lb.grid_forget()
	except:
		pass
	try:
		fileh.lb.delete(0, END)
	except:
		pass
	try:
		fileh.Undo.grid_forget()
	except:
		pass
	try:
		fileh.dsbutton.grid_forget()
	except:
		pass
	try:
		fileh.dsbutton1.grid_forget()
	except:
		pass
	try:
		fileh.dsbutton2.grid_forget()
	except:
		pass

def UpAndDown(iff = 1):

	if iff == 1:
        # for i in range(12):
        #     __main__.imlist[i] = PhotoImage(file = str(40*(i+1)) + '.png')
        #     __main__.labellist[i] = Label(__main__.nnBar, image = __main__.imlist[i])
        #     __main__.nnBar.update_idletasks()
        #     __main__.labellist[i].grid(row = 1, column = 0)
		for i in range(12):
			__main__.labellist[11-i].grid_forget()
			# time.sleep(0.01*i)
			__main__.nnBar.update_idletasks()

	if iff == 2:
		for i in range(12):
			# __main__.imlist[i] = PhotoImage(file = str(40*(i+1)) + '.png')
			# __main__.labellist[i] = Label(__main__.nnBar, image = __main__.imlist[i])
			__main__.nnBar.update_idletasks()
			# time.sleep(0.01*i)
			__main__.labellist[i].grid(row = 1, column = 0)

def mix(iff = 1, ifback = False):

	UpAndDown(iff)
	deletemodule()

	if ifback:
		__main__.state = 'main'
