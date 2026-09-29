# lexic analiser

def GetLetter(char: str) -> bool:
    return char.isalpha()

def GetDigit(char: str) -> bool:
    return char.isdecimal()

def GetIdent(char: int, charList: list[str]) -> int:
    if GetLetter(charList[char]):
        char += 1
        while GetLetter(charList[char]) or GetDigit(charList[char]):
            char += 1
    else:
        return False
    return True

def GetEmpty(char: int, charList: list[str]) -> int:
    if charList[char] == ' ' or charList[char] == '\t' or charList[char] == '\n':
        char += 1
    return char


def Compiler(code:str):
    charList = list(code)
    tokensList = []
    currentCharIndex = 0
    while currentCharIndex < len(charList):
        if GetIdent(currentCharIndex, charList):
            tokensList.append("IDENT")

        elif GetEmpty(currentCharIndex, charList):
            pass

        else:
            tokensList.append("OTHER")
    return tokensList

if __name__ == "__main__":
    with open("compilerEntrance.txt") as Entry:
        code = Entry.read()
    print(Compiler(code))