import MemReg
import Lists

#Attach File
def AttachFile(FileName):
    fileName = 'Programs/' + FileName + '.txt'
    d = open(fileName, 'r')

    attachedFile = d.read()
    attachedFile = attachedFile.split('\n')

    readyFile = []
    for each in attachedFile:
        each = each.lower()
        readyFile.append(each)

    isProc = False
    isAuto = False
    index = 0
    for line in readyFile:
        if line != '':
            line = line.split()
            if line[0] == "procedure":
                ProcName = line[1]
                CommandList = []
                isProc = True

            elif line[0] == "endproc":
                isProc = False
                MemReg.Assign('proc', CommandList, ProcName) #Type, Value(CommandList), Variable(ProcName)

            elif isProc:
                storedLine = attachedFile[index]
                CommandList.append(storedLine)

            elif line[0] == "autorun":
                isAuto = True

            elif line[0] == "endrun":
                isAuto = False

            elif isAuto:
                if line[0] == "assign":
                    if line[1] == "string":
                        inputString = ""
                        length = len(line) - 3
                        i = 2
                        while length > 0:
                            if length == 1:
                                inputString = inputString + line[i]
                            else:
                                inputString = inputString + line[i] + " "
                            i += 1
                            length -= 1

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
                    
        index += 1
        
    d.close()

#WriteTo File
def WriteTo(FileName, outVar, LineNumber=None):
    fileName = 'Programs/' + FileName + '.txt'
    d = open(fileName, 'r+')

    outVar = MemReg.Return(outVar)

    if LineNumber != None:
        attachedFile = d.read()
        attachedFile = attachedFile.split('\n')

        del attachedFile[LineNumber - 1]

        attachedFile.insert(LineNumber - 1, outVar)

        outString = ""
        for each in attachedFile:
            outString = outString + str(each) + "\n"

        d.seek(0)
        d.truncate()
        d.write(outString)
        d.close()
        
    else:
        d.seek(0)
        d.truncate()
        d.write(outVar)
        d.close()

#AppendTo File
def AppendTo(FileName, outVar):
    fileName = 'Programs/' + FileName + '.txt'
    d = open(fileName, 'a')
    outVar = MemReg.Return(outVar)
    outVar = '\n' + str(outVar)
    d.write(outVar)
    d.close()

#RemoveFrom File
def RemoveFrom(FileName, LineNumber):
    fileName = 'Programs/' + FileName + '.txt'
    d = open(fileName, 'r+')

    attachedFile = d.read()
    attachedFile = attachedFile.split('\n')

    del attachedFile[LineNumber - 1]

    outString = ""
    for each in attachedFile:
        outString = outString + str(each) + "\n"

    d.seek(0)
    d.truncate()
    d.write(outString)
    d.close()

#ReadFrom File
def ReadFrom(FileName, outVar, LineNumber=None):
    fileName = 'Programs/' + FileName + '.txt'
    d = open(fileName, 'r')

    attachedFile = d.read()
    attachedFile = attachedFile.split('\n')

    outList = []
    if LineNumber != None:       
        outVal = attachedFile[LineNumber - 1]
        MemReg.Assign('string', outVal, outVar)
        
    else:
        outList = attachedFile
        Lists.LAssign('string', outList, outVar)
        
    d.close()
