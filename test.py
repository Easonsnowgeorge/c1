a, b = map(int, input().split())
c, d = map(int, input().split())
gas = int(input())
ac = abs(a-c)
bd = abs(b-d)
abcd = ac + bd
if gas >= abcd and (gas - abcd) % 2 == 0:
    print('Y')
else:
    print('N')