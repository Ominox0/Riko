from tkinter import Tk, Text, DISABLED, END, NORMAL
class CMD():
    def __init__(self):
        self.root = Tk()
        self.root.title("CMD <|~~~|> output")
        self.t = Text(self.root)
        self.t.grid()

        self.t.tag_config('error', foreground="red")
        self.t.tag_config('warning', foreground="orange")
        self.t["state"] = DISABLED
        
    def AddColor(self,name,foreground="black",background="white"):
        self.t.tag_config(name, background=background, foreground=foreground)

    def AddText(self,text,Color="error"):
        self.t["state"] = NORMAL
        self.t.insert(END, text+"\n", Color)
        self.t["state"] = DISABLED
