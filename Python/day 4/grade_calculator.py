name = input("Enter your name: ")
mark1 = int(input("enter mark 1: "))
mark2 = int(input("enter mark 2: "))
mark3 = int(input("enter mark 3: "))
ave = (mark1 + mark2+ mark3)/3

if ave>=85:
    grade="A"
elif ave>=75:
    grade="B"
elif ave>=65:
    grade="C"
elif ave>=50:
    grade="D"
else:
    grade="F"

match grade:
    case "A" | "B" | "C" | "D":
        status="pass"
    case "F":
        status="fail"

print("Name:", name)
print("Average:", round(ave, 2))
print("grade:", grade)
print("Status:", status)