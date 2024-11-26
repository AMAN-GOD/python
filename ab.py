import random
list_username = []
list_password = []
list_account_no = []
a = None
b = None
Login = "yes"
while (Login == "yes"):
    ask = input("1 for New User / 2 for Existing User: ")
    
    if (ask == None):
        break
    else:
        if (ask == '1'):
            a = input("Enter your username: - ")
            b = input("Enter your password: - ")
            if (a!=None and b!=None):
                list_username.append(a)
                list_password.append(b)
                print("User added.")
                acc_no = random.randint(10**14, 10**15 - 1)
                print("Your account no is:- ",acc_no)
                list_account_no.append(acc_no)
            else:
                break
            
        elif (ask == '2'):
            a = input("Enter your username: - ")
            b = input("Enter your password: - ")
            if a in list_username:
                index = list_username.index(a)
                if list_password[index] == b:
                    print("Login successful")
                    print('''1.Desposit
                             2.Withdraw
                             3.Check Balance''')
                else:
                    print("Incorrect password")
            else:
                print("User not found")
        else:
            Login = input("Do you want to continue login (yes/no)? ")