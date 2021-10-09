#Speeding.py
#   This program tells the fine for speeding over the limits


import math

def main():
    speed = eval(input("Enter your speed:  "))
    
    if speed >= 90:
        print("Your fine is $50 for going over the state limit at 60, plus $30 for going 30mph over the limit and an additional $200 for going over 90mph in total $280 ")
    elif speed >= 60:
        print("Your fine is $50 for going over state limit")
    elif speed <= 60:
        print("You recieve no fine have a nice day")
    else:
        print("No fine")
        

main()
    
