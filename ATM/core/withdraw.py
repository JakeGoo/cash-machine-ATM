# -*- coding:utf-8 -*-
# author:Zero
import json
from conf import configure
"""
This file is used to complete the user's withdrawal operation
The whole code is exactly the same as deposit.py
"""

BASE = configure.BASE
negative = 0


def response(number, statu):
    if statu:
        while True:
            print("$$$$$$$$$$ Withdraw operation $$$$$$$$$$")
            draw = input("How much money do you want to take this time? \n")
            with open(BASE + "/core/account_data/%s.json" % number, 'r') as display_f:
                get_data = json.loads(display_f.read())
            if int(get_data['balance']) - int(draw) < negative:
                    print("You don't have enough money to withdraw money!")
            else:
                # if ok, overlay the new data
                with open(BASE+"/core/account_data/%s.json" % number, 'w') as new_data:
                    get_data['balance'] = int(get_data['balance']) - int(draw)
                    new_data.write(json.dumps(get_data))
                print("Success!---Withdraw $ %s" % draw)
                break
    else:
        print("***Program error***")
