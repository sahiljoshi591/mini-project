balance = 5000

print(" Bank Account System ")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    print("Your balance is:", balance)

elif choice == "2":
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Deposit successful!")
    print("New balance:", balance)

elif choice == "3":
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance!")

else:
    print("Invalid choice!")