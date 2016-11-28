#-----------------------------#
#Team Name: MacroHard
#Members: Zhenlin Qi
#         Zheyu Shi
#         Yong Mao
#It's a demo for User Interface
#-----------------------------#
from tkinter import *

def makeFileMenu():
    File = Menubutton(mBar, text='File', underline=0)
    File.pack(side=LEFT)

    File.menu = Menu(File)

    File.menu.choices = Menu(File.menu)

    File.menu.add_command(label='OpenFile')
    File.menu.add_command(label='Exit',command=quit)

    File['menu'] = File.menu

    return File

def makeEditMenu():
    Edit = Menubutton(mBar, text='Edit', underline=0)
    Edit.pack(side=LEFT)

    Edit.menu = Menu(Edit)

    Edit.menu.choices = Menu(Edit.menu)

    Edit.menu.add_command(label='Edit a file')
    Edit.menu.add_command(label='Imput a sentence')

    Edit['menu'] = Edit.menu

    return Edit

def makeSegmentationMenu():
    Segmentation = Menubutton(mBar, text='Segmentation', underline=0)
    Segmentation.pack(side=LEFT)

    Segmentation.menu = Menu(Segmentation)

    Segmentation.menu.choices = Menu(Segmentation.menu)

    Segmentation.menu.add_command(label='Segment sentences')
    Segmentation.menu.add_command(label='Into a file')

    Segmentation['menu'] = Segmentation.menu

    return Segmentation

def makeLexiconMenu():
    Lexicon = Menubutton(mBar, text='Lexicon', underline=0)
    Lexicon.pack(side=LEFT)

    Lexicon.menu = Menu(Lexicon)

    Lexicon.menu.choices = Menu(Lexicon.menu)

    Lexicon.menu.add_command(label='Load the Lexicon')
    Lexicon.menu.add_command(label='Add a word into the Lexicon')
    Lexicon.menu.add_command(label='Modify a word in the Lexicon')
    Lexicon.menu.add_command(label='Delete a word in the Lexicon')

    Lexicon['menu'] = Lexicon.menu

    return Lexicon

def makeRuleMenu():
    Rule = Menubutton(mBar, text='Rule', underline=0)
    Rule.pack(side=LEFT)

    Rule.menu = Menu(Rule)

    Rule.menu.choices = Menu(Rule.menu)

    Rule.menu.add_command(label='Load the Rule Library')
    Rule.menu.add_command(label='Add a new Rule into the Library')
    Rule.menu.add_command(label='Modify a Rule in the Library')
    Rule.menu.add_command(label='Delete a Rule in the Library')

    Rule['menu'] = Rule.menu

    return Rule

def makeHelpMenu():
    Help = Menubutton(mBar, text='Help', underline=0)
    Help.pack(side=LEFT)

    Help.menu = Menu(Help)

    Help.menu.choices = Menu(Help.menu)

    Help.menu.add_command(label='Instructions about the system')
    Help.menu.add_command(label='Copyright information')

    Help['menu'] = Help.menu

    return Help

#### Main starts here
root = Tk()
root.geometry('600x300')

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
#mBar.tk_menuBar(Help)

root.title('Chinese Words Segmentation System')
root.iconname('')

root.mainloop()