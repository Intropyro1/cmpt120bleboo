#Thunder.py
#This program calculates the distance of a lightning strike based on the time elasped betweem the flash and sound of thunder.

import math
def main():
    print("this program calculates the distance of lighting strikes")
    print()
    time = float(input("Enter time elasped from when you saw the flash and then heard the sound: "))
    distance = time/5
    
    print("the distance  of the lightstrikes is:", distance, "miles")

main()
