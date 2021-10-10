#Easter.py
#   This program verifies what day of the year easter is when it was inputted
#Al

import math


def Easter(year):
    if year >= 1900 and year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d +5) % 7
        dateofeaster = 22 + d + e
        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            dateofeaster = dateofeaster - 7

        if dateofeaster > 31:
            dateofeaster = dateofeaster - 31
            print("April", dateofeaster)
        else:
            print("March", dateofeaster)
    else:
        print("There is an error")

year = int(input("Enter a year"))
Easter(year)
