import MemReg
import SysMath
import Calls
import Loops
import Lists
import FileMan
import IfElseCon
import Inputs

#If / ElseIf
def BoolCase(inVar1, compSym, inVar2):
    if inVar1[0].isdigit():
        try:
            Var1 = int(inVar1)
        except:
            Var1 = float(inVar1)

    else:
        Var1 = MemReg.Return(inVar1, True)
        if Var1 == None:
            if inVar1 == "true" or inVar1 == "false":
                if inVar1 == "true":
                    Var1 = True
                else:
                    Var1 = False

            else:
                Var1 = inVar1

    if inVar2[0].isdigit():
        try:
            Var2 = int(inVar2)
        except:
            Var2 = float(inVar2)

    else:
        Var2 = MemReg.Return(inVar2, True)
        if Var2 == None:
            if inVar2 == "true" or inVar2 == "false":
                if inVar2 == "true":
                    Var2 = True
                else:
                    Var2 = False

            else:
                Var2 = inVar2

    if compSym == "==":
        if Var1 == Var2:
            return True
        else:
            return False
        
    elif compSym == ">=":
        if Var1 >= Var2:
            return True
        else:
            return False

    elif compSym == "<=":
        if Var1 <= Var2:
            return True
        else:
            return False

    elif compSym == "!=":
        if Var1 != Var2:
            return True
        else:
            return False

    elif compSym == ">":
        if Var1 > Var2:
            return True
        else:
            return False

    elif compSym == "<":
        if Var1 < Var2:
            return True
        else:
            return False

