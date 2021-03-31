# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 22:33:42 2021

@author: w7k-j
@https://github.com/W7k-J

"""

import sys
import random
import sqlite3

"""TABLE card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)"""

def main_menu_print():
    if Log == False:
        print("""1. Create an account\n2. Log into account\n0. Exit""")
    else:
        print("""1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit""")

def checker_card_number(number):
    if number[0] != "4":
        print("wrong number")
    elif number [:6] != "400000":
        print("wrong number")
    elif len(number) != 16:
        print("wrong number")



def balance_check():
    
    global current_log
    
    cur.execute(f""" SELECT * FROM card WHERE number = {current_log} """)
    row = tuple(cur.fetchone())

    print("\n")
    print(f"Balance: {row[3]}")
    print("\n")

def add_income():
    print('Enter income:\n')
    income = int(input())
    ### ADD TEST TO CHECK INCOME 
    
    print('Income was added!')
    
    global current_log
    
    cur.execute(f""" SELECT * FROM card WHERE number = {current_log} """)
    row = tuple(cur.fetchone())

    new_balance = income + int(row[3])
    
    cur.execute(f"""UPDATE card SET balance ={new_balance} WHERE number = {current_log}""")
    conn.commit()
    
def transfer():
    print('Transfer')
    print('Enter card number:')
    card_number = input()
    
    global current_log
    
    #Luhn algorithm
    
    if luhn_calculation(card_number[:-1]) != card_number[-1]:
        print("Probably you made a mistake in the card number. Please try again!")
        return
        
    #Not in data base
    try:
        cur.execute(f""" SELECT * FROM card WHERE number = {card_number} """)
        row = tuple(cur.fetchone())
    except:
        print("Such a card does not exist.")
        return()
    
    #Transfer
    
    transfer = int(input('Enter how much money you want to transfer:\n'))
    ###TEST TRANSFER INPUT
    
    cur.execute(f""" SELECT * FROM card WHERE number = {current_log} """)
    row = tuple(cur.fetchone())
    
    if transfer > row[3]:
        print('Not enough money!')
    else:
        cur.execute(f""" SELECT * FROM card WHERE number = {current_log} """)
        row = tuple(cur.fetchone())
        
        new_balance = row[3] - transfer
        
        cur.execute(f"""UPDATE card SET balance ={new_balance} WHERE number = {current_log}""")
        conn.commit()
        
        
        cur.execute(f""" SELECT * FROM card WHERE number = {card_number} """)
        row = tuple(cur.fetchone())
        
        new_balance = row[3] + transfer
        
        cur.execute(f"""UPDATE card SET balance ={new_balance} WHERE number = {card_number}""")
        conn.commit()
        

        
        print('Success!')



def close_account():
    global current_log
    cur.execute(f"""DELETE FROM card WHERE number = {current_log}""")
    conn.commit()
    log_out()
    
    
def testing():
    for row in cur.execute(f"""SELECT * FROM card"""):
        print(row)
    print((cur.execute(""" SELECT * FROM card""")))
    r = cur.fetchone()
    print(tuple(r))


def log_in():
    card_number = input("Enter your card number \n")
    pin_number = input("Enter your PIN \n")
    print("\n")
    
    try:
        cur.execute(f""" SELECT * FROM card WHERE number = {card_number} """)
        row = tuple(cur.fetchone())
    except:
        print("Wrong card number or PIN!")
        return()
        
    if row[2] == pin_number:
        global Log
        Log = True
        global current_log
        current_log = card_number
        print("You have successfully logged in!")
    else:
        print("Wrong card number or PIN!")

def log_out():
    global Log
    Log = False
    global current_log
    current_log = ""


def leave():
    print("Bye!")
    cur.close()
    conn.close() 
    sys.exit()

def luhn_calculation(lis):
    """put card number without last digit. returns luhn correct number"""
    #control sum
    total = 0
    for num, char in enumerate(lis):
        if (num + 1)% 2 == 1:
            mult = int(char) * 2
            if mult > 9:
                total = total + mult - 9
            else:
                total = total + mult
        else:
            total = total + int(char)

    return str(10 - (total % 10))


def create_account():
    print("Your card has been created")


    print("Your card number:")
    while True:

        #random card without last number
        temp_cn = ("400000" + ''.join([str(random.randrange(10)) for k in range(9)]))

        temp_card_number = temp_cn + luhn_calculation(temp_cn)[-1]

        #check if in database - new random if it is there! break if number unused
        if temp_card_number not in database:
            card_number = temp_card_number
            break
    print(card_number)

    print("Your card PIN:")
    pin = ''.join([str(random.randrange(10)) for k in range(4)])
    print(pin)

    database[card_number] = [pin, 0]

    cur.execute(f"""INSERT INTO card (
        number,
        pin
        )
        VALUES
        (
        {card_number},
        {pin}
        );
        """)
    conn.commit()

# database[4000004938320895][1]  = 1123



conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

try:
    cur.execute("CREATE TABLE card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);")
    conn.commit()
    
except:
    print("database exist")
conn.commit()


# number : (pin, money)
database = {}
Log = False
current_log = ""

while True:
    
    main_menu_print()
    choice = input()
    print("\n")
    if choice == 'test':
        testing()
    
    if Log == False:
        if choice == "1":
            create_account()
        if choice == "2":
            log_in()
            continue
        if choice == "0":
            leave()
            
    if Log == True:
        if choice == "1":
            balance_check()
        if choice == "2":
            add_income()
        if choice == "3":
            transfer()
        if choice == "4":
            close_account()
        if choice == "5":
            log_out()
            
        if choice == "0":
            leave()
            