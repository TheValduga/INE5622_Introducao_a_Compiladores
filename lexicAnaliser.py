# lexic analiser

def IsLetter():
    pass

def IsDigit():
    pass

def IsIdent():
    pass

def IsEmpty():
    pass

def IsOther():
    pass

def Compiler(codeEntry):
    code = codeEntry.read()
    charList = list(code)
    tokensList = []
    print(charList)
    for _ in range(len(charList)):
        print(1)

if __name__ == "__main__":
    with open("compilerEntrance.txt") as codeEntry:
        tokenizedEntry = Compiler(codeEntry)
    print(tokenizedEntry)