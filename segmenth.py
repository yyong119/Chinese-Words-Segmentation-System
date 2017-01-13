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
import re
import __main__
import segfunc
from tkinter.filedialog import *
from tkinter.messagebox import *

def getnewdir(filedir):

	temp = filedir.split('.')
	cr = ''
	for i in range(len(temp)-2):
		cr = cr + temp[i] + '.'
	cr = cr + temp[len(temp)-2]
	cr = cr + '-result.' + temp[len(temp)-1]
	return cr

def Segment_Sentences():

	filedir = askopenfilename()
	file = open(filedir,'r')
	data = file.read()
	file.close()

	datalist = data.split()

	newfiledir = getnewdir(filedir)
	resultfile = open(newfiledir,'w')
	resultfile.write('Here\'s the result:\n')
	try:
		for i in range(len(datalist)):
			if datalist[i] != '':
				resultfile.write(segfunc.seg(datalist[i])+'\n')

		showinfo(title = 'Save file', message = 'The result has been saved into the target file!')
	except:
		showinfo(title = 'Error', message = 'There\'re illegal characters in the text!')
		__main__.logfile.write('Error: Illegal characters occur in the text to be segmented!' + '\n')

	resultfile.close()

def Segment_Sentences2():

	filedir = askopenfilename()
	file = open(filedir,'r')
	data = file.read()
	file.close()

	datalist = data.split('\n')

	resultfile = open(filedir,'w')
	resultfile.write('Here\'s the result:\n')

	try:
		for i in range(len(datalist)):
			sentencelist = re.split('[，。：“”！？]', datalist[i])
			for j in range(len(sentencelist)):
				resultfile.write(segfunc.seg(sentencelist[j])+'\n')

		showinfo(title = 'Save the result', message = 'The result has covered the text!')
	except:
		showinfo(title = 'Error', message = 'There\'re illegal characters in the text!')
		__main__.logfile.write('Error: Illegal characters occur in the text to be segmented!' + '\n')
	resultfile.close()