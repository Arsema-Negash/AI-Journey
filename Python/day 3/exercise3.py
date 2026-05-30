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

m = 2
b = -2
x_int = -b / m
y_int = b
slope = m
print("slope, x-intercept, y-intercept:", slope, (x_int,0), (0,y_int))

x1 = 2
y1= 2 
x2 = 6 
y2 = 10
m = (y2-y1)/(x2-x1)
z = ((y2-y1)**2 + (x2-x1)**2)**0.5
print("slope, euclidean distance:", m, z)