from collections import *
from app import *
from typing import *
def load(admin_list,st):
    passd=admin_list[1]
    l=passd.money
    two_thousand=st[:3]
    five_hundred=st[3:6]
    two_hundred=st[6:9]
    hundred=st[9:12]
    am=int(st[12:])
    if int(two_thousand)<=100 or int(two_thousand)>=0 or int(five_hundred)<=100 or int(five_hundred)>=0 or int(two_hundred)<=100 or int(two_hundred)>=0 or int(hundred)<=100 or int(hundred)<=0:
        l[0]=l[0]+int(two_thousand)
        l[1]=l[1]+int(five_hundred)
        l[2]=l[2]+int(two_hundred)
        l[3]=l[3]+int(hundred)
        if l[0]>100 or l[1]>100 or l[2]>100 or l[3]>100:
            l[0]=l[0]-int(two_thousand)
            l[1]=l[1]-int(five_hundred)
            l[2]=l[2]-int(two_hundred)
            l[3]=l[3]-int(hundred)
            print("Tray is full cannot add more money")
        else:
            two_t=int(two_thousand) * 2000
            five_h=int(five_hundred) * 500
            two_h=int(two_hundred) * 200
            h=int(hundred) * 100
            temp=two_t+five_h+two_h+h
            if temp==am:
                passd.balance=passd.balance+temp
                passd.money=l
                passd.history.append("Credited by admin of amount $"+str(am))
                return "Amount of("+str(am)+") loaded successfully to the ATM"
            else:
                print("Entered amount and denomination doesn't match")
    else:
        print("Tray cannot accept more than 100 notes")
def add(user_list,accno,pin):
    if int(accno) in user_list.keys():
        return "Error: That name already exists"
    user_list[int(accno)] = USER(int(accno), int(pin))
    return "Successfully added Account "+ str(accno) + "."
def bal_check(user_list,accno,pin):
    if int(accno) in user_list.keys():
        card=user_list[int(accno)]
        if int(pin)==card.pin:
            return "Account balance for acc no "+str(accno)+" is $"+str(card.balance)
        else:
            return "Invalid pin"+"for account no : "+str(accno)
    else:
        return "Account not found"
def find_notes_combination(amount, denominations, notes_count, index=0, combination=None):
    if combination is None:
        combination = []
    if amount == 0:
        return combination
    if index == len(denominations):
        return
    notes = []
    for i in range(notes_count[index]+1):
        if i * denominations[index] <= amount:
            next_combination = find_notes_combination(amount - i * denominations[index], denominations, notes_count, index+1, combination + [denominations[index]]*i)
            if next_combination is not None:
                notes.append(next_combination + [denominations[index]]*i)
    if len(notes) == 0:
        return 
    return min(notes,key=len)
