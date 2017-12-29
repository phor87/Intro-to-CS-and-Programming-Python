def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    for letters in secretWord:
        if letters not in lettersGuessed:
            return False
        else:
            continue
    return True

print(isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
print(isWordGuessed('coconut', ['b', 'r', 'w', 'm', 'u', 'a', 'k', 'l', 'f', 'c']))
print(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))