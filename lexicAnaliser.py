# lexic analiser
import sys

def GetLetter(char: str) -> bool:
    return char.isalpha()

def GetDigit(char: str) -> bool:
    return char.isdecimal()

def GetIdent(char: int, charList: list[str]):
    initialChar = char
    if GetLetter(charList[char]):
        char += 1
        while GetLetter(charList[char]) or GetDigit(charList[char]):
            char += 1
        return char, True
    else:
        return initialChar, False
        
    

def GetEmpty(char: int, charList: list[str]):
    initialChar = char
    if charList[char] == ' ' or charList[char] == '\t' or charList[char] == '\n':
        char += 1
        while char < len(charList) and (charList[char] == ' ' or charList[char] == '\t' or charList[char] == '\n'):
            char += 1
        return char, True
    else:
        return initialChar, False

def GetIntegerNumber(char: int, charList: list[str]):
    initialChar = char
    if GetDigit(charList[char]):
        char += 1
        while GetDigit(charList[char]):
            char += 1
        if charList[char] == '.':
            char, isFloat = GetFloatNumber(char, charList)
            if isFloat:
                return char, "FLOAT"
            else:
                return char, "INT"
        return char, "INT"
    else:
        return initialChar, False

def GetFloatNumber(char: int, charList: list[str]):
    if charList[char] == '.':
        char += 1
        while GetDigit(charList[char]):
            char += 1
        return char, "FLOAT"
    else:
        return char, False    

def GetNumber(char: int, charList: list[str]):
    return GetIntegerNumber(char, charList)

def Compiler(code:str):
    charList = list(code)
    tokensList = []
    currentCharIndex = 0
    while currentCharIndex < len(charList):
        currentCharIndex, isIdent = GetIdent(currentCharIndex, charList)
        if isIdent:
            tokensList.append("IDENT")

        else:
            currentCharIndex, isEmpty = GetEmpty(currentCharIndex, charList)
            if isEmpty:
                pass

            else:
                currentCharIndex, isNumber = GetNumber(currentCharIndex, charList)
                if isNumber == "INT":
                    tokensList.append("INT")

                elif isNumber == "FLOAT":
                    tokensList.append("FLOAT")

                else:
                    currentCharIndex, isFloatNumber = GetFloatNumber(currentCharIndex, charList)
                    if isFloatNumber:
                        tokensList.append("FLOAT")
                    else:
                        tokensList.append("OTHER")
                        currentCharIndex += 1
        
    return tokensList

if __name__ == "__main__":
    
    entryFile = sys.argv[1]
    with open(entryFile) as Entry:
        code = Entry.read()
    print(Compiler(code))
    