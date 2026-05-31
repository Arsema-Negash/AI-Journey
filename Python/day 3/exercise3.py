age = 265

height = 2.45

z = 2-3j

base = input("Enter Base:")
height = input("Enter height:")
area = 0.5 * base * height

a = input("Enter side a:")
b = input("Enter side b:")
c = input("Enter side c:")

perimeter = a + b + c

width = input("Enter width:")
length = input("Enter length:")
area = length * width
perimeter = 2 * (length + width)

pi = 3.14
r = input("Enter radius:")
area = pi * r ** 2
c = 2 * pi * r

m1 = 2
b = -2
x_int = -b / m1
y_int = b
slope = m1
print("slope, x-intercept, y-intercept:", slope, (x_int,0), (0,y_int))

x1 = 2
y1= 2 
x2 = 6 
y2 = 10
m2 = (y2-y1)/(x2-x1)
z = ((y2-y1)**2 + (x2-x1)**2)**0.5
print("slope, euclidean distance:", m2, z)

if m1 > m2 : 
    print("the first slope is greater than the second slope")
elif m1 < m2 :
    print("the second slope is greater than the first slope")
else :
    print("the first slope is equal to the second slope")

for x in range(-5, 5):
    y = x**2 + (6*x) + 9
    if y != 0:
        continue
    print ("y = 0 when x is",x)

len('python')
len('dragon') 
print(len('python') > len('dragon') )  
print(len('python') < len('dragon') )
print(len('python') != len('dragon') )

word1 = "python"
word2 = "dragon"
print("on" in word1 and "on" in word2)

print("jargon" in "I hope this course is not full of jargon")

print("on" not in "python" and "on" not in "dragon")

length = len("python")
fl_length = float(length)
str_length = str(fl_length)
print(length, fl_length, str_length)

for num in range(1, 100):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is not even")

print(7//3 == int(2.7))

print((type('10')) == (type(10)))

print(int(9.8) == 10)

hrs = input("enter hours: ")
rate = input("enter rate per hour: ")
earn = hrs * rate
print("your week earning is", earn)

yr = input("enter number of years you have lived: ")
sec = yr * 31536000
print("you have lived for", sec, "seconds")

for num in range(1, 6):
    print(num, num**0, num**1, num**2, num**3)