import MemReg

#List Assign
def LAssign(conType, inputList, storeVar): #Type, List Elements, Variable
    storeList = []
    try:
        for each in inputList:
            if conType == "int":
                storeList.append(int(each))
            elif conType == "float":
                storeList.append(float(each))
            elif conType == "bool":
                storeList.append(bool(each))
            else:
                storeList.append(each)
    except:
        print("Error: Type conversion in list", storeVar, "elements!")

    if conType == "var":
        MemReg.Assign("varlist", storeList, storeVar) #Type, Value, Variable
    else:
        MemReg.Assign("list", storeList, storeVar) #Type, Value, Variable

#List Add
def LAdd(ListName):
    inList = MemReg.Return(ListName)
    listType = MemReg.ReturnType(ListName)

    tallySum = 0
    sumCheck = True
    for each in inList:
        if listType == "varlist":
            testVar = MemReg.Return(each, True)
            if testVar != None:
                if sumCheck:
                    tallySum = testVar
                    sumCheck = False
                else:
                    tallySum += testVar

        else:
            if sumCheck:
                tallySum = each
                sumCheck = False
            else:
                tallySum += each

    return tallySum

#List Sub
def LSub(ListName):
    inList = MemReg.Return(ListName)
    listType = MemReg.ReturnType(ListName)
    
    tallySum = 0
    sumCheck = True
    for each in inList:
        if listType == "varlist":
            testVar = MemReg.Return(each, True)
            if testVar != None:
                if sumCheck:
                    tallySum = testVar
                    sumCheck = False
                else:
                    tallySum -= testVar

        else:
            if sumCheck:
                tallySum = each
                sumCheck = False
            else:
                tallySum -= each

    return tallySum

#List Mul
def LMul(ListName):
    inList = MemReg.Return(ListName)
    listType = MemReg.ReturnType(ListName)
    
    tallySum = 0
    sumCheck = True
    for each in inList:
        if listType == "varlist":
            testVar = MemReg.Return(each, True)
            if testVar != None:
                if sumCheck:
                    tallySum = testVar
                    sumCheck = False
                else:
                    tallySum = tallySum * testVar

        else:
            if sumCheck:
                tallySum = each
                sumCheck = False
            else:
                tallySum = tallySum * each

    return tallySum

#List Div
def LDiv(ListName):
    inList = MemReg.Return(ListName)
    listType = MemReg.ReturnType(ListName)
    
    tallySum = 0
    sumCheck = True
    for each in inList:
        if listType == "varlist":
            testVar = MemReg.Return(each, True)
            if testVar != None:
                if sumCheck:
                    tallySum = testVar
                    sumCheck = False
                else:
                    tallySum = tallySum / testVar

        else:
            if sumCheck:
                tallySum = each
                sumCheck = False
            else:
                tallySum = tallySum / each

    return tallySum

#List Mod
def LMod(ListName):
    inList = MemReg.Return(ListName)
    listType = MemReg.ReturnType(ListName)
    
    tallySum = 0
    sumCheck = True
    for each in inList:
        if listType == "varlist":
            testVar = MemReg.Return(each, True)
            if testVar != None:
                if sumCheck:
                    tallySum = testVar
                    sumCheck = False
                else:
                    tallySum = tallySum % testVar

        else:
            if sumCheck:
                tallySum = each
                sumCheck = False
            else:
                tallySum = tallySum % each

    return tallySum

#Index
def LIndex(ListName, Position, outVar):
    inList = MemReg.Return(ListName)
    listType = MemReg.ReturnType(ListName)

    if Position.isdigit():
        Position = int(Position)
    else:
        Position = MemReg.Return(Position)

    if listType == "varlist":
        tempVar = inList[Position]
        outVal = MemReg.Return(tempVar)
    else:
        outVal = inList[Position]

    outType = type(outVal)
    if outType is int:
        outType = "int"
    elif outType is float:
        outType = "float"
    elif outType is str:
        outType = "string"
    elif outType is bool:
        outType = "bool"
    elif outType is list:
        outType = "list"
        
    MemReg.Assign(outType, outVal, outVar)
    
#Length
def LLength(ListName, outVar):
    inList = MemReg.Return(ListName)
    outVal = len(inList)

    MemReg.Assign("int", outVal, outVar)

#Remove
def LRemove(ListName, Position):
    inList = MemReg.Return(ListName)
    listType = MemReg.ReturnType(ListName)

    if Position.isdigit():
        Position = int(Position)
    else:
        Position = MemReg.Return(Position)
    
    del inList[Position]
    MemReg.Assign(listType, inList, ListName)

#Insert
def LInsert(ListName, inVal, Position):
    inList = MemReg.Return(ListName)
    listType = MemReg.ReturnType(ListName)

    if Position.isdigit():
        Position = int(Position)
    else:
        Position = MemReg.Return(Position)

    if inVal[0].isdigit():
        try:
            inVal = int(inVal)
        except:
            inVal = float(inVal)
    else:
        inVal = MemReg.Return(inVal)

    inList.insert(Position, inVal)
    MemReg.Assign(listType, inList, ListName)

#Append
def LAppend(ListName, inVal):
    inList = MemReg.Return(ListName)
    listType = MemReg.ReturnType(ListName)
    
    if inVal[0].isdigit():
        try:
            inVal = int(inVal)
        except:
            inVal = float(inVal)
    else:
        inVal = MemReg.Return(inVal)

    inList.append(inVal)
    MemReg.Assign(listType, inList, ListName)

#Search
def LSearch(ListName, element, outVar):
    inList = MemReg.Return(ListName)

    if element[0].isdigit():
        try:
            element = int(element)
        except:
            element = float(element)
    else:
        element = MemReg.Return(element)

    i = 0
    for each in inList:
        if element == each:
            break
        i += 1

    MemReg.Assign('int', i, outVar)
