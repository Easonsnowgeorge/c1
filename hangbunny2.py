def getGuessedWord(secretWord, lettersGuessed):
    string = ""
    for i in secretWord:
        if i in lettersGuessed:
            string += i
        else:
            string += "_"
    return string
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))