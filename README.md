# **Store & Fetch**

### **Description**:

A simple CLI tool for storing/fetching key-value pairs. Given a key-value pair (both strings), these are stored and can be fetched later via the key. 

### **Requirements**:
| User Story | Yes/No |
| :------------------------------------------ | :-----------------------: |
| Should run from CLI by typing `key-value` OR `./key-value.py`.|✅|
| Running the tool must be interactive using `put`, `fetch` and `exit` commands. |✅|
| When accepting commands must output the string "`> `"as a command prompt. |✅|
| If a key exists than the old value is discarded. |✅|
| On success, the command should output the string "`Ok.`". |✅|
| The `exit` command should output the string `Bye!` and exit the program. |✅| 
| Other unknown commands should output the string "`Unknown command. Known commands are: "put", "fetch", "exit".`" |✅|
| If a command has incorrect arguments, will output "`Invalid syntax.`" |✅|
| Must include tests; any testing framework is allowed as long as it doesn't require additional libaries or resources beyond built-in libraries for language of choice |✅|

### **Instructions**:

1. Download GH repo locally
2. Run program with `./key-value.py`.
> * CLI tool should run with the above command, if not, check that the first line of `key-value.py`, "`#!/usr/bin/python`" matches the location and version of your interpreter. e.g. If you're using Python3, change the line to `#1/usr/bin/python3`
> * You may also have to give executable permissions to the file; use the command "`chmod +x key-value.py`".

Enjoy! 