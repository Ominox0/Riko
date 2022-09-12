# Import
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from threading import Thread
import sys
try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
# Setup Variables
orange=["true","false","none","if","elif","else","while","for","in","and","or","not"]
purple=["print"]
red=["str","num","bool","list","byte"]

appName = 'Riko Editor'
nofileOpenedString = 'New File'

currentFilePath = nofileOpenedString

# Viable File Types, when opening and saving files.
fileTypes = [("Text Files","*.txt"), ("Markdown","*.md")]

# Tkinter Setup
window = Tk()

# Set the first column to occupy 100% of the width
window.grid_columnconfigure(0, weight=1)

window.title(appName + " - " + currentFilePath)

# Window Dimensions in Pixel
window.geometry('900x900')

# Handler Functions
def fileDropDownHandeler(action):
    global currentFilePath

    # Opening a File
    if action == "open":
        file = filedialog.askopenfilename(filetypes = fileTypes)

        window.title(appName + " - " + file)

        currentFilePath = file

        with open(file, 'r') as f:
            txt.delete(1.0,END)
            txt.insert(INSERT,f.read())

    # Making a new File
    elif action == "new":
        currentFilePath = nofileOpenedString
        txt.delete(1.0,END)
        window.title(appName + " - " + currentFilePath)

    # Saving a file
    elif action == "save" or action == "saveAs":
        if currentFilePath == nofileOpenedString or action== 'saveAs':
            currentFilePath = filedialog.asksaveasfilename(filetypes = fileTypes)

        with open(currentFilePath, 'w') as f:
            f.write(txt.get('1.0','end'))

        window.title(appName + " - " + currentFilePath)
def RunRk(Dir):
    import os
    os.system(f"{Dir} {currentFilePath}")
def Runs():
    from cmd import CMD
    cmd = CMD()
    cmd.AddColor("Normal",foreground="black",background="white")
    cmd.AddColor("Blue",foreground="blue",background="white")
    import os
    Rfile, name=os.path.split("D:/AAA/AAA.txt")
    Dir = os. getcwd()
    for i in range(5):
        Dir=Dir[:-1]
    Rfile =  f"{Dir}Riko.exe"
    cmd.AddText(f"Runing : {currentFilePath} from {Rfile}","Normal")
    cmd.AddText("=========================================","Blue")
    cmd.AddText("")
    Thread(target=RunRk, args=[Dir],daemon=False).start()
def RunS(action):
    if action=="RunScript":
        Thread(target=Runs,daemon=False).start()
        
def textchange(event):
    window.title(appName + " - *" + currentFilePath)

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def find(tx, word,color,targ):
    try:
        text, line = tx.get("1.0",END), 0
        text = text.split("\n")
        for x, i in enumerate(text):
            if word in i:
                for e in range(0, i.count(word)):
                    index = find_nth(i, word, e+1)
                    start = float(str(x+1)+"."+str(index))
                    end = float(str(x+1)+"."+str(index+len(word)))
                    tx.focus()
                    tx.tag_add(targ, start, end)
                    tx.tag_config(targ,foreground=color)
    except:
        pass
def colors(tx):
    while True:
        for i in orange:
            find(tx, i, "orange","orange")
        for i in purple:
            find(tx, i, "purple","purple")
        for i in red:
            find(tx, i, "red","red")
# Widgets

# Text Area
txt = scrolledtext.ScrolledText(window, height=999)
txt.grid(row=1,sticky=N+S+E+W)

# Bind event in the widget to a function
txt.bind('<KeyPress>', textchange)
Thread(target=colors, args=[txt],daemon=True).start()
# Menu
menu = Menu(window)

# set tearoff to 0
fileDropdown = Menu(menu, tearoff=False)

Run =  Menu(menu, tearoff=False)

# Add Commands and and their callbacks
fileDropdown.add_command(label='New', command=lambda: fileDropDownHandeler("new"))
fileDropdown.add_command(label='Open', command=lambda: fileDropDownHandeler("open"))


Run.add_command(label='Run script', command=lambda: RunS("RunScript"))

# Adding a seperator between button types.
fileDropdown.add_separator()
fileDropdown.add_command(label='Save', command=lambda: fileDropDownHandeler("save"))
fileDropdown.add_command(label='Save as', command=lambda: fileDropDownHandeler("saveAs"))

menu.add_cascade(label='File', menu=fileDropdown)
menu.add_cascade(label='Run', menu=Run)

# Set Menu to be Main Menu
window.config(menu=menu)

# Enabling "open with" by looking if the second argument was passed.
if len(sys.argv) == 2:
    currentFilePath = sys.argv[1]

    window.title(appName + " - " + currentFilePath)

    with open(currentFilePath, 'r') as f:
        txt.delete(1.0,END)
        txt.insert(INSERT,f.read())

# Main Loop
window.mainloop()
