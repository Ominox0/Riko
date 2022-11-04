# Riko
New programing language based on python

How to run program:
Go to cmd (windows + r, type cmd and click enter or
click windows button on screen or on keyboard and type cmd)


while you are in cmd type riko "FileName.rk"


if you see "**'riko' is not recognized as an internal or external command,
operable program or batch file.**"

finde where riko is stored and copy full path
go to environment variables
click path then new and type path to program.


Or
copy this in .bat file


    SET PATH=%PATH%;YOUR_PROGRAM_DIR_HERE

Now when you have it in you path
you can start program like this(in cmd)


    riko "Filename"
<h2>Update logs:</h2><br>
  <h5>2 November 2022</h5><br>
  bug fixed
  <h5>3 New build in functions:</h5>
  
  
    #Random
    Random(Max Number)
    #Returns number
    
    
    #Read
    Read(File name, Mod <"text" or "byte">)
    #Returns string
    
    
    #Write
    Write(File name, Mod <"text" or "byte">, content)
    #Returns null
  <h5>3 November 2022</h5><br>
  In this new update you can import/read/write in your files<br>
  <h5>4 New build in functions:</h5>
  
  
    #Change directory
    cdir(Dir)
    #Returns null
    
    #gets the current selected directory
    get_dir()
    #Returns string
    
    #Delets file/folder/tree
    delete(mod <"file", "dir" or "tree", dir/file>
    #Rturns null
    
    #lists all files and folders in folder
    listdir(dir)
    #Returns list
  <h5>4 November 2022</h5><br>
  Removed 1 build in function (input_int)<br>
  <h5>9 New build in functions:</h5>
  
  
    #Get content of list by index
    get_index(list, index)
    #Returns obj
    
    #Edits list content
    edit_index(list, index, value)
    #Returns null
    
    #Makes object for gui use
    GuiMake(id, type <"root", "label", "button", "entry", "text", "list">)
    #Returns null
    
    #Configs object of gui !!!-{This function is not 100% done}-!!!
    GuiConfig(id, setting, value)
    #Returns null
    
    #Starts mainloop of gui
    GuiMainloop()
    #Returns null
    
    #int
    int(Obj)
    #Returns intiger
    
    #str
    str(Obj)
    #Returns string
    
    #bool
    bool(Obj)
    #Returns bool
    
    #float
    float(Obj)
    #Returns float

# How do you use riko
it is easy
<h3>Key Words</h3>
[<br>
  'var',<br>
  'and',<br>
  'or',<br>
  'not',<br>
  'if',<br>
  'elif',<br>
  'else',<br>
  'for',<br>
  'to',<br>
  'step',<br>
  'while',<br>
  'fun',<br>
  'then',<br>
  'end',<br>
  'return',<br>
  'continue',<br>
  'break',<br>
]

<h3>Build in functions/variables</h3>
[<br>
"print"<br>
"print_ret"<br>
"input"<br>
"clear"<br>
"is_number"<br>
"is_string"<br>
"is_list"<br>
"is_function"<br>
"append"<br>
"pop"<br>
"extend"<br>
"len"<br>
"run"<br>
"random"<br>
"read"<br>
"write"<br>
"cdir"<br>
"get_dir"<br>
"delete"<br>
"listdir<br>

"get_index<br>
"edit_index<br>
"GuiMake<br>
"GuiConfig<br>
"GuiMainloop<br>
"str<br>
"int<br>
"float<br>
"bool<br>

"true"<br>
"false"<br>
"null"<br>
"math_pi"<br>
]
