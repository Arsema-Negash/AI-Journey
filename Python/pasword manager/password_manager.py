storage = {
    "password":[
        {
        "website":"google",
        "user":"arse",
        "password":"1234"
        },
        {
        "website":"youtube",
        "user":"bill",
        "password":"qwer"
        }
    ]
}

def add(storage):
    new_web=input("enter the website")
    new_user=input("enter the user")
    new_password=input("enter the password")
    
    new = {
        "website":new_web,
        "user":new_user,
        "password":new_password
        }
    
    storage["password"].append(new)
    
    return storage