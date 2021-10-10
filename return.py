#firstandlast.py
#This program takes a string and returns the first 2 char and last 2 char if the string is atleast greater than 2 char.

def string_beg_ends(str):
    if len(str) < 2:
        return ''
        
    return str[0:2] + str[-2:]
print(string_beg_ends('w3resource'))
print(string_beg_ends('ju'))
print(string_beg_ends('j'))
