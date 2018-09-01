# -*- coding:utf-8 -*-
# author:Zero
from core import deposit
from core import tran_account
from core import withdraw
from core import user_message
from core import main
"""
Use decorator...
This file controls the state of user operation (whether it is being operated),
and transfers control of user selected operations to corresponding functions.
Prevent operation from crossing the main entrance of the program
"""


def tran_control(number, mod, statu):
    """
    this is a decorator to control four functions..
    :param number: user accountNumber now
    :param mod: module'name to call function
    :param statu: if True
    :return:
    """
    def fun():
        mod.response(number, statu)
    return fun


def run(number, mod, statu):
    go = tran_control(number, mod, statu)
    go()
