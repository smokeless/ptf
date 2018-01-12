#!/usr/bin/env python
########################################
# Core installation for macOS Packages
########################################
from src.core import logging
import subprocess

# this will do updates and installations

#get a list of users, brew doesn't work as root.
def get_user_list()->str:
    s = subprocess.check_output(["dscl", ".", "list", "/Users" ])
    userList = []
    txt = "".join(map(chr,s)).strip().split('\n')
    for i in txt:
        firstChar = i[0]
        if '_' in firstChar:
            pass
        else:
            userList.append(i)
    #just get the first non-root user skipping nobody, daemon, and obv root
    for i in userList:
        if i=='daemon' or i=='nobody' or i=='root':
            pass
        else:
            return i
get_user_list()




def base_install_modules(module_name):

    # will work for 1 or more space- or comma-separated modules
    modules = module_name.replace(",", " ")
    command = "brew install " + modules
    subprocess.Popen(command, shell=True).wait()
