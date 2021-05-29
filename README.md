# CEdit
## CEdit, the free, open source, lightweight and terribly coded text editor. ##


CEdit is a command line or standalone tool for windows, coded in python.
yes, I know my code is messy.
yes, I know I used way too much variables.
I just needed a tool like this one where I can quickly make and save files line by line, while being able to edit single lines.
There is also a Command integration, i.e. you can enter cmd commands without closing the program (ideal for compiling code etc)

# Usage

by default, on opening the program by either running the executable by hand or typing cedit in cmd (provided you set up your path correctly),
you can instantly start typing, line by line and start a new line by pressing ENTER.

with ---el you can edit a line, you will first be asked which line you want to edit, and then you can type what should be placed into this line.
this can be used, for example, to type one of the --- commands into your file, as ---el doesnt look for those, meaning you can for example write
text files containing ---exit, ---el etc.

with ---exit you can exit the program, which either closes the window if you ran the executable, or brings you back to the command prompt, if ran
from there.

with ---list you can list the entire file that you wrote. the file does not have to be saved for that.

with ---cmd you can enter a command, like a normal cmd shell. CEdit will normally continue once you ran the program.

with ---help you can get a short description of all those commands.

# Installing CEdit

you can install CEdit by either just putting the executable or python file whereever you want and then just run it from there everytime you need it.
you can also put the file into a directory like C:\CEdit or C:\Program Files (x86)\CEdit and then makiing a PATH entry to the folder where cedit.exe
is located.(here's how: https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/)

ScuidTheSquid, 2021

## THANK YOU FOR READING
