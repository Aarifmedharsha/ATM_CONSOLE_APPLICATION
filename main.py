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
def run(command:str,type_a):
    if type_a == 1:
        command = command.split(" ")
        if command[0] == "LOAD_AMOUNT":
            if len(command[1])!= 12:
                print("Error!Please Enter the valid amount")
            else:
                print(load(admin_list,command[1]))
        elif command[0] == "ATM_BALANCE":
            print("Current ATM balance is : "+str(admin_list[1].balance))
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
def main():
    print("**********************************Hi!!Welcome to the bank**********************************\n")
    print("For ADMIN --1\nFor USER --2")
    s=int(input("Option : "))
    if s==1:
        print("Hey!!Admin please enter your username : ")
        username=str(input())
        print(str(username)+" please enter your password : ")
        password=str(input())
        if username in admins.keys():
            if admins.get(username) == password:
                print("Hii Admin("+str(username)+")!! please select any options from below")
                print("1 for Load amount\n2 for Balance check\n3 for exit :")
                n=int(input())
                if n==1:
                    print("Enter count of - 2000 notes(XXX format) : ")
                    a=str(input())
                    print("Enter count of - 500 notes(XXX format) : ")
                    b=str(input())
                    print("Enter count of - 200 notes(XXX format) : ")
                    c=str(input())
                    print("Enter count of - 100 notes(XXX format) : ")
                    d=str(input())
                    run("LOAD_AMOUNT"+" "+a+b+c+d,1)
                if n==2:
                    run("ATM_BALANCE",1)
                if n==3:
                    print("Succesfully Logged Out")
                    return
            else:
                print("Hii! "+str(username)+" Please Check your password")
        else:
            print("OOPS!You are not a admin here!!")
    elif s==2:
        print("Hey!!User please enter your username : ")
        username=str(input())
        print(str(username)+" please enter your password : ")
        password=str(input())
        if username in users.keys():
            if users.get(username) == password:
                print("Hii User("+str(username)+")!! please select any options from below : ")
                n=int(input("1 for Balance Check\n2 for Withdrawl\n3 for MiniStatement()\n4 for Deposit\n5 for Transfer\n6 for Pin Change\n7 for adding\n8 for exit : "))
                if n!=7:
                    an=int(input("Enter your accno : "))
                    pi=int(input("Enter your pin : "))
                if n==1:
                    run("BALANCE_CHECK"+" "+str(an)+" "+str(pi),2)
                if n==2:
                    mn=int(input("Enter amount to withdraw :"))
                    run("WITHDRAW"+" "+str(an)+" "+str(pi)+" "+str(mn),2)
                if n==3:
                    run("MINI_STATEMENT"+" "+str(an)+" "+str(pi),2)
                if n==4:
                    mn=int(input("Enter amount to deposit :"))
                    print("Enter count of - 2000 notes(XXX format) : ")
                    a=str(input())
                    print("Enter count of - 500 notes(XXX format) : ")
                    b=str(input())
                    print("Enter count of - 200 notes(XXX format) : ")
                    c=str(input())
                    print("Enter count of - 100 notes(XXX format) : ")
                    sg=str(input())
                    run("DEPOSIT"+" "+str(an)+" "+str(pi)+" "+str(mn)+" "+a+b+c+sg,2)
                if n==5:
                    tr=int(input("Enter Accno who to transfer : "))
                    mn=int(input("Enter amount to transfer : "))
                    run("TRANSFER"+" "+str(an)+" "+str(pi)+" "+str(tr)+" "+str(mn),2)
                if n==6:
                    npin=int(input("Enter your new pin : "))
                    run("PIN_CHANGE"+" "+str(an)+" "+str(pi)+" "+str(npin),2)
                if  n==7:
                    accn=int(input("Enter you new acc no : "))
                    ppin=int(input("Enter you new pin for the new acc no : "))
                    run("ADD"+" "+str(accn)+" "+str(ppin),2)
                if n==8:
                    return
            else:
                print("Hii! "+str(username)+" Please Check your password")
        else:
            print("OOPS!You are not a user here!!")
    print("To Continue press 1\nTo exit press 0")
    button=int(input())
    if button==1:
        main()
    else:
        return    

if __name__=="__main__":
    main()
