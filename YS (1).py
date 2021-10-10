#Days

#This program numbers days of the year

def leapYear(num):
   if ((num % 400 == 0) or (((num % 4) == 0) and ((num % 100) != 0))):
       return 1
   else:
       return 0

      
def check(month, day, year):      
   month31 = [1,3,5,7,8,10,12]
   month30 = [4,6,9,11]

   if month < 1:
       print("\nPlease correct date input.")
   if month > 12:
       print("\nPlease correct date input.")
   if month == 2:
       lyear = leapYear(year)
       if lyear == 1:
           if day <= 29 and day>= 1:
               print("This is a valid date.")
               return 0
           else:
               print("This is not a valid date.")
               return 1
       else:
           if day <= 28 and day >= 1:
               print("This is a valid date.")
               return 0
           else:  
               print("This is not a valid date.")
               return 1

   for i in month30:
       if i == month:
           if day >= 1 and day <= 30:
               print("This is a valid date.")
               return 0

           else:
               print("This is not a valid date.")
               return 1

   for i in month31:
       if i == month:
           if day >= 1 and day <= 31:
               print("This is a valid date.")
               return 0

  
def main():
   print("This program will check to see if the date is valid.")
   date = input("Please enter a date in the form of Month/Day/Year:")

   try:
       month,day,year = date.split("/")
       month = int(month)
       day = int(day)
       year = int(year)
  
       # Calling leapYear function
       lyear = leapYear(year)
  
       if lyear == 1:
           print("This is a leap year.")
       else:
           print("This is a normal year.")

       result = check(month,day,year)

       num = 0
      
       if result == 0:
           num =(31*(month-1)) + day
           if month >= 3:
               num = num-((4*month)+23)//10
               if month >= 3 and lyear == 1:
                   num = num + 1
           print("The number is:", num)

   except ValueError:
       print("\nPlease correct the date input")

main()
