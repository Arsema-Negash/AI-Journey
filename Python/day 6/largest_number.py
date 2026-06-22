#num = [7,3,9,1,6]
x=input("enter numbers using space:-")
num=list(map(int, x.split()))

large = num[0]
for n in num:
    if n>large:
        large=n
print(large)