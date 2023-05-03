a = float(input())
b = float(input())
c = a/b**2
if c < 18.5:
    print("Underweight")
if c > 18.5 and c < 25:
    print("Normal weight")
if c > 25:
    print("Overweight")