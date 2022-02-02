# -------------------------------
# Juniper Command System
# 'options.py'
# Author: Juan Carlos Juárez.
# Licensed under MPL 2.0.
# All rights reserved.
# -------------------------------

# Options Subcommands

def default_options(selection,varMemory,cmdList):
    if(selection == "exit"):
        print("\n Thank you for using Juniper CS.\n")
        return 1
    elif(selection == "variables"):
        if(len(varMemory)):
            print("\n Current Session Variables:\n")
            for key in varMemory:
                print(" - {0} < {1} , {2} >".format(key,varMemory[key][0],varMemory[key][1]))
        else:
            print("\n No Variables Created Yet.")
    elif(selection == "commands"):
        print("\n Juniper CS Commands:")
        for key in cmdList:
            print("\n {0} \n".format(key))
            currCommands = cmdList[key]
            for command in currCommands:
                print(" - {0}".format(command))
    elif(selection == "help"):
        print('''\n Juniper Command System is a Micro CLI Tool that allows you to manage your files, launch applications, as well as providing extra tools for OS Management. 
        \n Type 'commands' to see all available commands. 
        \n Type 'variables' to see this Session's Variables. 
        \n Type 'exit' to quit Juniper CS. 
        \n Find more information about Juniper CS at https://github.com/jc-juarez/junipercs''')
    return 0
