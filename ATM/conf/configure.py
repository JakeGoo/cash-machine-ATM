# -*- coding:utf-8 -*-
# author:Zero
import os

# The parent directory of the project
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Maximum deposit fund
limit = 15000

# it's a choose information
info = """
************ ATM2 ************
------choose you number------
1.Account information(账户信息)
2.Deposit(存款) 
3.Withdraw money(取款)
4.Transfer accounts(转账)
5.Quit(退出)
"""

# Display the information of the user account
user_tran = """
----------Your account information----------
Account Number: {n}
User Name: {u}
Balance: ${b}
Save Limit: ${s}
Period: {p}Y
"""
