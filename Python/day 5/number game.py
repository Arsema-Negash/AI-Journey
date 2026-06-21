import random

num = random.randint(1,10)
x = int(input("guess number in between 1 to 10 "))
for i in range(1,4):
    if x == num:
        print("you got it ")
        break
    elif x > num:
        print("too high")
    else:
        print("too low")
else:
    print("you lost the number was ", num)