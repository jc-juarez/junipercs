# Juniper CS 🕹️

Juniper Command System is a Micro CLI Tool that allows you to manage your files, launch applications, as well as providing extra tools for OS Management.

How to Install & Run Juniper CS
==========

*Requirements: 
- Python 3.6+ installed.

Make sure you have Python 3.6+ installed and run the following command in your terminal to install Juniper CS:

For MacOS/Linux:

```python
pip3 install junipercs
```

For Windows:

```python
pip install junipercs
```

And now to start Juniper CS run the following command:

For MacOS/Linux:

```python
python3 -m junipercs
```

For Windows:

```python
python -m junipercs
```

Juniper CS Commands
==========

Juniper CS allows you to create, read, and traverse files and directories, as well as saving variables making direct references to them in order to use them later. Here are the Commands that Juniper CS offers:

- create dir "{directory_name}" at "{directory_path}"
- create dir "{directory_name}" at this
- create dir "{directory_name}" at "{directory_path}" -> {variable_name}
- create dir "{directory_name}" at this -> {variable_name}
- create file "{file_name}" at "{directory_path}"
- create file "{file_name}" at this
- create file "{file_name}" at "{directory_path}" with "{text_content}"
- create file "{file_name}" at this with "{text_content}"
- create file "{file_name}" at "{directory_path}" -> {variable_name}
- create file "{file_name}" at this -> {variable_name}
- create file "{file_name}" at "{directory_path}" with "{text_content}" -> {variable_name}
- create file "{file_name}" at this with "{text_content}" -> {variable_name}
- goto "{directory_path}"
- list "{directory_path}"
- list this
- list {variable_name}
- up "{upper_directory_path}"
- down
- read "{file_path}"
- read {variable_name}
- var file is "{file_path}" -> {variable_name}
- var directory is "{directory_path}" -> {variable_name}
- forget {variable_name}
   



