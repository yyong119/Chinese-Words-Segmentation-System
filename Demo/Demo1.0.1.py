# -*- coding: UTF-8 -*-
#-----------------------------#
#It's a demo for User Interface
#Team Name: MacroHard
#Members: Zhenlin Qi
#         Zheyu Shi
#         Yong Mao
#All Rights Reserved
#It's a demo for User Interface
#-----------------------------#
import pickle
from tkinter import *
from FileEditHelpButton import *
from SegmentationButton import *
from LexiconRuleButton import *

def seg(sentense):
    in_pkl_file = open('matrix.pkl', 'rb')
    transition_matrix = pickle.load(in_pkl_file)
    confusion_matrix = pickle.load(in_pkl_file)
    in_pkl_file.close()
    #pi maybe more accurate if use 'B'/all and 'S'/all
    pi = {'B':0.5,'E':0,'M':0,'S':0.5}
    delta = dict()

    length = len(sentense)
    sentense = ' '+sentense

    max_pr_list = []
    max_pr = 0
    forward_pointer = dict()
    for i in 'BMES':
        delta[(1,i)] = pi[i]*confusion_matrix[(i,sentense[1])]
        if delta[(1,i)] > max_pr:
            max_pr = delta[(1,i)]

    for i in range(2,length+1):

        for j in 'BMES':
            max_pr = 0
            forward = ''
            for k in 'BMES':
                prob = delta[(i-1,k)]*transition_matrix[(k,j)]*confusion_matrix[(j,sentense[i])] # confusion_matrix is not necessary when comparing
                if prob > max_pr:
                    max_pr = prob
                    forward = k
            delta[(i,j)] = max_pr
            forward_pointer[(i,j)] = forward
    max = 0
    last_tag = ''
    for i in 'ES':
        if delta[(length,i)] > max:
            max = delta[(length,i)]
            last_tag = i
    tags = last_tag
    t = length
    while t>=2:
        last_tag = forward_pointer[(t,last_tag)]
        t -= 1
        tags = last_tag + tags

    # for i in range(len(tags)):
    #     product.insert(END,sentense[i+1],tags[i])

    seged_sentense = ''
    for i in range(len(tags)):
        if tags[i] in 'BM':
            seged_sentense += sentense[i+1]
        else:
            seged_sentense += sentense[i+1] + ' '
    product.insert(END,seged_sentense)

def makeFileMenu():
    File = Menubutton(mBar, text='File', underline=0)
    File.pack(side=LEFT)

    File.menu = Menu(File)

    File.menu.choices = Menu(File.menu)

    File.menu.add_command(label='OpenFile',command=Open_File())
    File.menu.add_command(label='Exit',command=quit)

    File['menu'] = File.menu

    return File

def makeEditMenu():
    def Input_a_Sentence():
        def toproduct():
            product.delete(0.0,END)
            sentence=inwin.get(0.0,END)
            sentence.strip()
            sentense=sentence[0:len(sentence)-1]
            in_pkl_file = open('matrix.pkl', 'rb')
            transition_matrix = pickle.load(in_pkl_file)
            confusion_matrix = pickle.load(in_pkl_file)
            in_pkl_file.close()
            pi = {'B':0.5,'E':0,'M':0,'S':0.5}
            delta = dict()

            length = len(sentense)
            sentense = ' '+sentense

            max_pr_list = []
            max_pr = 0
            forward_pointer = dict()
            for i in 'BMES':
                delta[(1,i)] = pi[i]*confusion_matrix[(i,sentense[1])]
                if delta[(1,i)] > max_pr:
                    max_pr = delta[(1,i)]

            for i in range(2,length+1):

                for j in 'BMES':
                    max_pr = 0
                    forward = ''
                    for k in 'BMES':
                        prob = delta[(i-1,k)]*transition_matrix[(k,j)]*confusion_matrix[(j,sentense[i])]
                        if prob > max_pr:
                            max_pr = prob
                            forward = k
                    delta[(i,j)] = max_pr
                    forward_pointer[(i,j)] = forward
            max = 0
            last_tag = ''
            for i in 'ES':
                if delta[(length,i)] > max:
                    max = delta[(length,i)]
                    last_tag = i
            tags = last_tag
            t = length
            while t>=2:
                last_tag = forward_pointer[(t,last_tag)]
                t -= 1
                tags = last_tag + tags
            seged_sentense = ''
            for i in range(len(tags)):
                if tags[i] in 'BM':
                    seged_sentense += sentense[i+1]
                else:
                    seged_sentense += sentense[i+1] + ' '
            product.insert(END,seged_sentense)
        inwin=Text(nBar,width=25,height=5,font=('Verdana',15))
        inwin.grid(row=1,column=1)
        product=Text(nBar,width=25,height=5,font =('Verdana',15))
        sbutton=Button(nBar,text='Segment the sentence==>',width=40,height=8,command=toproduct)
        sbutton.grid(row=1,column=2)
        product.grid(row=1,column=3,columnspan=5)
    Edit = Menubutton(mBar, text='Edit', underline=0)
    Edit.pack(side=LEFT)

    Edit.menu = Menu(Edit)

    Edit.menu.choices = Menu(Edit.menu)

    Edit.menu.add_command(label='Edit a file',command=Edit_a_File())
    Edit.menu.add_command(label='Input a sentence',command=Input_a_Sentence)

    Edit['menu'] = Edit.menu

    return Edit

