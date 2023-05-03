a=int(input())
for i in range(a):
    str=input()
    newstr=str.split()
    for i in range(len(newstr)):
         if(len(newstr[i]))==4:
             str=str.replace(newstr[i], '****')

    print(str)
