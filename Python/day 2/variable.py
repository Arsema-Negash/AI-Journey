#Day 2: 30 Days of python programming
first_name = 'Herpsime'
last_name = 'medi'
full_name = 'Herpsimedi'
country = 'Ethiopia'
city = 'addis ababa' 
age = 812
year = 2026
is_married = False
is_true = True
is_light_on = False
name, age, country = 'Herpsime', 812, 'Ethiopia'
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))

if len(first_name) > len(last_name):
    print('first name is longer than last name')
elif len(first_name) < len(last_name):
    print('last name is longer than first name')
else: print('first name and last name have equal length')
num_1 = 5
num_2 = 4
total = num_1 + num_2
diff = num_1 - num_2
product = num_1 * num_2
division = num_1 / num_2
remaining = num_1 % num_2
exp = num_1 ** num_2
floor_division = num_1 // num_2

radius = 30
area = 3.14 * radius ** 2
circumference = 2* 3.14 * radius

rad = float(input('Enter radius-'))
area = 3.14 * rad ** 2
print(area)