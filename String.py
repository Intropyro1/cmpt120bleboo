#String.py
#this program get a string from a given string where all occurrences of the first char is $

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('windows'))
