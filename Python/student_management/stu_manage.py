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

def view(student):
    print ("Name:",student["name"])
    print ("ID:",student["ID"])
    print ("Department:",student["department"])
    print ("Age:",student["Age"])
    print ("CGPA:",student["CGPA"])

def search(student):
    id=input("enter id you want to find")
    if student["ID"]==id:
        view(student)
    else:
        print("student not found")
        
def delete(student):
    id=input("enter id you want to delete")
    if student["ID"]==id:
        student.clear()
        print("student deleted")
    else:
        print("student not found")
        
student={}
print("student management")
print("1. add student ")
print("2. view student ")
print("3. search student ")
print("4. delete student ")
print("5. exit ")
    
    
choice = int(input ("enter your choice"))
        

match choice:
    case 1:
        add()
    case 2:
        if student:
            view(student)
        else:
            print("no student record add a student first")
    case 3:
        if student:
            search(student)
        else:
            print("no student record add a student first")
    case 4:
        if student:
            delete(student)
        else:
            print("no student record add a student first")   