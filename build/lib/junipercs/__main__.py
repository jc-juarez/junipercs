# -------------------------------
# Juniper Command System
# 'juniper_main_script.py'
# Author: Juan Carlos Juárez.
# Licensed under MPL 2.0.
# All rights reserved.
# -------------------------------

import junipercs.juniper_source as jp
import os

def main(): 

    # Command Counter

    commandCounter = 0

    print("\n <<< Welcome to Juniper CS v0.0.1 // A Micro Command System by Juan Carlos Juarez // https://github.com/jc-juarez >>>\n")

    sessionName = input(" Provide a Session Name: ")
    print("\n Options: \n")
    print(" - commands : Display All Juniper CS Commands")
    print(" - variables : Display All Current Session Variables")
    print(" - help : Get help with Juniper CS")
    print(" - exit : Exit Juniper CS")

    while(True):
        print("\n <{0}> Juniper CS - Session: {1} [ {2} ]".format(str(commandCounter),sessionName,str(os.getcwd())))
        command = input(" - ")
        jp.exec(command)
        commandCounter += 1

    return # Unreachable

if __name__ == "__main__":
    main()
