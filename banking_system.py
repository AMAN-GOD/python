import random

list_username = []
list_password = []
list_account_no = []
list_balance = []

Login = "yes"

while (Login == "yes"):
    ask = input("1 for New User / 2 for Existing User: ")
    
    if ask == None:
        break
    else:
        if ask == '1':
            a = input("Enter your username: - ")
            b = input("Enter your password: - ")
            print(a)
            print(b)
            if a and b:
                list_username.append(a)
                list_password.append(b)
                acc_no = random.randint(10**14, 10**15 - 1)
                print("Your account no is:", acc_no)
                list_account_no.append(acc_no)
                list_balance.append(0)
                print("User added successfully.")
            else:
                print("Username or password cannot be empty.")
            
        elif ask == '2':
            a = input("Enter your username: - ")
            b = input("Enter your password: - ")
            if a in list_username:
                index = list_username.index(a)
                if list_password[index] == b:
                    print("Login successful")
                    while True:
                        print('''1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout''')
                        choice = input("Choose an option: ")

                        if choice == '1':
                            deposit_amount = float(input("Enter amount to deposit: "))
                            list_balance[index] += deposit_amount
                            print(f"Deposited {deposit_amount}. New balance: {list_balance[index]}")

                        elif choice == '2':
                            withdraw_amount = float(input("Enter amount to withdraw: "))
                            if withdraw_amount <= list_balance[index]:
                                list_balance[index] -= withdraw_amount
                                print(f"Withdrew {withdraw_amount}. New balance: {list_balance[index]}")
                            else:
                                print("Insufficient balance.")

                        elif choice == '3':
                            print(f"Your current balance is: {list_balance[index]}")

                        elif choice == '4':
                            print("Logging out...")
                            break

                        else:
                            print("Invalid option. Please try again.")
                else:
                    print("Incorrect password")
            else:
                print("User not found")
        else:
            Login = input("Do you want to continue login (yes/no)? ")
