def add():
    name=input("enter Name") 
    ID=input("enter ID") 
    department=input("enter Department") 
    Age=input("enter Age") 
    CGPA=input("enter CGPA") 
    
    student={
        "name":name,
        "ID":ID,
        "department":department,
        "Age":Age,
        "CGPA":CGPA
    }
    
    return student


student={}
print("student management")
print("1. add student ")
print("2. view student ")
print("3. search student ")
print("4. delete student ")
print("5. exit ")
    
    
choice = int(input ("enter your choice"))
        