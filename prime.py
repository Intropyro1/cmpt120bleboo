#prime.py
#Program to check if a number is prime or not
def isPrime(num):
    #prime numbers are greater than 1
    if num > 1:
        #check for factors
        for i in range(2, num):
            if (num % i) == 0:
                #if factor is found, set flag to True
                return False
    return True
    
def main():
    #Take input from the user
    num = int(input("Enter a number: "))

    #Check if the number is prime
    flag = isPrime(num)
   

    message = str(num) + " is not a prime number"
    if flag:
        message = str(num) + " is a prime number"
    print(message)
main()
