# -------------------------------
# Juniper Command System
# 'commands_list.py'
# Author: Juan Carlos Juárez.
# Licensed under MPL 2.0.
# All rights reserved.
# -------------------------------

# Commands List                            

cmdList = {"create" : [
    'create dir "{directory_name}" at "{directory_path}"',
    'create dir "{directory_name}" at this',
    'create dir "{directory_name}" at "{directory_path}" -> {variable_name}',
    'create dir "{directory_name}" at this -> {variable_name}',
    'create file "{file_name}" at "{directory_path}"',
    'create file "{file_name}" at this',
    'create file "{file_name}" at "{directory_path}" with "{text_content}"',
    'create file "{file_name}" at this with "{text_content}"',
    'create file "{file_name}" at "{directory_path}" -> {variable_name}',
    'create file "{file_name}" at this -> {variable_name}',
    'create file "{file_name}" at "{directory_path}" with "{text_content}" -> {variable_name}',
    'create file "{file_name}" at this with "{text_content}" -> {variable_name}'
],
"goto" : [
    'goto "{directory_path}"'
],
"list" : [
    'list "{directory_path}"',
    'list this',
    'list {variable_name}'
],
"up" : [
    'up "{upper_directory_path}"'
],
"down" : [
    'down'
],
"read" : [
    'read "{file_path}"',
    'read {variable_name}'
],
"var" : [
    'var file is "{file_path}" -> {variable_name}',
    'var directory is "{directory_path}" -> {variable_name}'
],
"forget" : [
    'forget {variable_name}'
]}