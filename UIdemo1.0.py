#-----------------------------#
#It's a demo for User Interface
#Team Name: MacroHard
#Members: Zhenlin Qi
#         Zheyu Shi
#         Yong Mao
#All Rights Reserved
#It's a demo for User Interface
#-----------------------------#
from tkinter import *
from FileEditHelpButton import *
from SegmentationButton import *
from LexiconRuleButton import *

def makeFileMenu():
    File = Menubutton(mBar, text='File', underline=0)
    File.pack(side=LEFT)

    File.menu = Menu(File)

    File.menu.choices = Menu(File.menu)

    File.menu.add_command(label='OpenFile',command=Open_File())
    File.menu.add_command(label='Exit',command=Quit())

    File['menu'] = File.menu

    return File

def makeEditMenu():
    Edit = Menubutton(mBar, text='Edit', underline=0)
    Edit.pack(side=LEFT)

    Edit.menu = Menu(Edit)

    Edit.menu.choices = Menu(Edit.menu)

    Edit.menu.add_command(label='Edit a file',command=Edit_a_File())
    Edit.menu.add_command(label='Input a sentence',command=Input_a_Sentence())

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
    Help = Menubutton(mBar, text='Help', underline=0)
    Help.pack(side=LEFT)

    Help.menu = Menu(Help)

    Help.menu.choices = Menu(Help.menu)

    Help.menu.add_command(label='Instructions about the system',command=Instructions())
    Help.menu.add_command(label='Copyright information',command=Copyright())

    Help['menu'] = Help.menu

    return Help

#### Main starts here
root = Tk()
root.geometry('1366x768')

mBar = Frame(root)
mBar.pack(fill=X)

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

# im=PhotoImage(file='test.gif')
# label(root,text='abc',image=im).pack(side='LEFT')

root.title('Chinese Words Segmentation System')
root.iconname('')

root.mainloop()
