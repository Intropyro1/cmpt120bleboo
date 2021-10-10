#Pie.persquareinch.py
#this program calculates the price per square inch of a pizza, given the diameter and price of the pizza.

import math

def main():
    print("this program calculates the price per square inch of a pizza")
    print()
    diameter = float(input("Enter the diameter of the pizza: "))
    area = float(math.pi * (diameter/2)**2)
    price = float(input("Enter the price: "))
    square = area/price

    print("the price per square inch of the pizza is" , square)

main()
