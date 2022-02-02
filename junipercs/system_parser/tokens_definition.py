# -------------------------------
# Juniper Command System
# 'tokens_definition.py'
# Author: Juan Carlos Juárez.
# Licensed under MPL 2.0.
# All rights reserved.
# -------------------------------

# System Tokens Definition

def t_CREATE(t):
	r'\b(create)\b'
	t.type = 'CREATE'
	return t

def t_SET(t):
	r'\b(set)\b'
	t.type = 'SET'
	return t

def t_DELETE(t):
	r'\b(delete)\b'
	t.type = 'DELETE'
	return t

def t_READ(t):
	r'\b(read)\b'
	t.type = 'READ'
	return t

def t_START(t):
	r'\b(start)\b'
	t.type = 'start'
	return t

def t_NEW(t):
	r'\b(new)\b'
	t.type = 'NEW'
	return t

def t_WEBSERVER(t):
	r'\b(webServer)\b'
	t.type = 'WEBSERVER'
	return t

def t_AT(t):
	r'\b(at)\b'
	t.type = 'AT'
	return t

def t_INSTANCE(t):
	r'\b(instance)\b'
	t.type = 'INSTANCE'
	return t

def t_DIRECTORY(t):
	r'\b(dir)\b'
	t.type = 'DIRECTORY'
	return t

def t_PATH(t):
	r'\b(path)\b'
	t.type = 'PATH'
	return t

def t_EXIT(t):
	r'\b(exit)\b'
	t.type = 'EXIT'
	return t

def t_THIS(t):
	r'\b(this)\b'
	t.type = 'THIS'
	return t

def t_GOTO(t):
	r'\b(goto)\b'
	t.type = 'GOTO'
	return t

def t_LIST(t):
	r'\b(list)\b'
	t.type = 'LIST'
	return t

def t_FILE(t):
	r'\b(file)\b'
	t.type = 'FILE'
	return t

def t_UP(t):
	r'\b(up)\b'
	t.type = 'UP'
	return t

def t_DOWN(t):
	r'\b(down)\b'
	t.type = 'DOWN'
	return t

def t_WITH(t):
	r'\b(with)\b'
	t.type = 'WITH'
	return t

def t_FROM(t):
	r'\b(from)\b'
	t.type = 'FROM'
	return t

def t_VARIABLES(t):
	r'\b(variables)\b'
	t.type = 'VARIABLES'
	return t

def t_HELP(t):
	r'\b(help)\b'
	t.type = 'HELP'
	return t

def t_COMMANDS(t):
	r'\b(commands)\b'
	t.type = 'COMMANDS'
	return t

def t_VAR(t):
	r'\b(var)\b'
	t.type = 'VAR'
	return t

def t_FORGET(t):
	r'\b(forget)\b'
	t.type = 'FORGET'
	return t

def t_IS(t):
	r'\b(is)\b'
	t.type = 'IS'
	return t

# Defined One-Character-Tokens

t_LEFTPAR = r'\('
t_RIGHTPAR = r'\)'
t_QUOTES = r'\"'
t_SEMICOLON = r'\;'
t_DASH = r'\-'
t_DOUBLEDASH = r'\-\-'
t_ARROW = r'\-\>'

# Ignored Line Jumps

t_ignore = " \t"

# Variable Types Definitions

def t_NUMBER(t):
    r'(\-|)\d+((\.\d+)|)'
    try:
        t.value = float(t.value)
    except ValueError:
        print("\n<!> Juniper CS Command Error: Float value not supported %d", t.value)
        t.value = 0
    return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = 'ID'
	return t

def t_STRING(t):
	r'\".+?(")'
	curr = str(t.value)
	curr = curr[1:]
	curr = curr[:-1]
	t.value = curr
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("\n<!> Juniper CS Command Error: '%s' is not a defined Keyword." % t.value[0])
    t.lexer.skip(1)