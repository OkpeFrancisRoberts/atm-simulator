balance = 1000000
password = "1234"  # Set your ATM password

# Ask user to enter password
for attempt in range(3):  # Max 3 attempts
    user_pass = input("Enter your ATM password: ")
    if user_pass == password:
        print("Login successful!\n")
        break
    else:
        print("Incorrect password.")
else:
    print("Too many failed attempts. Exiting...")
    exit()

# Main ATM Menu
while True:
    print("-----Welcome to Opay ATM-----")
    print("Please select an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Enter a number (1-4): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        print(f"Your account balance is: ₦{balance}\n")

    elif choice == 2:
        try:
            deposit = int(input("How much do you want to deposit?: "))
            if deposit <= 0:
                print("Invalid amount. Must be more than 0.\n")
                continue
            balance += deposit
            print(f"Deposit successful! New balance: ₦{balance}\n")
        except ValueError:
            print("Please enter a valid number.\n")

    elif choice == 3:
        try:
            withdraw = int(input("How much do you want to withdraw?: "))
            if withdraw <= 0:
                print("Invalid amount. Must be more than 0.\n")
                continue
            if withdraw > balance:
                print("Insufficient funds.\n")
                continue
            balance -= withdraw
            print(f"Withdrawal successful! New balance: ₦{balance}\n")
        except ValueError:
            print("Please enter a valid number.\n")

    elif choice == 4:
        print("Thank you for using Opay ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please choose between 1 and 4.\n")
  
