import MemReg
import Lists

#Add
def Add(variableArray, castType, output): #Array, Type, Output Variable
    tallysum = 0
    sumCheck = True
    for each in variableArray:
        if sumCheck:
            if each[0].isdigit() == True:
                try:
                    tallysum = int(each)
                except:
                    tallysum = float(each)
            else:
                varType = MemReg.ReturnType(each)
                if varType == "list" or varType == "varlist":
                    variableReturned = Lists.LAdd(each)
                else:
                    variableReturned = MemReg.Return(each) #Variable
                try:
                    tallysum = variableReturned
                except:
                    tallysum = variableReturned
            sumCheck = False

        else:        
            if each[0].isdigit() == True:
                try:
                    tallysum += int(each)
                except:
                    tallysum += float(each)
            else:
                varType = MemReg.ReturnType(each)
                if varType == "list" or varType == "varlist":
                    variableReturned = Lists.LAdd(each)
                else:
                    variableReturned = MemReg.Return(each) #Variable
                try:
                    tallysum += variableReturned
                except:
                    tallysum += variableReturned

    MemReg.Assign(castType, tallysum, output) #Type, Value, Variable
    

#Sub
def Sub(variableArray, castType, output): #Array, Type, Output Variable
    tallysum = 0
    sumCheck = True
    for each in variableArray:
        if sumCheck:
            if each[0].isdigit() == True:
                try:
                    tallysum = int(each)
                except:
                    tallysum = float(each)
            else:
                varType = MemReg.ReturnType(each)
                if varType == "list" or varType == "varlist":
                    variableReturned = Lists.LSub(each)
                else:
                    variableReturned = MemReg.Return(each) #Variable
                try:
                    tallysum = int(variableReturned)
                except:
                    tallysum = float(variableReturned)
            sumCheck = False

        else:        
            if each[0].isdigit() == True:
                try:
                    tallysum -= int(each)
                except:
                    tallysum -= float(each)
            else:
                varType = MemReg.ReturnType(each)
                if varType == "list" or varType == "varlist":
                    variableReturned = Lists.LSub(each)
                else:
                    variableReturned = MemReg.Return(each) #Variable
                try:
                    tallysum -= int(variableReturned)
                except:
                    tallysum -= float(variableReturned)

    MemReg.Assign(castType, tallysum, output) #Type, Value, Variable


#Mul
def Mul(variableArray, castType, output): #Array, Type, Output Variable
    tallysum = 0
    sumCheck = True
    for each in variableArray:
        if sumCheck:
            if each[0].isdigit() == True:
                try:
                    tallysum = int(each)
                except:
                    tallysum = float(each)
            else:
                varType = MemReg.ReturnType(each)
                if varType == "list" or varType == "varlist":
                    variableReturned = Lists.LMul(each)
                else:
                    variableReturned = MemReg.Return(each) #Variable
                try:
                    tallysum = int(variableReturned)
                except:
                    tallysum = float(variableReturned)
            sumCheck = False                    

        else:        
            if each[0].isdigit() == True:
                try:
                    tallysum = tallysum * int(each)
                except:
                    tallysum = tallysum * float(each)
            else:
                varType = MemReg.ReturnType(each)
                if varType == "list" or varType == "varlist":
                    variableReturned = Lists.LMul(each)
                else:
                    variableReturned = MemReg.Return(each) #Variable
                try:
                    tallysum = tallysum * int(variableReturned)
                except:
                    tallysum = tallysum * float(variableReturned)

    MemReg.Assign(castType, tallysum, output) #Type, Value, Variable


#Div
def Div(variableArray, castType, output): #Array, Type, Output Variable
    tallysum = 0
    sumCheck = True
    try: 
        for each in variableArray:
            if sumCheck:
                if each[0].isdigit() == True:
                    try:
                        tallysum = int(each)
                    except:
                        tallysum = float(each)
                else:
                    varType = MemReg.ReturnType(each)
                    if varType == "list" or varType == "varlist":
                        variableReturned = Lists.LDiv(each)
                    else:
                        variableReturned = MemReg.Return(each) #Variable
                    try:
                        tallysum = int(variableReturned)
                    except:
                        tallysum = float(variableReturned)
                sumCheck = False

            else:        
                if each[0].isdigit() == True:
                    try:
                        tallysum = tallysum / int(each)
                    except:
                        tallysum = tallysum / float(each)
                else:
                    varType = MemReg.ReturnType(each)
                    if varType == "list" or varType == "varlist":
                        variableReturned = Lists.LDiv(each)
                    else:
                        variableReturned = MemReg.Return(each) #Variable
                    try:
                        tallysum = tallysum / int(variableReturned)
                    except:
                        tallysum = tallysum / float(variableReturned)

        MemReg.Assign(castType, tallysum, output) #Type, Value, Variable
    except ZeroDivisionError:
        print("Attempted Divison by zero!")
    except ValueError:
        print("Error: Type converstion!")
    except:
        print("Unexpected Halting Detected!")

#Mod
def Mod(variableArray, castType, output): #Array, Type, Output Variable
    tallysum = 0
    sumCheck = True
    try:
        for each in variableArray:
            if sumCheck:
                if each[0].isdigit() == True:
                    try:
                        tallysum = int(each)
                    except:
                        tallysum = float(each)
                else:
                    varType = MemReg.ReturnType(each)
                    if varType == "list" or varType == "varlist":
                        variableReturned = Lists.LMod(each)
                    else:
                        variableReturned = MemReg.Return(each) #Variable
                    try:
                        tallysum = int(variableReturned)
                    except:
                        tallysum = float(variableReturned)
                sumCheck = False

            else:        
                if each[0].isdigit() == True:
                    try:
                        tallysum = tallysum % int(each)
                    except:
                        tallysum = tallysum % float(each)
                else:
                    varType = MemReg.ReturnType(each)
                    if varType == "list" or varType == "varlist":
                        variableReturned = Lists.LMod(each)
                    else:
                        variableReturned = MemReg.Return(each) #Variable
                    try:
                        tallysum = tallysum % int(variableReturned)
                    except:
                        tallysum = tallysum % float(variableReturned)

        MemReg.Assign(castType, tallysum, output) #Type, Value, Variable
    except ZeroDivisionError:
        print("Attempted Divison by zero!")
    except ValueError:
        print("Error: Type converstion!")
    except:
        print("Unexpected Halting Detected!")
