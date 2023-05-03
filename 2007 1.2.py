for i in range(15):
    a = input()
    if a == 'TTYL':
        print("talk to you later")
        break
    if a == 'CU':
        print("see you")
    if a == ':-)':
        print("I'm happy")
    if a == ':-(':
        print("I'm sad")
    if a == ';-)':
        print("wink")
    if a == ':-P':
        print("stick out my tongue")
    if a == '(˜.˜)':
        print("sleepy")
    if a == 'TA':
        print("totally awesome")
    if a == 'CCC':
        print("Canadian Computing Competition")
    if a == 'CUZ':
        print("because")
    if a == 'TY':
        print("thank-you")
    if a == 'YW':
        print("you’re welcome")
    if a != 'CU' and a != ':-(' and a != ';-)' and a != ':-P' and a != '(~.~)' and a != 'TA' and a != 'CCC' and a != 'CUZ' and a != 'TY' and a != 'YW' and a != 'TTYL':
        print(a)