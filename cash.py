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
    if int(two_thousand)<100 or int(two_thousand)>0 or int(five_hundred)<100 or int(five_hundred)>0 or int(two_hundred)<100 or int(two_hundred)>0 or int(hundred)<100 or int(hundred)<0:
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
            passd.balance=passd.balance+two_t+five_h+two_h+h
            passd.money=l
            print("Amount loaded successfully")
    else:
        print("Enter the correct amount format")
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
            return "Invalid Pin"+"for Account No : "+str(accno)
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
            if next_combination is not None and next_combination not in notes:
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
            if int(amount) > sum([a * b for a, b in zip(note,l)]):
                return "Sorry, the ATM does not have enough cash."
            elif int(amount)%100!=0:
                return "Please!Enter the amount in multiples of hundred" 
            elif card.balance<int(amount):
                return "Funds not available in your Account"
            else:
                combination = find_notes_combination(int(amount),note,l)
                if combination is None:
                    return "Sorry,ATM Cannot dispense the amount with aailable notes."
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
                    if ggg<=l[0]:
                        l[0]=l[0]-ggg
                    if hhh<=l[1]:
                        l[1]=l[1]-hhh
                    if iii<=l[2]:
                        l[2]=l[2]-iii
                    if hhh<=l[3]:
                        l[3]=l[3]-hhh
                    print("Cash $"+str(amount)+" withdrawed successfully with notes")
                    if ggg!=0:
                        print("\n2000 --> "+str(ggg))
                    if hhh!=0:
                        print("500 --> "+str(hhh))
                    if iii!=0:
                        print("200 --> "+str(iii))
                    if jjj!=0:
                        print("100 --> "+str(jjj))
                    card.balance=card.balance-int(amount)
                    print("Account balance $"+str(card.balance))
                    card.history.append("Debited amount $"+str(amount)+" Closing Balance $"+str(card.balance))
                    passd.balance=passd.balance-int(amount)
                    passd.money=l

        else:
            return "Invalid Pin "+"for Account No : "+str(accno)
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
             print("Invalid Pin for Account No : "+str(accno))
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
            passd.balance = passd.balance+two_t+five_h+two_h+h
            card.balance=card.balance+int(amount)
            card.history.append("Credited amount $"+str(amount)+" Closingbalance is $"+str(card.balance))
            passd.money=l
            return "Amount deposited successfully\nAccount balance : "+str(card.balance)
        else:
            return "Invalid Pin "+"for Account No : "+str(accno)
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
                card1.history.append("Credit transfer by Account No :"+str(accno)+" of amount $"+str(amount)+" Closingbalance is $"+str(card1.balance))
                card.balance=card.balance-int(amount)
                card.history.append("Transfered of amount $"+str(amount)+" to Accno "+str(tranaccno)+" Closing Balance $"+str(card.balance))
                return "Transfer succesfull of amount "+str(amount)+"to Account no : "+str(tranaccno)+"\nYour account balance is"+str(card.balance)
            else:
                return "No account found with userno : "+str(tranaccno)
        else:
            return "Invalid Pin"+"for Account No : "+str(accno)
    else:
        return "Account not found"
def pinchan(user_list,accno,pin,newpin):
    if int(accno) in user_list.keys():
        card=user_list[int(accno)]
        if int(pin)==card.pin:
            card.pin=int(newpin)
            return "Pin changed successfully for Account No : "+str(accno)
        else:
            return "Invalid Pin"+"for Account No : "+str(accno)
    else:
        return "Account not found"


