import random
n=random.randint(0,99)
g=int(input("your guess"))
while n != "find":
    if g<n:
        print("guess is low")
        g=int(input("your guess"))
    elif g>n:
        print("guess is high")
        g=int(input("your guess"))
    elif g==n:
        print("your guess is right")
        break
    
