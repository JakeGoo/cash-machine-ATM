# -*- coding:utf-8 -*-
# author:Zero
import json
from conf import configure
"""
This file is used to give the user a deposit,
The maximum fund for the bank card is 15000.
The excess is not stored in the operation
"""

BASE = configure.BASE
# Maximum deposit fund
limit = configure.limit


def response(number, statu):
    if statu:
        while True:
            print("$$$$$$$$$$ Deposit operation $$$$$$$$$$")
            save = input("How much do you want to deposit in your account this time?\n")
            with open(BASE + "/core/account_data/%s.json" % number, 'r') as display_f:
                get_data = json.loads(display_f.read())
            if int(save) + int(get_data['balance']) > limit:
                    print("The maximum deposit funds have exceeded, please reduce the amount of deposit!")
            else:
                # if ok, overlay the new data
                with open(BASE+"/core/account_data/%s.json" % number, 'w') as new_data:
                    get_data['balance'] = int(save) + int(get_data['balance'])
                    new_data.write(json.dumps(get_data))
                print("Success!---Deposit $ %s" % save)
                break
    else:
        print("***Program error***")
