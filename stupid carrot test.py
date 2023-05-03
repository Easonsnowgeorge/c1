def is_vowel(a):
    if a in ["a", "e", "i", "o", "u"]:
        return True
def closest_vowel(i):
    number = ord(i) - 96
    if number <= 3:
        return "a"
    elif number <= 7:
        return "e"
    elif number <= 12:
        return "i"
    elif number <= 18:
        return "o"
    else:
        return "u"
def next_consonant(i):
    number = ord(i) + 1
    if number == 123:
        return "z"
    elif is_vowel(chr(number)):
        return chr(number+1)
    else:
        return chr(number)
word = input()
result = ""
for i in word:
    if is_vowel(i):
        result += i
    else:
        result += i
        result += closest_vowel(i)
        result += next_consonant(i)
print(result)