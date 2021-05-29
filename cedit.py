import os

print("--- CEdit, the simple Commandline Text editor. ---help for help ---")

totalstr = [""]
cl = 0
dl = [""]
run = True

while run:
    cline = input("> ")

    if cline == "---list":
        liststr = ""
        for i in range(len(totalstr)):
            liststr += totalstr[i]
        print(liststr)

    elif cline == "---help":
        print("---save  saves the file")
        print("---exit  exits the program")
        print("---el    edit a specific line")
        print("---list  lists the complete file")

    elif cline == "---save":
        finalsavestr = ""
        for i in range(len(totalstr)):
            finalsavestr += totalstr[i]
        fn = input("File Name: ")
        f = open(fn, "w")
        f.write(finalsavestr)
        f.close()
        print("File saved as " + fn + ".")

    elif cline == "---exit":
        print("CEdit © by Paul 2021")
        run = False

    elif cline == "---cmd":
        cmd = input("CMD> ")
        os.system(cmd)

    elif cline == "---el":
        elint = int(input("line: "))
        eline = input(str(elint) + "> ")
        totalstr[elint] = eline

    else:
        dl[0] = cline + "\n"
        cl += 1
        totalstr.extend(dl)
