import re

#Create Mem
def MemStart():
    global IntMem
    global StringMem
    global FloatMem
    global BoolMem
    global ListMem
    global VariableNameMem
    global ProcMem
    global VarListMem
    
    IntMem = dict()
    StringMem = dict()
    FloatMem = dict()
    BoolMem = dict()
    ListMem = dict()

    VariableNameMem = dict()

    ProcMem = dict()
    VarListMem = dict()

#Assign
def Assign(StoreType, Value, VariableName): #Type, Value, Variable    
    if (VariableNameMem.get(VariableName, None) != None):
        currentType = VariableNameMem.get(VariableName)
        if ((StoreType == currentType) and (currentType == "int")):
            IntMem[VariableName] = int(Value)

        elif ((StoreType == currentType) and (currentType == "float")):
            FloatMem[VariableName] = float(Value)

        elif ((StoreType == currentType) and (currentType == "bool")):
            if Value == "true":
                BoolMem[VariableName] = bool(Value)
            else:
                BoolMem[VariableName] = False

        elif ((StoreType == currentType) and (currentType == "list")):
            ListMem[VariableName] = Value

        elif ((StoreType == currentType) and (currentType == "string")):
            StringMem[VariableName] = Value

        elif ((StoreType == currentType) and (currentType == "proc")):
            ProcMem[VariableName] = Value

        elif ((StoreType == currentType) and (currentType == "varlist")):
            VarListMem[VariableName] = Value
            
        else:
            print("Error: Duplicate Variable Name Assignment!")

    else:
        charCheck = re.compile('abcdefghijklmnopqrstuvwxyz_0123456789')
        if (bool(charCheck.search(VariableName)) == False):
            charCheck = re.compile('abcdefghijklmnopqrstuvwxyz_')
            if (bool(charCheck.search(VariableName[0])) == False):
                if (StoreType == "int"):
                    IntMem[VariableName] = int(Value)

                elif (StoreType == "float"):
                    FloatMem[VariableName] = float(Value)

                elif (StoreType == "bool"):
                    if Value == "true":
                        BoolMem[VariableName] = bool(Value)
                    else:
                        BoolMem[VariableName] = False

                elif (StoreType == "list"):
                    ListMem[VariableName] = Value

                elif (StoreType == "string"):
                    StringMem[VariableName] = str(Value)

                elif (StoreType == "proc"):
                    ProcMem[VariableName] = Value

                elif (StoreType == "varlist"):
                    VarListMem[VariableName] = Value
    
                VariableNameMem[VariableName] = StoreType
                
            else:
                commandWords = ['assign','add','subtract','multiply','divide','mod','compare','call','procedure','endproc','loopstart','loopend','tflag','fflag','gflag','lflag','eflag','continue','true','false','print']
                cwCheck = False
                for each in commandWords:
                    if (VariableName == each):
                        print("Error: Variable name is same as command names!")
                        cwCheck = False
                        break
                    else:
                        cwCheck = True

                if (cwCheck):
                    if (StoreType == "int"):
                        IntMem[VariableName] = int(Value)

                    elif (StoreType == "float"):
                        FloatMem[VariableName] = float(Value)

                    elif (StoreType == "bool"):
                        if Value == "true":
                            BoolMem[VariableName] = bool(Value)
                        else:
                            BoolMem[VariableName] = False
                        
                    elif (StoreType == "list"):
                        ListMem[VariableName] = Value

                    elif (StoreType == "string"):
                        StringMem[VariableName] = str(Value)

                    elif (StoreType == "proc"):
                        ProcMem[VariableName] = Value

                    elif (StoreType == "varlist"):
                        VarListMem[VariableName] = Value

                    VariableNameMem[VariableName] = StoreType
        else:
            print("Error: Variable contains illegal characters!")


