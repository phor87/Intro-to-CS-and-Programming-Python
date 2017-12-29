def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    display = ''
    for letters in 'abcdefghijklmnopqrstuvwxyz':
        if letters in lettersGuessed:
            continue
        else:
            display += letters
    return display

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
# abcdfghjlmnoqtuvwxyz