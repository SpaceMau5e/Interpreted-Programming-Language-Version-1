import MemReg

#Input
def GetInput(expectedType, variableName, message=""): #Type expected, message to user
    if message == "":
        collectedInput = input(message)
    else:
        message += " "
        collectedInput = input(message)
    returnedInput = None

    try:
        if expectedType == "int":
            try:
                returnedInput = int(collectedInput)
            except:
                returnedInput = 0
                for each in collectedInput:
                    returnedInput = returnedInput + ord(each)

        elif expectedType == "float":
            try:
                returnedInput = float(collectedInput)
            except:
                returnedInput = 0
                for each in collectedInput:
                    returnedInput = returnedInput + ord(each)
                returnedInput = float(returnedInput)

        elif expectedType == "bool":
            returnedInput = bool(collectedInput)

        elif expectedType == "string":
            returnedInput = collectedInput

        MemReg.Assign(expectedType, returnedInput, variableName)

    except:
        print("Error: Incorrect data type entered into input!")
