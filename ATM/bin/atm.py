# -*- coding:utf-8 -*-
# author:Zero
"""
This is the place to start the program
"""
import sys
from conf import configure
from core import main

BASE = configure.BASE
sys.path.append(BASE)

main.run()
