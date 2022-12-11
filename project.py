# acc class
import os
import sys
"""" 
THIS PROGRAM ACTS AS AN ATM MACHINE. IT ASKS USERS ITS USERNAME AND
PASSWORD AND LET THE USER DEPOSIT THE MONEY IN THE BANK ACCOUNT. IT 
ALSO ALLOWS THE USER TO WITHDRAW THE MONEY AND ALSO SHOWS THE CURRENT BALANCE 
AFTER WITHDRAWN . IN THE INITIAL THE BALANCE IS ZERO
"""
def main():
        username = input("what is your username?\n")
        password = input("password?\n")
        if username == 'virat' and password == 'virat123' :
            print("welcome!")
        else:
            print("the password or username is wrong")
            exit()
        
        acc = bank_account()
        acc.deposit()
        acc.withdraw()
        acc.display()

# the initial function
class bank_account:
    def __init__(self) :
        self.balance = 0
        print("hello !!! welcome to the atm")

# deposit function
    def deposit(self):
       amount = float(input("Enteramount to be deposited : "))
       self.balance += amount 
       print("\n Amount deposited :", amount)

# withdraw function 
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n you withdrew :" , amount)
        else:
            print("\n insufficient balance  ")

# function to desplay net ballance
    def display(self):
        print("\n Net available balance = " , self.balance ) 

          

if __name__ == '__main__':
    main()
