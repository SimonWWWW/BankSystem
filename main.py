import random
import sys
class BankSystem:
    def __init__(self):
        self.balance = 0
        self.pin_number = 0
        self.card_number = 0
    def first_menu(self):
        while True:
            print("1. Create an account")
            print("2. Log into account")
            print("0. Exit")
            input_number_1 = int(input())
            if input_number_1 == 1:
                self.create_account()
            elif input_number_1 == 2:
                self.log_in()
            elif input_number_1 == 0:
                print()
                print("Bye!")
                sys.exit()

    def second_menu(self):
        while True:
            print("1. Balance")
            print("2. Log out")
            print("0. Exit")
            input_number_2 = int(input())
            if input_number_2 == 1:
                print("\nBalance:",self.balance,"\n")
                self.second_menu()
            elif input_number_2 == 2:
                print("\nYou have successfully logged out!\n")
                self.first_menu()
            elif input_number_2 == 0:
                print("\nBye!")
                sys.exit()

    def create_account(self):
        while True:
            Bank_Identification_Number = '400000'
            Account_Identifier = str(random.randint(1000000000,9999999999))
            self.card_number = Bank_Identification_Number+Account_Identifier
            self.pin_number = random.randint(1000,9999)
            digit_sum = 0
            for i, digit in enumerate(reversed(self.card_number)):
                n = int(digit)
                if i % 2 == 0:
                    digit_sum += n
                elif n >= 5:
                    digit_sum += n * 2 - 9
                else:
                    digit_sum += n * 2
            if digit_sum % 10 == 0:
                print("\nYour card has been created")
                print("Your card number:")
                print(self.card_number)
                print("Your card PIN:")
                print(self.pin_number)
                break
    def log_in(self):
        print("\nEnter your card number:")
        log_in_card = input()
        print("Enter your PIN:")
        log_in_pin = int(input())
        if log_in_card == self.card_number and log_in_pin == self.pin_number:
            print("\nYou have successfully logged in!\n")
            self.second_menu()
        else:
            print("\nWrong card number or PIN!\n")
            self.first_menu()
BankSystem().first_menu()