#IfElse Loop
def IfElseLoop(Core, Inner):
    boolCount = 0
    killSwitch = False
    tempVal = Core[boolCount]
    tempLine = tempVal.lower()
    tempLine = tempLine.split()

    if len(tempLine) > 4:
        boolVal = not BoolCase(tempLine[2], tempLine[3], tempLine[4])
    else:
        boolVal = BoolCase(tempLine[1], tempLine[2], tempLine[3])
        
    while not boolVal:
        boolCount += 1
        tempVal = Core.get(boolCount, None)
        if tempVal == None:
            killSwitch = True
            break
        else:
            tempLine = tempVal.lower()
            tempLine = tempLine.split()

            if tempLine[0] == "else":
                boolVal = True
            elif len(tempLine) > 4:
                boolVal = not BoolCase(tempLine[2], tempLine[3], tempLine[4])
            else:
                boolVal = BoolCase(tempLine[1], tempLine[2], tempLine[3])

    if not killSwitch:
        CommandList = Inner[boolCount]
        commandlength = len(CommandList)
        linenumber = 0
        while commandlength > 0:
            storedLine = CommandList[linenumber]
            line = storedLine
            line = line.lower()
            line = line.split()
                
            if line != '':
                if line[0] == "assign":
                    if line[1] == "string":
                        stringLine = storedLine.strip()

                        highCut = (len(stringLine) - 1) - len(line[-1])

                        inputString = stringLine[14:highCut]

                        MemReg.Assign(line[1], inputString, line[len(line) - 1]) #Type, Value, Variable
                            
                    else:
                        MemReg.Assign(line[1], line[2], line[3]) #Type, Value, Variable

                elif line[0] == "lassign":
                    inputList = []
                    length = len(line) - 3
                    i = 2
                    while length > 0:
                        inputList.append(line[i])
                        i += 1
                        length -= 1
                        
                    Lists.LAssign(line[1], inputList, line[len(line) - 1]) #Type, List Elements, Variable

                elif line[0] == "dup":
                    MemReg.Dup(line[1], line[2]) #Variable to copy, Variable copy location

                elif line[0] == "convert":
                    if len(line) > 3:
                        MemReg.Convert(line[1], line[2], line[3]) #Variable to convert, Type to convert too
                    else:
                        MemReg.Convert(line[1], line[2]) #Variable to convert, Type to convert too

                elif line[0] == "delete":
                    MemReg.Delete(line[1])

                elif line[0] == "add" or line[0] == "subtract" or line[0] == "multiply" or line[0] == "divide" or line[0] == "mod":
                    length = len(line) - 3
                        
                    variableArray = []
                    i = 1
                    while length > 0:
                        variableArray.append(line[i])
                        i += 1
                        length -= 1

                    if line[0] == "add":   
                        SysMath.Add(variableArray, line[len(line) - 2], line[len(line) - 1]) #Array, Type, Output Variable
                    elif line[0] == "subtract":
                        SysMath.Sub(variableArray, line[len(line) - 2], line[len(line) - 1]) #Array, Type, Output Variable
                    elif line[0] == "multiply":
                        SysMath.Mul(variableArray, line[len(line) - 2], line[len(line) - 1]) #Array, Type, Output Variable
                    elif line[0] == "divide":
                        SysMath.Div(variableArray, line[len(line) - 2], line[len(line) - 1]) #Array, Type, Output Variable
                    elif line[0] == "mod":
                        SysMath.Mod(variableArray, line[len(line) - 2], line[len(line) - 1]) #Array, Type, Output Variable

                elif line[0] == "if":
                    #print("hi")
                    IfElseDictCore = dict()
                    IfElseDictIn = dict()
                    ifCount = 0
                    currentCount = 0
                    holdCase = True

                    IfElseDictCore[currentCount] = storedLine
                    ifCount += 1
                    ifList = []

                    linenumber += 1
                    commandlength -= 1
                    storedLine = CommandList[linenumber]
                    line = storedLine.lower()
                    line = line.split()
                    while holdCase:
                        if (line[0] == "continue" or line[0] == "elseif" or line[0] == "else") and ifCount == 1:
                            holdCase = False
                        else:
                            if line[0] == "if" and ifCount > 0:
                                ifCount += 1
                            elif line[0] == "continue" and ifCount > 0:
                                ifCount -= 1
                                
                            ifList.append(storedLine)

                            linenumber += 1
                            commandlength -= 1
                            storedLine = CommandList[linenumber]
                            line = storedLine.lower()
                            line = line.split()

                    IfElseDictIn[currentCount] = ifList

                    elifCase = True
                    while elifCase:
                        if (line[0] == "continue" or line[0] == "else") and ifCount == 1:
                            elifCase = False
                        else:
                            holdCase = True
                            if line[0] == "elseif" and ifCount == 1:
                                currentCount += 1
                                ifList = []
                                IfElseDictCore[currentCount] = storedLine
                                
                                linenumber += 1
                                commandlength -= 1
                                storedLine = CommandList[linenumber]
                                line = storedLine.lower()
                                line = line.split()
                                while holdCase:
                                    if (line[0] == "continue" or line[0] == "elseif" or line[0] == "else") and ifCount == 1:
                                        holdCase = False
                                    else:
                                        if line[0] == "if" and ifCount > 0:
                                            ifCount += 1
                                        elif line[0] == "continue" and ifCount > 0:
                                            ifCount -= 1

                                        ifList.append(storedLine)

                                        linenumber += 1
                                        commandlength -= 1
                                        storedLine = CommandList[linenumber]
                                        line = storedLine.lower()
                                        line = line.split()

                                IfElseDictIn[currentCount] = ifList
                                    
                    if line[0] == "else" and ifCount == 1:
                        currentCount += 1
                        ifList = []
                        IfElseDictCore[currentCount] = storedLine
                        holdCase = True

                        linenumber += 1
                        commandlength -= 1
                        storedLine = CommandList[linenumber]
                        line = storedLine.lower()
                        line = line.split()
                        while holdCase:
                            if line[0] == "continue" and ifCount == 1:
                                holdCase = False
                            else:
                                if line[0] == "if" and ifCount > 0:
                                    ifCount += 1
                                elif line[0] == "continue" and ifCount > 0:
                                    ifCount -= 1

                                ifList.append(storedLine)

                                linenumber += 1
                                commandlength -= 1
                                storedLine = CommandList[linenumber]
                                line = storedLine.lower()
                                line = line.split()

                        IfElseDictIn[currentCount] = ifList

                    if line[0] == "continue":
                        ifCount -= 1

                        IfElseCon.IfElseLoop(IfElseDictCore, IfElseDictIn)
                        
                elif line[0] == "call":
                    Calls.Call(line[1]) #ProcName

                elif line[0] == "procedure":
                    ProcName = line[1]

                    CommandList = []
                    linenumber += 1
                    commandlength -= 1
                    storedLine = CommandList[linenumber]
                    line = storedLine.lower()
                    line = line.split()
                    while line[0] != "endproc":
                        CommandList.append(storedLine)
                        linenumber += 1
                        commandlength -= 1
                        storedLine = CommandList[linenumber]
                        line = storedLine.lower()
                        line = line.split()

                    MemReg.Assign('proc', CommandList, ProcName) #Type, Value(CommandList), Variable(ProcName)

                elif line[0] == "loopstart":
                    if line[-1][0].isdigit():
                        length = int(line[-1])
                    elif line[-1] == "loopstart":
                        length = True
                    else:
                        length = int(MemReg.Return(line[-1])) #Variable
                    CommandList = []
                    linenumber += 1
                    commandlength -= 1
                    storedLine = CommandList[linenumber]
                    line = storedLine.lower()
                    line = line.split()
                    while line[0] != "loopend":
                        CommandList.append(storedLine)
                        linenumber += 1
                        commandlength -= 1
                        storedLine = CommandList[linenumber]
                        line = storedLine.lower()
                        line = line.split()

                    Loops.Loop(length, CommandList) #Length of Loop, List of commands to be looped

                elif line[0] == "print":
                    printValue = MemReg.Return(line[1]) #Variable to be returned
                    print(printValue)

                elif line[0] == "index":
                    Lists.LIndex(line[1], line[2], line[3])

                elif line[0] == "length":
                    Lists.LLength(line[1], line[2])

                elif line[0] == "remove":
                    Lists.LRemove(line[1], line[2])

                elif line[0] == "insert":
                    Lists.LInsert(line[1], line[2], line[3])

                elif line[0] == "append":
                    Lists.LAppend(line[1], line[2])

                elif line[0] == "attach":
                    FileMan.AttachFile(line[1])

                elif line[0] == "search":
                    Lists.LSearch(line[1], line[2], line[3])

                elif line[0] == "writeto":
                    if len(line) > 3:
                        if line[2][0].isdigit():
                            outVal = int(line[2])
                        else:
                            outVal = int(MemReg.Return(line[2])) #Variable
                                
                        FileMan.WriteTo(line[1],line[3],outVal)
                    else:
                        FileMan.WriteTo(line[1], line[2])

                elif line[0] == "appendto":
                    FileMan.AppendTo(line[1], line[2])

                elif line[0] == "removefrom":
                    if line[2][0].isdigit():
                        outVal = int(line[2])
                    else:
                        outVal = int(MemReg.Return(line[2])) #Variable
                        
                    FileMan.RemoveFrom(line[1], outVal)

                elif line[0] == "readfrom":
                    if len(line) > 3:
                        if line[2][0].isdigit():
                            outVal = int(line[2])
                        else:
                            outVal = int(MemReg.Return(line[2])) #Variable
                                
                        FileMan.ReadFrom(line[1],line[3],outVal)
                    else:
                        FileMan.ReadFrom(line[1], line[2])

                elif line[0] == "getinput":
                    if len(line) > 3:
                        inputString = ""
                        length = len(line) - 3
                        i = 2
                        while length > 0:
                            inputString = inputString + line[i] + " "
                            i += 1
                            length -= 1
                                
                        Inputs.GetInput(line[1], line[len(line) - 1], inputString)
                    else:
                        Inputs.GetInput(line[1], line[2])

##                elif line[0] == "save":
##                    f.close()
##                    f = open(mainfileName, 'r')
##                    resetLine = linenumber
##                    while resetLine > 0:
##                        line = f.readline()
##                        resetLine -= 1
##
##                elif line[0] == "run":
##                    fileName = MemReg.Return(line[1])                    
##                    if fileName == None:
##                        fileName = line[1]
##
##                    Main(fileName)
##
##                elif line[0] == "reload":
##                    if line[1] == "true":
##                        MemReg.MemStart()
##
##                    f.close()
##                    f = open(mainfileName, 'r')
##                    linenumber = 0

                elif line[0] == "break":
                    Loops.loopBreak = True

            linenumber += 1
            commandlength -= 1

