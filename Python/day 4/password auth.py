

name=str(input("username"))

pass=int(input("password"))



if name == "admin":
    if pass == 1234:
        print("login successful")
else:

 print("login failed")