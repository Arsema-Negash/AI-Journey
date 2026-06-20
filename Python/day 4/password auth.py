

name=str(input("username"))

password=int(input("password"))



if name == "admin":
    if password == 1234:
        print("login successful")
else:
    print("login failed")