#Return
def Return(VariableName, isVar=False): #Variable, Mute for VarLists
    calledVarType = VariableNameMem.get(VariableName, None)
    if (calledVarType == None):
        if not isVar:
            print("Error: Variable", VariableName, "Not Defined!")
        else:
            return (None)
    else:
        if (calledVarType == "int"):
            storedValue = IntMem.get(VariableName)
            return (storedValue)

        elif (calledVarType == "float"):
            storedValue = FloatMem.get(VariableName)
            return (storedValue)
        
        elif (calledVarType == "bool"):
            storedValue = BoolMem.get(VariableName)
            return (storedValue)

        elif (calledVarType == "list"):
            storedValue = ListMem.get(VariableName)
            return (storedValue)
        
        elif (calledVarType == "string"):
            storedValue = StringMem.get(VariableName)
            return (storedValue)
        
        elif (calledVarType == "proc"):
            storedValue = ProcMem.get(VariableName)
            return (storedValue)

        elif (calledVarType == "varlist"):
            storedValue = VarListMem.get(VariableName)
            return (storedValue)

        return (None)
        
#Return Type
def ReturnType(VariableName, isVar=False): #Variable, Mute for VarLists
    calledVarType = VariableNameMem.get(VariableName, None)
    if (calledVarType == None):
        if not isVar:
            print("Error: Variable", VariableName, "Not Defined!")
        else:
            return (None)
    else:
        if (calledVarType == "int"):
            return ("int")

        elif (calledVarType == "float"):
            return ("float")
        
        elif (calledVarType == "bool"):
            return ("bool")

        elif (calledVarType == "list"):
            return ("list")
        
        elif (calledVarType == "string"):
            return ("string")
        
        elif (calledVarType == "proc"):
            return ("proc")

        elif (calledVarType == "varlist"):
            return ("varlist")
        else:
            return (None)

#Duplicate       
def Dup(VariableIn, VariableOut): #Variable to copy, Variable copy location
    inType = ReturnType(VariableIn)
    outType = VariableNameMem.get(VariableOut, None)

    if ((inType == outType) or (outType == None)):
        Assign(inType, Return(VariableIn), VariableOut)
    else:
        print("Error: Unable to duplicate", VariableIn, "into", VariableOut + "!")

#Convert
def Convert(VariableIn, conType, keepForm=False): #Variable to convert, Type to convert too
    inType = ReturnType(VariableIn)
    inVal = Return(VariableIn)

    if inType == "int":
        del IntMem[VariableIn]
        del VariableNameMem[VariableIn]

    elif inType == "float":
        del FloatMem[VariableIn]
        del VariableNameMem[VariableIn]

    elif inType == "string":
        del StringMem[VariableIn]
        del VariableNameMem[VariableIn]

    elif inType == "bool":
        del BoolMem[VariableIn]
        del VariableNameMem[VariableIn]

    elif inType == "proc":
        del ProcMem[VariableIn]
        del VariableNameMem[VariableIn]

    outVal = None
    if inType == conType or (inType == "int" and conType == "float") or (inType == "float" and conType == "int"):
        if conType == "float":
            outVal = float(inVal)
        elif conType == "int":
            outVal = int(outVal)

    elif conType == "string":
        outVal = str(inVal)

    elif conType == "bool":
        outVal = str(inVal)

    elif (conType == "int" and inType == "string") or (conType == "float" and inType == "string"):
        try:
            if conType == "int":
                outVal = int(inVal)
            else:
                outVal = float(inVal)
                
        except:
            outVal = 0
            for each in inVal:
                outVal = outVal + ord(each)

            if conType == "float":
                outVal = float(outVal)

    elif (conType == "list" and inType == "string"):
        outVal = []
        if keepForm:
            outVal = inVal.split()
        else:
            for each in inVal:
                outVal.append(inVal)

    else:
        print("Error: Type conversion failed!")

    Assign(conType, outVal, VariableIn)

#Delete
def Delete(VariableIn):
    inType = ReturnType(VariableIn, True)

    if inType == "int":
        del IntMem[VariableIn]
        del VariableNameMem[VariableIn]

    elif inType == "float":
        del FloatMem[VariableIn]
        del VariableNameMem[VariableIn]

    elif inType == "string":
        del StringMem[VariableIn]
        del VariableNameMem[VariableIn]

    elif inType == "bool":
        del BoolMem[VariableIn]
        del VariableNameMem[VariableIn]

    elif inType == "proc":
        del ProcMem[VariableIn]
        del VariableNameMem[VariableIn]
