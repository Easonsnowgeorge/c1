num = 0
for i in range(10000):
    a = input()
    if a == 'halt':
        break
    for b in range(len(a)):
        c = a[b]
        if c == 'a':
            num += 1
        if c == 'b':
            num +=2
        if c == 'c':
            num +=3
        if c == 'd':
            num +=1
        if c == 'e':
            num +=2
        if c == 'f':
            num +=3
        if c == 'g':
            num +=1
        if c == 'h':
            num +=2
        if c == 'i':
            num +=3
        if c == 'j':
            num +=1
        if c == 'b':
            num +=2
        if c == 'l':
            num +=3
        if c == 'm':
            num +=1
        if c == 'n':
            num +=2
        if c == 'o':
            num +=3
        if c == 'p':
            num +=1
        if c == 'q':
            num +=2
        if c == 'r':
            num +=3
        if c == 's':
            num +=4
        if c == 't':
            num +=1
        if c == 'u':
            num +=2
        if c == 'v':
            num +=3
        if c == 'w':
            num +=1
        if c == 'x':
            num +=2
        if c == 'y':
            num +=3
        if c == 'z':
            num +=4
        if (c[b] in 'abc') and (c[b+1] in 'abc') or (c[b] in 'def') and (c[b+1] in 'def') or (c[b] in 'ghi') and (c[b+1] in 'ghi') or (c[b] in 'jkl') and (c[b+1] in 'jkl') or (c[b] in 'mno') and (c[b+1] in 'mno') or (c[b] in 'pqrs') and (c[b+1] in 'pqrs') or (c[b] in 'tuv') and (c[b+1] in 'tuv') or (c[b] in 'wxyz') and (c[b+1] in 'wxyz'):
            print(num)