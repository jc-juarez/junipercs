# -------------------------------
# Juniper Command System
# 'juniper_source.py'
# Author: Juan Carlos Juárez.
# Licensed under MPL 2.0.
# All rights reserved.
# -------------------------------

# Packages

import junipercs.ply.lex as lex
import junipercs.ply.yacc as yacc
import sys 
import os # delete

# Additional Resources

import junipercs.resources.commands_list as cmd_file
import junipercs.system_parser.tokens as tokens_file
from junipercs.system_parser.tokens_definition import *

# Commands

import junipercs.modules.options as options
import junipercs.modules.create as create
import junipercs.modules.goto as goto
import junipercs.modules.list as list_cmd

#-------------------------------------------
# ___________GLOBAL VARIABLES_______________
#-------------------------------------------

# Variables Memory

varMemory = {}

# Commands List

cmdList = cmd_file.cmdList

# System Tokens

tokens = tokens_file.tokens

# Auxiliary Checks

checkString = False
checkId = False

# ----------------------------
# _____LEXER CONSTRUCTION_____
# ----------------------------

lexer = lex.lex()

# ----------------------------
# __________GRAMMAR___________
# ----------------------------

# Main Grammar Command Production

def p_juniper(t):
    'juniper                : juniper_command'

# Command Options

def p_juniper_command(t):
    '''juniper_command      : command_selection
                            | EXIT
                            | VARIABLES
                            | HELP
                            | COMMANDS'''
    global varMemory
    global cmdList
    selection = str(t[1])
    if(selection is None): return
    if options.default_options(selection,varMemory,cmdList) == 1: sys.exit()
    
# Command Selection
    
def p_command_selection(t):
    '''command_selection    : create 
                            | goto
                            | list
                            | up
                            | down
                            | read
                            | forget
                            | var'''

# Create Selection

def p_create(t):
    '''create               : create_directory
                            | create_file'''

# Goto Command

def p_goto(t):
    'goto               : GOTO STRING'
    path = repr(str(t[2]))[1:-1]
    goto.goto(path)

# List Command

def p_list(t):
    '''list               : list_string
                          | list_id  
                          | list_this '''

def p_list_string(t):
    'list_string          : LIST STRING'
    path = str(t[2])
    list_cmd.list_string(path)

def p_list_id(t):
    'list_id              : LIST ID'
    global varMemory
    varId = str(t[2])
    list_cmd.list_id(varMemory,varId)

def p_list_this(t):
    'list_this            : LIST THIS'
    path = str(os.getcwd())
    list_cmd.list_this(path)

def p_up(t):
    'up                     : UP STRING'
    currentDirectory = str(os.getcwd())
    path = repr(str(currentDirectory))[1:-1]
    upDir = str(t[2])
    newPath = os.path.join(path, upDir)
    if(os.path.isdir(newPath)):
        os.chdir(newPath)
    else:
        print("\n<!> Juniper CS Command Error: Directory does not exist.")

def p_down(t):
    'down                     : DOWN'
    os.chdir("..")

def p_read(t):
    '''read                     : READ STRING is_string
                                | READ ID'''
    global varMemory
    global checkString
    try:
        path = ""
        if(checkString):
            path = repr(str(t[2]))[1:-1]
        else:
            varId = str(t[2])
            if(varId in varMemory):
                path = varMemory[varId][1]
            else:
                print("\n<!> Juniper CS Command Error: Variable does not exist.")
                return
        f = open(path, "r")
        print("\n<$> File Content: \n")
        for x in f:
            print(x)
    except:
        print("\n<!> Juniper CS Command Error: File could not be read or does not exist.")


def p_forget(t):
    'forget                     : FORGET ID'
    global varMemory
    variableId = str(t[2])
    try:
        del varMemory[variableId]
    except KeyError:
        print("\n<!> Juniper CS Command Error: Variable does not exist.") 

