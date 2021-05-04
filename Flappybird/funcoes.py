def isNum(char):
    for digit in range(10):
        if char == str(digit):
            return True
    return False


def isFloat(string):
    for i,char in enumerate(string):
        if i==0 and char == "-" and len(string)>1:
            continue
        if not isNum(char) and not char==".":
            return False
    return True

def isInt(string):
    for i,char in enumerate(string):
        if i == 0 and char == "-" and len(string)>1:
            continue
        if not isNum(char):
            return False
    return True