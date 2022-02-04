# -------------------------------
# Juniper Command System
# 'list.py'
# Author: Juan Carlos Juárez.
# Licensed under MPL 2.0.
# All rights reserved.
# -------------------------------

import os

# 'list' Command Subcommands

def list_helper_one(path):
    if(os.path.isdir(path)):
        dirList = []
        fileList = []
        for root, dirs, files in os.walk(path):
            dirList = dirs
            fileList = files
            break
        if(len(dirList)):
            print("\n <$> Directory Directories: \n")
            for dir in dirList:
                print(" > {0}".format(dir))
        else:
            print("\n <$> No Directories in this Directory.")
        if(len(fileList)):
            print("\n <$> Directory Files: \n")
            for file in fileList:
                print(" > {0}".format(file))
        else:
            print("\n <$> No Files in this Directory.")
    else:
        print("\n <!> Juniper CS Command Error: Directory does not exist.")

def list_string(path):
    list_helper_one(path)

def list_this(path):
    list_helper_one(path)

def list_id(varMemory,varId):
    path = ""
    if(varId in varMemory):
        path = varMemory[varId][1]
    else:
        print("\n <!> Juniper CS Command Error: Variable does not exist.")
        return
    list_helper_one(path)


