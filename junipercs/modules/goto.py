# -------------------------------
# Juniper Command System
# 'goto.py'
# Author: Juan Carlos Juárez.
# Licensed under MPL 2.0.
# All rights reserved.
# -------------------------------

import os

# 'goto' Command Subcommands

def goto(path):
    if(os.path.isdir(path)):
        os.chdir(path)
    else:
        print("\n <!> Juniper CS Command Error: Directory does not exist.")