from atm.Account import Account
from atm.Bank import Bank

bank = Bank()
a = Account("John", 1, 100.23, 1234)
bank.add_account(a)
bank.add_account(Account("Mary", 2, 200.12, 1234))

current = None
cmd = 111
while cmd != "0":
    if (current != None):
        print("Hello,", current.name )

    print( "1 - add account,  2 - login,  3 - logout, 4 - show balance, 5 - add funds, 6 - withdraw funds, 7 - transfer,  0 - exit" )
    cmd = input() 
    #print("i got ", cmd)

    # add account
    if (cmd == "1"):
        print("adding account...  what is your name?")
        name = str(input())

    # logout
    if (cmd == "3"):
        print("goodbye")
        current = None

    # login
    if (cmd == "2"):
        print("Login...  what is your name?") 
        name = str(input())
        print("Login...  what is your pin?") 
        pin = int(input())
        current = bank.find_account(name, pin)
        if (current == None):
            print("you don't have an account. Do you want to create one?")

    if (cmd == "4"):
        print("your balance is ", current.balance)

    print("")

