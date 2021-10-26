#Goldbach_conjuncture
#
#

def player_input():
    while True:
        try:
            Num = int(input("Enter an even number: "))
            if Num % 2 !=0:
                print("Not an even number")
            elif Num % 2 == 0 and Num > 2:
                return Num
        except ValueError:
            print("Bad input!")
            continue
def isprime(n):
    for i in range(2,n):     
        if n % i == 0:
            return False
        return n != 1
def main():
    flag = True
    n = player_input()
    for i in range(3,n):
        if isprime(i) and flag:
            for x in range(i+1, n):
                if isprime(i) and i+x == n and flag:
                    print(n,"=", i , "+", x)
                    flag = False
                    
main()
