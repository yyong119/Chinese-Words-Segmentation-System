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
import jieba
from string import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from tkinter.messagebox import *

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

def seg(sentense):
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
    return seged_sentense

def makeFileMenu():
    global sentencelist
    sentences=['']*100
    def Open_File():
        filedir=askopenfilename()
        file=open(filedir,'r')
        data=file.readlines()
        file.close()
        def takeapart():
            global sentencelist
            sentence=inwin.get(0.0,END)
            sentencelist=sentence.split('，')
            lb.delete(0,END)
            for item in sentencelist:
                lb.insert(END,item)
        def toproduct():
            global sentencelist
            product.delete(0.0,END)
            for i in range(len(sentencelist)):
                if lb.selection_includes(i):
                    sentences[i]=sentencelist[i].replace('\n','')
                    if sentences[i]!='':
                        product.insert(END,'  第'+str(i+1)+'句：'+seg(sentences[i]))
        def toproduct2():
            global sentencelist
            product.delete(0.0,END)
            for i in range(len(sentencelist)):
                if lb.selection_includes(i):
                    sentences[i]=sentencelist[i].replace('\n','')
                    if sentences[i]!='':
                        product.insert(END,'  第'+str(i+1)+'句：'+" ".join(jieba.cut(sentences[i])))

        def tofile():
            filedir=askopenfilename()
            file=open(filedir,'w')
            toproduct()
            file.write(product.get(0.0,END))
            file.close()
            showinfo(title='Chinese Words Segment System',message='File has been saved successfully!')
        def deletemodule():
            inwin.grid_forget()
            pbutton.grid_forget()
            sbutton.grid_forget()
            sbutton2.grid_forget()
            product.grid_forget()
            back.grid_forget()
            fbutton.grid_forget()
            sl.grid_forget()
            sl2.grid_forget()
            sl3.grid_forget()
            lb.grid_forget()
        inwin=Text(nBar)
        inwin.grid(row=1,column=1)
        inwin.insert(END,data[0])

        sl = Scrollbar(nBar,orient = VERTICAL)
        sl.set(0.5,1)
        sl.grid(row=1,column=2,sticky=NS)
        inwin.configure(yscrollcommand=sl.set)
        sl.configure(command=inwin.yview)

        product=Text(nBar)
        product.grid(row=1,column=5)

        pbutton=Button(nBar,text='take apart the sentences',command=takeapart)
        pbutton.grid(row=3,column=1)

        blank1=Label(nBar)
        blank1.grid(row=2,column=3)

        sbutton=Button(nBar,text='Segment the sentence==>',command=toproduct)
        sbutton.grid(row=3,column=3)

        sbutton2=Button(nBar,text='Segment Pro==>',command=toproduct2)
        sbutton2.grid(row=4,column=3)

        blank2=Label(nBar)
        blank2.grid(row=2,column=3)

        fbutton=Button(nBar,text='Segment and save into file',command=tofile)
        fbutton.grid(row=5,column=3)

        blank3=Label(nBar,text='     ')
        blank3.grid(row=4,column=2,sticky=NS)

        sl2 = Scrollbar(nBar,orient = VERTICAL)
        sl2.set(0.5,1)
        sl2.grid(row=1,column=6,sticky=NS)       
        product.configure(yscrollcommand=sl2.set)
        sl2.configure(command=product.yview)

        back=Button(nBar,text='Back',command=deletemodule)
        back.grid(row=3,column=5)

        lb=Listbox(nBar,selectmode=MULTIPLE)
        lb.grid(row=1,column=3,sticky=NS)

        sl3 = Scrollbar(nBar,orient = HORIZONTAL)
        sl3.set(0.5,1)
        sl3.grid(row=2,column=3,sticky=EW)
        lb.configure(yscrollcommand=sl3.set)
        sl3.configure(command=lb.xview)

    File = Menubutton(mBar, text='File')
    File.pack(side=LEFT)

    File.menu = Menu(File)

    File.menu.choices = Menu(File.menu)

    File.menu.add_command(label='OpenFile',command=Open_File)
    File.menu.add_command(label='Exit',command=quit)

    File['menu'] = File.menu

    return File