def makeSegmentationMenu():
    Segmentation = Menubutton(mBar, text='Segmentation', underline=0)
    Segmentation.pack(side=LEFT)

    Segmentation.menu = Menu(Segmentation)

    Segmentation.menu.choices = Menu(Segmentation.menu)

    Segmentation.menu.add_command(label='Segment sentences',command=Segment_Sentences())
    Segmentation.menu.add_command(label='Into a file',command=Into_a_File())

    Segmentation['menu'] = Segmentation.menu

    return Segmentation

def makeLexiconMenu():
    Lexicon = Menubutton(mBar, text='Lexicon', underline=0)
    Lexicon.pack(side=LEFT)

    Lexicon.menu = Menu(Lexicon)

    Lexicon.menu.choices = Menu(Lexicon.menu)

    Lexicon.menu.add_command(label='Load the Lexicon',command=Load_Lexicon())
    Lexicon.menu.add_command(label='Add a new word into the Lexicon',command=Add_Lexicon())
    Lexicon.menu.add_command(label='Modify a word in the Lexicon',command=Modify_Lexicon())
    Lexicon.menu.add_command(label='Delete a word in the Lexicon',command=Delete_Lexicon())

    Lexicon['menu'] = Lexicon.menu

    return Lexicon

def makeRuleMenu():
    Rule = Menubutton(mBar, text='Rule', underline=0)
    Rule.pack(side=LEFT)

    Rule.menu = Menu(Rule)

    Rule.menu.choices = Menu(Rule.menu)

    Rule.menu.add_command(label='Load the Rule Library',command=Load_Rule())
    Rule.menu.add_command(label='Add a new Rule into the Library',command=Add_Rule())
    Rule.menu.add_command(label='Modify a Rule in the Library',command=Modify_Rule())
    Rule.menu.add_command(label='Delete a Rule in the Library',command=Delete_Rule())

    Rule['menu'] = Rule.menu

    return Rule

def makeHelpMenu():
    def Instructions():
        help1=Tk()
        help1.geometry('500x300')
        frame=Frame(help1)
        frame.pack(fill=X)
        context=Label(frame,
            text=
'''Instrcutions Here:
   Chinese word segmentation system made by
   Zhenlin Qi, Zheyu Shi, Yong Mao
            ''',width=50,height=20,font=(16))
        context.pack()
        help1.mainloop()

    def Copyright():
        help2=Tk()
        help2.geometry('500x300')
        frame=Frame(help2)
        frame.pack(fill=X)
        context=Label(frame,
            text=
'''Made by
   Zhenlin Qi, Zheyu Shi, Yong Mao
   Team Macrohard
   All Rights Reserved
            ''',width=50,height=20,font=(16))
        context.pack(side=LEFT)
        help2.mainloop()

    Help = Menubutton(mBar, text='Help', underline=0)
    Help.pack(side=LEFT)

    Help.menu = Menu(Help)

    Help.menu.choices = Menu(Help.menu)

    Help.menu.add_command(label='Instructions about the system',command=Instructions)
    Help.menu.add_command(label='Copyright information',command=Copyright)

    Help['menu'] = Help.menu

    return Help

#### Main starts here
root = Tk()
root.geometry('1000x500')

mBar = Frame(root)
mBar.pack(fill=X)
nBar=Frame(root)
nBar.pack(fill=X)

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

label1=Label(nBar,text='戚振林大佬是组长',width=25,height=5,font=('Verdana',15))
label1.grid(row=2,column=1)
label2=Label(nBar,text='2楼留给石大佬',width=25,height=5,font=('Verdana',15))
label2.grid(row=2,column=2)
label3=Label(nBar,text='我是渣渣，火钳留名',width=25,height=5,font=('Verdana',15))
label3.grid(row=2,column=3)

# photo = PhotoImage(file='dog.gif')
# label = Label(image=photo)
# label.image = photo
# label.grid(row=2, column=10, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

root.title('Chinese Words Segmentation System')
root.iconname('')

root.mainloop()
