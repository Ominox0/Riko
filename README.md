# Riko
New programing language based on python

How to run program:
Go to cmd (windows + r, type cmd and click enter or
click windows button on screen or on keyboard and type cmd)


while you are in cmd type riko "FileName.rk"


if you see *'riko' is not recognized as an internal or external command,
operable program or batch file.*

finde where riko is stored and copy full path
go to environment variables
click path then new and type path to program.


OR
copy this in .bat file


    SET PATH=%PATH%;YOUR_PROGRAM_DIR_HERE

Update:

  3 New build in functions:
  
  
    #Random
    Random(Max Number)
    #Returns Number
    
    
    #Read
    Read(File name, Mod <"text" or "byte">)
    #Returns String
    
    
    #Write
    Write(File name, Mod <"text" or "byte">, content)
    #Returns Null


inside of .rk file your can import : riko scripts [Later you will be able to import python to!]