def makeEditMenu():
    global sentencelist
    sentences=['']*100
    def Edit_a_File():
        filedir=askopenfilename()
        filer=open(filedir,'r')
        data=filer.readlines()
        filer.close()
        def savefile():
            filew=open(filedir,'w')
            filew.write(inwin.get(0.0,END))
            filew.close()
            showinfo(title='Chinese Words Segment System',message='File has been saved successfully!')
        def deletemodule():
            inwin.grid_forget()
            save.grid_forget()
            back.grid_forget()
        inwin=Text(nBar)
        inwin.grid(row=1,column=1,sticky=W)
        if type(data)==list:
            inwin.insert(END,data[0])
        save=Button(nBar,text='Save',command=savefile)
        save.grid(row=1,column=2,sticky=W)
        back=Button(nBar,text='Back',command=deletemodule)
        back.grid(row=2,column=2,sticky=W)
    def Input_a_Sentence():
        def takeapart():
            global sentencelist
            sentence=inwin.get(0.0,END)
            sentencelist=sentence.split('，')
            lb.delete(0,END)
            for item in sentencelist:
                lb.insert(END,item)
        def toproduct():
            product.delete(0.0,END)
            global sentencelist
            for i in range(len(sentencelist)):
                if lb.selection_includes(i):
                    sentences[i]=sentencelist[i].replace('\n','')
                    if sentences[i]!='':
                        product.insert(END,'  第'+str(i+1)+'句：'+seg(sentences[i]))
        def toproduct2():
            global sentencelist
            product.delete(0.0,END)
            for i in range(len(sentencelist)):
                if lb.selection_includes(i):
                    sentences[i]=sentencelist[i].replace('\n','')
                    if sentences[i]!='':
                        product.insert(END,'  第'+str(i+1)+'句：'+" ".join(jieba.cut(sentences[i])))
        def tofile():
            filedir=askopenfilename()
            file=open(filedir,'w')
            toproduct()
            file.write(product.get(0.0,END))
            file.close()
            showinfo(title='Chinese Words Segment System',message='File has been saved successfully!')
        def deletemodule():
            inwin.grid_forget()
            pbutton.grid_forget()
            sbutton.grid_forget()
            sbutton2.grid_forget()
            product.grid_forget()
            back.grid_forget()
            fbutton.grid_forget()
            sl.grid_forget()
            sl2.grid_forget()
            sl3.grid_forget()
            lb.grid_forget()
        inwin=Text(nBar)
        inwin.grid(row=1,column=1)

        sl = Scrollbar(nBar,orient = VERTICAL)
        sl.set(0.5,1)
        sl.grid(row=1,column=2,sticky=NS)
        inwin.configure(yscrollcommand=sl.set)
        sl.configure(command=inwin.yview)

        product=Text(nBar)
        product.grid(row=1,column=5)

        pbutton=Button(nBar,text='take apart the sentences',command=takeapart)
        pbutton.grid(row=3,column=1)

        blank1=Label(nBar)
        blank1.grid(row=2,column=3)

        sbutton=Button(nBar,text='Segment the sentence==>',command=toproduct)
        sbutton.grid(row=3,column=3)

        sbutton2=Button(nBar,text='Segment Pro==>',command=toproduct2)
        sbutton2.grid(row=4,column=3)

        blank2=Label(nBar)
        blank2.grid(row=2,column=3)

        fbutton=Button(nBar,text='Segment and save into file',command=tofile)
        fbutton.grid(row=5,column=3)

        blank3=Label(nBar,text='     ')
        blank3.grid(row=4,column=2,sticky=NS)

        sl2 = Scrollbar(nBar,orient = VERTICAL)
        sl2.set(0.5,1)
        sl2.grid(row=1,column=6,sticky=NS)       
        product.configure(yscrollcommand=sl2.set)
        sl2.configure(command=product.yview)

        back=Button(nBar,text='Back',command=deletemodule)
        back.grid(row=3,column=5)

        lb=Listbox(nBar,selectmode=MULTIPLE)
        lb.grid(row=1,column=3,sticky=NS)

        sl3 = Scrollbar(nBar,orient = HORIZONTAL)
        sl3.set(0.5,1)
        sl3.grid(row=2,column=3,sticky=EW)
        lb.configure(yscrollcommand=sl3.set)
        sl3.configure(command=lb.xview)
    Edit = Menubutton(mBar, text='Edit')
    Edit.pack(side=LEFT)

    Edit.menu = Menu(Edit)

    Edit.menu.choices = Menu(Edit.menu)

    Edit.menu.add_command(label='Edit a file',command=Edit_a_File)
    Edit.menu.add_command(label='Input a sentence',command=Input_a_Sentence)

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

    def Instructions():
        help1=Tk()
        help1.geometry('600x400')
        help1.title('Instructions')
        frame=Frame(help1)
        frame.pack(fill=X)
        context=Label(frame,
            text=
     '''Instrcutions Here:
        Chinese word segmentation system made by
        Zhenlin Qi, Zheyu Shi, Yong Mao
            ''',font=('Verdana',12,'bold'))
        context.grid(row=0)
        back=Button(frame,text='Back',command=help1.destroy)
        back.grid(row=1)
        help1.mainloop()

    def Copyright():
        help2=Tk()
        help2.geometry('600x300')
        help2.title('Copyright')
        frame=Frame(help2)
        frame.pack(fill=X)
        context=Label(frame,
            text=
     '''Made by
        Zhenlin Qi, Zheyu Shi, Yong Mao
        https://github.com/yyong119/
        Chinese-Words-Segmentation-System
        Copyright © 2016 - 2016 MacroHard. 
        All Rights Reserved
            ''',font=('Verdana',12,'bold'))
        context.grid(row=0)
        back=Button(frame,text='Back',command=help2.destroy)
        back.grid(row=1)
        help2.mainloop()

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