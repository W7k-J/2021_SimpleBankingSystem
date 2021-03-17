# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 22:33:42 2021

@author: w7k-j
@https://github.com/W7k-J

"""

import sys
import random

def main_menu_print():
    if Log == False:
        print("""1. Create an account\n2. Log into account\n0. Exit""")
    else:
        print("""1. Balance\n2. Log out\n0. Exit""")
    
def checker_card_number(number):
    if number[0] != "4":
        print("wrong number")
    elif number [:6] != "400000":
        print("wrong number")
    elif len(number) != 16:
        print("wrong number")
    
# def checker_pin(pin):
#     try len 

def log_in():
    card_number = input("Enter your card number \n")
    pin_number = input("Enter your PIN \n")
    print("\n")
    if card_number in database and database[card_number][0] == pin_number:
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
    current_log = 0

def balance_check():
    print("\n")
    print(f"Balance: {database[current_log][1]}")
    print("\n")    
    
def create_account():
    print("Your card has been created")
    
    
    print("Your card number:")
    while True:
        #control sum
        temp_cn = ("400000" + ''.join([str(random.randrange(10)) for k in range(9)]))
        total = 0
        for num, char in enumerate(temp_cn):
            print(str(num) + "----" + str(char))
            if (num + 1)% 2 == 1:
                mult = int(char) * 2
                if mult > 9:  
                    total = total + mult - 9 
                else:
                    total = total + mult
            else:
                total = total + int(char)
        print(total)
        last_digit = str(10 - (total % 10))

        print(last_digit)
        
        temp_card_number = temp_cn + last_digit[-1]        
         
        #check if in database
        if temp_card_number not in database:
            card_number = temp_card_number
            break
    print(card_number)

    print("Your card PIN:")
    pin = ''.join([str(random.randrange(10)) for k in range(4)])
    print(pin)

    database[card_number] = [pin, 0]

# database[4000004938320895][1]  = 1123


# number : (pin, money)
database = {}
Log = False
current_log = 0

while True:
    
    main_menu_print()
    choice = input()
    if choice == "1":
        if Log == False:
            create_account()
        else:
            balance_check()
        
    elif choice == "2":
        if Log == False:
            log_in()
        else:
            log_out()
    elif choice == "0":
        print("Bye!")
        sys.exit()
