def deposit():
    balance = 0
    amount = float(input("enter amount you want to deposit "))
    if amount >= 0:
        balance += amount
        print(amount,"deposited successfully and now your balance is ",balance)
    else :
        print("invalid amount")
        
    return balance

def withdraw(balance):
    amount = float(input("enter amount you want to withdraw "))
    if amount <= balance:
        balance -= amount
        print(amount,"withdrawn successfully")
    else:
        print("insufficient balance")
    return balance

print("1. deposit") 
print("2. withdraw")
print("3. check balance")
print("4. transfer")
print("5. exit")
choice = int(input("enter your choice "))

