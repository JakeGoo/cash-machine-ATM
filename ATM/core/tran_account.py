# -*- coding:utf-8 -*-
# author:Zero
"""
The user's transfer operation will not operate if the funds
are insufficient or the transferred funds exceed the limit
or the other account number does not exist..
"""
import os
import json
from conf import configure
BASE = configure.BASE
limit = configure.limit
negative = 0


def response(number, statu):
    if statu:
        print("$$$$$$$$$$ Transfer operation $$$$$$$$$$")
        other = input("Enter the other's account number..\n")
        # find out the input account number if exist
        if not os.path.exists("%s/core/account_data/%s.json" % (BASE, other)):
            print("the other account number does not exist!")
            return
        tran_money = input("Enter transfer amount..\n")
        with open(BASE + "/core/account_data/%s.json" % number, 'r') as user_f, \
                open(BASE + "/core/account_data/%s.json" % other, 'r') as other_f:
            user_data = json.loads(user_f.read())
            other_data = json.loads(other_f.read())
            # if the transfer conditions are not satisfied
        if int(user_data['balance']) - int(tran_money) < negative \
                or int(other_data['balance']) + int(tran_money) > limit:
                print("the transfer conditions are not satisfied!")
                exit()
        else:
            # if ok, overlay the new data
            user_data['balance'] = user_data['balance'] - int(tran_money)
            other_data['balance'] = other_data['balance'] + int(tran_money)
            with open(BASE + "/core/account_data/%s.json" % number, 'w') as user_new_data, \
                    open(BASE + "/core/account_data/%s.json" % other, 'w') as other_new_data:
                user_new_data.write(json.dumps(user_data))
                other_new_data.write(json.dumps(other_data))
            print("Transfer Success!")

    else:
        print("***Program error***")
