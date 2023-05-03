import string
string = string.ascii_lowercase
def getAvailableLetters(lettersGuessed):
    temp = ""
    string = "abcdefghijklmnopqrstuvwxyz"
    for i in string:
        if i not in lettersGuessed:
            temp += i
    return temp
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))