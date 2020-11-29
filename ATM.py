from atm.Account import Account
from atm.Bank import Bank
from pprint import pprint

bank = Bank()
a = Account("John", 1, 100.23, 1234)
bank.add_account1(a)
bank.add_account1(Account("Mary", 2, 200.12, 1234))

current = None
cmd = 111
new_user = True
while cmd != 0:
    if (current is not None):
        if (new_user):
            print("Hello,", current.name, " your account number is", current.acc_number)
            new_user = False
        else:
            print(current.name, " your account number is", current.acc_number)
    else:
        print('hello, would you like to login?')

    print(
        "1 - add account,  2 - login,  3 - logout, 4 - show balance, 5 - add funds, 6 - withdraw funds, 7 - transfer,  0 - exit")
    cmd = int(input())
    # print("i got ", cmd)

    # add account
    if cmd == 1:
        current = bank.add_account()

    # logout
    elif cmd == 3:
        if current is not None:
            print("goodbye")
        current = None
        new_user = True

    # login
    elif cmd == 2:
        new_user = True
        if current is not None:
            print("Logging out before you can login again...")
            current = None
            print("logged off")
        print("Login...  ")
        name = str(input("what is your name? "))
        pin = int(input("what is your pin? "))
        current = bank.find_account(name, pin)
        if (current is None):
            print("you don't have an account. Create account before you can continue")

    elif cmd == 4:
        if current is None:
            print("You need to login before you can use your account")
        else:
            print("your balance is ", current.balance)

    # Deposit to account
    elif cmd == 5:
        if current is None:
            print("You need to login before you can use your account")
        else:
            print("depositing...")
            amount = float(input("What amount you wold like to deposit? "))
            if amount > 0:
                current.deposit(amount)
            print("Your balance now is ", current.balance)

    # Withdraw from account
    elif cmd == 6:
        if current is None:
            print("You need to login before you can use your account")
        else:
            print("withdrawing...")
            amount = float(input("What amount you wold like to withdraw? "))
            current.withdraw(amount)
            print("Your balance now is ", current.balance)

    # transfer to another account
    elif cmd == 7:
        if current is None:
            print("You need to login before you can use your account")
        else:
            print("Transferring...")
            amount = float(input("What amount you wold like to transfer? "))
            acc_number = int(input("what destination account number? "))
            bank.transfer(current, acc_number, amount)
            print("Your balance now is ", current.balance)
    else:
        if cmd != 0:
            print("select option 0 .. 7")

    print("")
    # for acc in bank.accounts:
    #     pprint(vars(acc))
    #     print(acc)
print("turning ATM off, good bye!")
