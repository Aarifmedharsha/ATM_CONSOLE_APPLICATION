from collections import *
from app import *
from cash import *

admins = {
    "aarif":"1234",
    "robin":"ABC1234"
    }
users = {
    "aarif1":"5678",
    "robin1":"9384"
}

admin_list=defaultdict(lambda:[])
user_list=defaultdict(lambda:[])
admin_list[1]=ADMIN(1)
print("**********************************Hi!!Welcome to the bank**********************************")
def run(command:str,type_a):
    if type_a == 1:
        command = command.split(" ")
        if command[0] == "LOAD_AMOUNT":
            print(load(admin_list,command[1]))
        elif command[0] == "ATM_BALANCE":
            print("Current ATM balance is : $"+str(admin_list[1].balance))
            print("-----------------------------")
            print("---------ATM History---------")
            print("-----------------------------")
            print(*admin_list[1].history,sep="\n")
    elif type_a == 2:
        command = command.split(" ")
        if command[0]=="BALANCE_CHECK":
            print(bal_check(user_list,command[1],command[2]))
        elif command[0]=="WITHDRAW":
            print(withdraw(user_list,command[1],command[2],command[3],admin_list))
        elif command[0]=="MINI_STATEMENT":
            mini(user_list,command[1],command[2])
        elif command[0]=="DEPOSIT":
            print(depo(user_list,command[1],command[2],command[3],admin_list,command[4]))
        elif command[0]=="TRANSFER":
            print(trans(user_list,command[1],command[2],command[4],command[3]))
        elif command[0]=="PIN_CHANGE":
            print(pinchan(user_list,command[1],command[2],command[3]))
        elif command[0]=="ADD":
            print(add(user_list,command[1],command[2]))
def user():
    print("Selcect any of the options below")
    n=int(input("1 for balance check\n2 for cash withdrawl\n3 for mini-statement(last 5 transaction)\n4 for deposit\n5 for transfering to other acc\n6 for pinchange\n7 for adding new account to the user\n8 to exit as user \nOption : "))
    if n!=7 and n!=8:
        an=int(input("Enter your accno : "))
        pi=int(input("Enter your pin : "))
    if n==1:
        print("-----------------------------")
        run("BALANCE_CHECK"+" "+str(an)+" "+str(pi),2)
        print("-----------------------------")
    if n==2:
        mn=int(input("Enter amount to withdraw : "))
        print("-----------------------------")
        run("WITHDRAW"+" "+str(an)+" "+str(pi)+" "+str(mn),2)
        print("-----------------------------")
    if n==3:
        print("-----------------------------")
        run("MINI_STATEMENT"+" "+str(an)+" "+str(pi),2)
        print("-----------------------------")
    if n==4:
        mn=int(input("Enter amount to deposit : "))
        print("Denomination")
        a=str(input("Enter count of - 2000 notes(001 format if 1 one note) : "))
        b=str(input("Enter count of - 500 notes(001 format if 1 one note) : "))
        c=str(input("Enter count of - 200 notes(001 format if 1 one note) : "))
        d=str(input("Enter count of - 100 notes(001 format if 1 one note) : "))
        print("-----------------------------")
        run("DEPOSIT"+" "+str(an)+" "+str(pi)+" "+str(mn)+" "+a+b+c+d,2)
        print("-----------------------------")
    if n==5:
        tr=int(input("Enter Accno who to transfer : "))
        mn=int(input("Enter amount to transfer : "))
        print("-----------------------------")
        run("TRANSFER"+" "+str(an)+" "+str(pi)+" "+str(tr)+" "+str(mn),2)
        print("-----------------------------")
    if n==6:
        npin=int(input("Enter your new pin : "))
        print("-----------------------------")
        run("PIN_CHANGE"+" "+str(an)+" "+str(pi)+" "+str(npin),2)
        print("-----------------------------")
    if  n==7:
        accn=int(input("Enter your new acc no : "))
        ppin=int(input("Enter your pin for the new acc no "+str(accn)+" : "))
        print("-----------------------------")
        run("ADD"+" "+str(accn)+" "+str(ppin),2)
        print("-----------------------------")
    if n!=8:
        user()
    if n==8:
        print("Thanks for using our Bank Visit again")
        return
def admin():
    print("Selcect any of the options below")
    n=int(input("1 for loading amount\n2 for balance check\n3 to exit as admin:"))
    if n==1:
        i=str(input("Enter amount to deposit : "))
        print("Denomination")
        a=str(input("Enter count of - 2000 notes(001 format if 1 one note) : "))
        b=str(input("Enter count of - 500 notes(001 format if 1 one note) : "))
        c=str(input("Enter count of - 200 notes(001 format if 1 one note) : "))
        d=str(input("Enter count of - 100 notes(001 format if 1 one note) : "))
        print("-----------------------------")
        run("LOAD_AMOUNT"+" "+a+b+c+d+i,1)
        print("-----------------------------")
    if n==2:
        print("-----------------------------")
        run("ATM_BALANCE",1)
        print("-----------------------------")
    if n!=3:
        admin()
    if n==3:
        print("Thanks Admin!!")
        return
def main():
    s=int(input("For ADMIN -- 1\nFor USER -- 2\nOption : "))
    if s==1:
        username=str(input("Hey!!Admin please enter your username : "))
        password=str(input(str(username)+" please enter your password : "))
        if username in admins.keys():
            if admins.get(username) == password:
                print("Hii Admin("+str(username)+")!!")
                admin()
            else:
                print("Hii! "+str(username)+" Please Check your password")
        else:
            print("OOPS!You are not a admin here!!")
    elif s==2:
        username=str(input("Hey!!User please enter your username : "))
        password=str(input(str(username)+" please enter your password : "))
        if username in users.keys():
            if users.get(username) == password:
                print("Hii User("+str(username)+")!!")
                user()
            else:
                print("Hii! "+str(username)+" Please Check your password")
        else:
            print("OOPS!You are not a user here!!")
    button=int(input("To continue banking 1\nTo exit banking press 0\nOption : "))
    if button==1:
        main()
    else:
        print("Bye!!")
        return    

if __name__=="__main__":
    main()
