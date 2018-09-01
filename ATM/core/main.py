# -*- coding:utf-8 -*-
# author:Zero
from core import status
from core import deposit
from core import tran_account
from core import withdraw
from core import user_message
from conf import configure
import time
import datetime
import json

BASE_DIR = configure.BASE
"""
this file is about ATM main program

"""

# it's a choose information
info = configure.info

# The execution function corresponding to the option of the user enter
user_choose_number = {
    '1': user_message,
    '2': deposit,
    '3': withdraw,
    '4': tran_account
}
index_password = 0
pq = '0'
cq = '5'


def check(number):
    """
    check if the entered account number exists
    if not exist can to register
    :param number:
    :return: flag
    """
    flag = False
    with open(BASE_DIR+"/core/account_data/user_data.txt", 'r') as user_file:
        for line in user_file:
            account_number = line[0:6]
            if account_number == number:
                flag = True
                global index_password
                index_password = line[7:11]
                return flag
        return flag


def run():
    number = input("Enter your account number(6 digits).."
                   "\nAny key to apply for an account\n")
    flag = check(number)
    if flag:
        print("account check is successfully!")
        input_count = 0
        while True:
            password = input("Please input you account password to continue to control.."
                             "\n'0' will exit..\n")
            if password == index_password:
                time.sleep(2)
                print(info)
                choose = input()
                if choose in user_choose_number:
                    # pass the accountNumber and module file to control..
                    status.run(number, user_choose_number[choose], True)
                elif choose == cq:
                    exit()
                else:
                    print("Without this option!")
            elif password == pq:
                exit()
            else:
                print("input password is error..")
                input_count = input_count + 1
                if input_count == 3:
                    print("input error to many! SORRY!")
                    exit()
    else:
        apply = input("no account exists, do you want to apply card? y or n")
        if apply == 'y' or apply == 'Y':
            apply_for_card()
        else:
            print("Thank you ! Bye..")
            exit()


def apply_for_card():
    """
    this function can allow new user to apply a bank account
    :return:
    """
    # create an account number with current time(6 digits)
    account_number = datetime.datetime.now().strftime('%H:%M:%S').replace(':', '').strip()
    print("*** Welcome to apply for an ATM account ***")
    new_name = input("input you name:\n")
    while True:
        new_password = input("think about you password(4 digits):\n")
        check_pass = new_password.isdigit()
        if (not check_pass) or (len(new_password) < 4 or len(new_password) > 4):
            print("Bad password format!")
        else:
            # account number, password, name, balance, save money limit, validity period
            new_dict = {'account number': account_number,
                        'password': new_password,
                        'user_name': new_name,
                        'balance': 0,
                        'limit': 15000,
                        'period': "2020"}
            # use json to write this new account into a separate file(.json)
            with open(BASE_DIR+"/core/account_data/%s.json" % account_number, 'w') as new_append:
                new_append.write(json.dumps(new_dict))
            # write this new account's number and password used to verification check
            with open(BASE_DIR + "/core/account_data/user_data.txt", 'a+') as data_append:
                data_append.write(account_number + " " + new_password + '\n')
            print("Your Account Number is %s\n"
                  "Remember you password: %s\n"
                  "create account is successful and can now be used!" % (account_number, new_password))
            exit()
