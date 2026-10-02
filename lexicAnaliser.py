# lexic analiser

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
    if charList[char] == ' ' or charList[char] == '\t' or charList[char] == '\n':
        char += 1
        return True
    else:
        return False


def Compiler(code:str):
    charList = list(code)
    tokensList = []
    currentCharIndex = 0
    while currentCharIndex < len(charList):
        nextCharIndex, isIdent = GetIdent(currentCharIndex, charList)
        if isIdent:
            tokensList.append("IDENT")
            currentCharIndex = nextCharIndex

        elif GetEmpty(currentCharIndex, charList):
             currentCharIndex += 1

        else:
            tokensList.append("OTHER")
            currentCharIndex += 1
        
    return tokensList

if __name__ == "__main__":
    with open("compilerEntrance.txt") as Entry:
        code = Entry.read()
    print(Compiler(code))
    