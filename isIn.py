def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    mid = int(len(aStr) / 2)
    if len(aStr) == 0:
        return False
    elif char == aStr[mid]:
        return True
    elif len(aStr) == 1:
        return False
    elif char > aStr[mid]:
        return isIn(char, aStr[mid:])
    else:
        return isIn(char, aStr[:mid])

print(isIn('k',''))