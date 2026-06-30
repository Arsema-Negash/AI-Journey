def deposit():
    balance = 0
    amount = float(input("enter amount you want to deposit "))
    if amount >= 0:
        balance += amount
        print("amount deposited successfully")
    else :
        print("invalid amount")
        
    return balance

print("1. deposit")
print("2. withdraw")
print("3. check balance")
print("4. transfer")
print("5. exit")
choice = int(input("enter your choice "))

