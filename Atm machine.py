balance = 1000

print("Welcome to ATM")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = input("Enter your choice: ")

if choice == "1":
    print("Your balance is", balance)

elif choice == "2":
    money = int(input("Enter amount to deposit: "))
    balance = balance + money
    print("Money deposited successfully.")
    print("New balance is", balance)

elif choice == "3":
    money = int(input("Enter amount to withdraw: "))

    if money <= balance:
        balance = balance - money
        print("Please collect your cash.")
        print("Remaining balance is", balance)
    else:
        print("Not enough balance.")

else:
    print("Invalid choice.")