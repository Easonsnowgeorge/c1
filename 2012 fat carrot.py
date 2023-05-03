a = int(input())
b = int(input())
if b > a:
    c = b-a
    if c >=1 and c <= 20:
        print("You are speeding and your fine is $100.")
    if c > 20 and c <= 30:
        print("You are speeding and your fine is $270.")
    if c >= 31:
        print("You are speeding and your fine is $500.")
if a > b:
    print("Congratulations, you are within the speed limit!")