def p_create_directory(t):
    '''create_directory     : CREATE DIRECTORY STRING AT STRING ARROW ID
                            | CREATE DIRECTORY STRING AT THIS ARROW ID     
                            | CREATE DIRECTORY STRING AT STRING 
                            | CREATE DIRECTORY STRING AT THIS'''
    global varMemory
    if(t[len(t)-2] == "->" and (t[len(t)-1] in varMemory)):
        print("\n<!> Juniper CS Command Error: Variable with that name already exists.")
        return
    currentDirectory = str(os.getcwd())
    directoryName = str(t[3])
    path = ""
    if(str(t[5]) == "this"):
        path = repr(str(currentDirectory))[1:-1]
    else:
        path = repr(str(t[5]))[1:-1]
    newPath = os.path.join(path, directoryName)
    if(os.path.isdir(newPath)):
        print("\n<!> Juniper CS Command Error: Directory already exists.")
    else:
        try:
            os.mkdir(newPath)
            if(t[len(t)-2] == "->"): 
                varMemory[t[len(t)-1]] = ["Directory",newPath]
        except:
            print("\n<!> Juniper CS Command Error: Directory cannot be created.")

def p_create_file(t):
    '''create_file          : CREATE FILE STRING AT STRING ARROW ID
                            | CREATE FILE STRING AT THIS ARROW ID     
                            | CREATE FILE STRING AT STRING 
                            | CREATE FILE STRING AT THIS
                            | CREATE FILE STRING AT STRING WITH STRING ARROW ID
                            | CREATE FILE STRING AT THIS WITH STRING ARROW ID
                            | CREATE FILE STRING AT STRING WITH STRING
                            | CREATE FILE STRING AT THIS WITH STRING'''
    global varMemory
    if(t[len(t)-2] == "->" and (t[len(t)-1] in varMemory)):
        print("\n<!> Juniper CS Command Error: Variable with that name already exists.")
        return
    currentDirectory = str(os.getcwd())
    fileName = str(t[3])
    path = ""
    if(str(t[5]) == "this"):
        path = repr(str(currentDirectory))[1:-1]
    else:
        path = repr(str(t[5]))[1:-1]
    newPath = os.path.join(path, fileName)
    if(os.path.isfile(newPath)):
        print("\n<!> Juniper CS Command Error: File already exists.")
    else:
        try:
            with open(newPath, 'w') as fp:
                if(len(t) >= 8 and str(t[6] == "with")):
                    fp.write(str(t[7]))
            if(t[len(t)-2] == "->"): 
                varMemory[t[len(t)-1]] = ["File",newPath]        
            #print("\n<" + str(globalCounter) + "$> File '% s' has been created." % fileName)
        except:
            print("\n<!> Juniper CS Command Error: File cannot be created.")

def p_var(t):
    '''var                 : VAR FILE IS STRING ARROW ID
                           | VAR DIRECTORY IS STRING ARROW ID'''
    global varMemory
    objectType = str(t[2])
    varId = str(t[6])
    if(varId in varMemory):
        print("\n<!> Juniper CS Command Error: Variable with that name already exists.")
        return
    path = str(t[4])
    newPath = repr(str(path))[1:-1]
    if(objectType == "file"):
        if(os.path.isfile(newPath)):
            varMemory[varId] = ["File",newPath]
        else:
            print("\n<!> Juniper CS Command Error: Variable Type does not match.")
    else:
        if(os.path.isdir(newPath)):
            varMemory[varId] = ["Directory",newPath]
        else:
            print("\n<!> Juniper CS Command Error: Variable Type does not match.")


def p_is_string(t):
    'is_string             : empty'
    global checkString
    checkString = True

# Syntax Error

def p_error(t):
    if(t is not None):
        print("\n<!> Juniper CS Command Error: Syntax Error at '%s'." % t.value)
    else:
        print("\n<!> Juniper CS Command Error: Syntax Error.")

# Empty Rule

def p_empty(t):
	'''
	empty : 
	'''
	t[0] = None

parser = yacc.yacc()

def resetChecks():
    global checkString
    global checkId
    checkString = checkId = False

def exec(command):
    resetChecks()
    if(command != ""): parser.parse(command)
