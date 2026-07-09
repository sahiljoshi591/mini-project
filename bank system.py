accounts = {}

def create_account():
    name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print("Account already exists.")
        return
    accounts[account_number] = {"name": name, "balance": 0.0}
    print("Account created successfully.")


def deposit():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Invalid amount.")
        return
    if amount <= 0:
        print("Enter a positive amount.")
        return
    accounts[account_number]["balance"] += amount
    print("Deposit successful.")


def withdraw():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Invalid amount.")
        return
    if amount <= 0:
        print("Enter a positive amount.")
        return
    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return
    accounts[account_number]["balance"] -= amount
    print("Withdrawal successful.")


def check_balance():
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return
    balance = accounts[account_number]["balance"]
    print(f"Account balance: {balance}")


def main():
    while True:
        print("\nBank System")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Thank you for using the bank system.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()