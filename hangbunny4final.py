def hangman(secretWord):
    print('Welcome to the game, Hangbunny!')
    print('I am thinking of a word that is', len(secretWord), "letters long.")
    def isWordGuessed(secretWord, lettersGuessed):
        for i in secretWord:
            if i in lettersGuessed:
                return True
            return False

    def getGuessedWord(secretWord, lettersGuessed):
        string = ""
        for i in secretWord:
            if i in lettersGuessed:
                string += i
            else:
                string += "_"
        return string
    def getAvailableLetters(lettersGuessed):
        temp = ""
        string = "abcdefghijklmnopqrstuvwxyz"
        for i in string:
            if i not in lettersGuessed:
                temp += i
        return temp

    mistakesMade = 0
    lettersGuessed = []

    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('Congratulations, you won!')
            break
        else:
        	print('------------')
        	print('You have', 8 - mistakesMade, 'guesses left.')
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Please guess a letter:')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 8 - mistakesMade == 0:
        	print('------------')
        	print('Sorry, you ran out of guesses. The word was', secretWord)
        	break
        else:
        	continue
hangman('stupid')