def withdraw(user_list,accno,pin,amount,admin_list):
    note=[100,200,500,2000]
    passd=admin_list[1]
    l=passd.money
    if int(accno) in user_list.keys():
        card=user_list[int(accno)]
        if int(pin)==card.pin:
            if int(amount) > passd.balance:
                return "Sorry! the ATM does not have enough cash."
            elif int(amount)%100!=0:
                return "Please! Enter the amount in multiples of hundred" 
            elif card.balance<int(amount):
                return "Funds not available in your Account"
            else:
                combination = find_notes_combination(int(amount),note,l[::-1])
                if combination is None:
                    return "Sorry! ATM cannot dispense the amount with available notes."
                else:
                    ggg=0
                    hhh=0
                    iii=0
                    jjj=0
                    for i in range(len(combination)//2):
                        if combination[i]==2000:
                            ggg=ggg+1
                        elif combination[i]==500:
                            hhh=hhh+1
                        elif combination[i]==200:
                            iii=iii+1
                        elif combination[i]==100:
                            jjj=jjj+1
                    l[0]=l[0]-ggg
                    l[1]=l[1]-hhh
                    l[2]=l[2]-iii
                    l[3]=l[3]-hhh
                    print("Cash $"+str(amount)+" withdrawed successfully with notes")
                    print("----Notes---")
                    if ggg!=0:
                        print("2000 --> "+str(ggg))
                    if hhh!=0:
                        print("500 --> "+str(hhh))
                    if iii!=0:
                        print("200 --> "+str(iii))
                    if jjj!=0:
                        print("100 --> "+str(jjj))
                    print("-----------")
                    card.balance=card.balance-int(amount)
                    card.history.append("Debited amount $"+str(amount)+" Closing Balance $"+str(card.balance))
                    passd.balance=passd.balance-int(amount)
                    passd.money=l
                    passd.history.append("Debited by user of amount $"+str(amount))
                    return "Account balance $"+str(card.balance)

        else:
            return "Invalid pin "+"for account No : "+str(accno)
    else:
        return "Account not found"
def mini(user_list,accno,pin):
    if int(accno) in user_list.keys():
        card=user_list[int(accno)]
        if int(pin)==card.pin:
            print("Account balance for acc no "+str(accno)+" is $"+str(card.balance))
            if len(card.history)<=5 and len(card.history)!=0:
                print(*card.history ,sep="\n")
            else:
                for i in range(0,6):
                    print(card.history[i])
        else:
             print("Invalid pin for account no : "+str(accno))
    else:
        print("Account not found")
def depo(user_list,accno,pin,amount,admin_list,money_d):
    passd=admin_list[1]
    l=passd.money
    if int(accno) in user_list.keys():
        card=user_list[int(accno)]
        if int(pin)==card.pin:
            two_thousand=money_d[:3]
            five_hundred=money_d[3:6]
            two_hundred=money_d[6:9]
            hundred=money_d[9:12]
            l[0]=l[0]+int(two_thousand)
            l[1]=l[1]+int(five_hundred)
            l[2]=l[2]+int(two_hundred)
            l[3]=l[3]+int(hundred)
            two_t=int(two_thousand) * 2000
            five_h=int(five_hundred) * 500
            two_h=int(two_hundred) * 200
            h=int(hundred) * 100
            temp=two_t+five_h+two_h+h
            if temp==int(amount):
                passd.balance = passd.balance+temp
                card.balance=card.balance+int(amount)
                card.history.append("Credited amount $"+str(amount)+" Closingbalance is $"+str(card.balance))
                passd.money=l
                passd.history.append("Credited by user of amount $"+str(amount))
                return "Amount deposited successfully\nAccount balance : "+str(card.balance)
            else:
                return "Entered amount and denomination doesn't match"
        else:
            return "Invalid pin "+"for account no : "+str(accno)
    else:
        return "Account not found"
    
def trans(user_list,accno,pin,amount,tranaccno):
    if int(accno) in user_list.keys():
        card=user_list[int(accno)]
        if int(pin)==card.pin:
            if int(card.balance)<int(amount):
                return "Funds not available in your Account to transfer"
            if int(tranaccno) in user_list.keys():
                card1=user_list[int(tranaccno)]
                card1.balance=card1.balance+int(amount)
                card1.history.append("Credit transfer by Account No : "+str(accno)+" of amount $"+str(amount)+" closing balance $"+str(card1.balance))
                card.balance=card.balance-int(amount)
                card.history.append("Transfered of amount $"+str(amount)+" to Account no "+str(tranaccno)+" closing balance $"+str(card.balance))
                return "Transfer succesfull of amount "+str(amount)+"to Account no : "+str(tranaccno)+"\nYour account balance is $"+str(card.balance)
            else:
                return "No account found with no : "+str(tranaccno)
        else:
            return "Invalid pin"+"for account no : "+str(accno)
    else:
        return "Account not found"
def pinchan(user_list,accno,pin,newpin):
    if int(accno) in user_list.keys():
        card=user_list[int(accno)]
        if int(pin)==card.pin:
            card.pin=int(newpin)
            return "Pin changed successfully for account no : "+str(accno)
        else:
            return "Invalid pin"+"for account no : "+str(accno)
    else:
        return "Account not found"


