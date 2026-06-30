accounts = {
    "alex":300,
    "bela":400
}

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
        print(amount,"withdrawn successfully your remaining balance is", balance)
    else:
        print("insufficient balance")
    return balance

def check_balance(balance):
    print("your current balance is ",balance)
    return balance


def transfer(balance):
    ozr_acc = input("for whom are you transfering ").lower()
    if ozr_acc in accounts:
        ozr_balance = accounts[ozr_acc]
        amount=float(input("enter the amount you want to transfer "))
        if amount > balance:
            print("insufficient balance")
        elif amount >= 0:
            balance -= amount
            ozr_balance += amount
            accounts[ozr_acc] = ozr_balance
            
            print(amount, "has been transfered to", ozr_acc,"their current balance is",ozr_balance)
            print("your remaining balance is", balance)
        else:
            print("invalid amount")
    else:
        print("there is no account like that")
        
    return balance


print("1. deposit") 
print("2. withdraw")
print("3. check balance")
print("4. transfer")
print("5. exit")
choice = int(input("enter your choice "))

