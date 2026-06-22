x=input("enter numbers using space:-")
num=list(map(int, x.split()))

small = num[0]
for n in num:
    if n<small:
        small=n
print(small)