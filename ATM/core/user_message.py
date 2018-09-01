# -*- coding:utf-8 -*-
# author:Zero
import json
from conf import configure
from core import status
"""
this file is a ATM2 user's message about account number, password, 
name, balance, save money limit, validity period...
use json to read passed about account number's information
"""

BASE = configure.BASE

# Display the information of the user account
user_tran = configure.user_tran


def response(number, statu):
    if statu:
        with open(BASE+"/core/account_data/%s.json" % number, 'r') as display_f:
            get_infor = json.loads(display_f.read())
            print(user_tran.format(n=get_infor['account number'],
                                    u=get_infor['user_name'],
                                    b=get_infor['balance'],
                                    s=get_infor['limit'],
                                    p=get_infor['period']))
    else:
        print("***Program error***")
