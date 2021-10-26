#GCD
#   This program gives you the gcd of an inputed number
#

def main():
    def gcd(a, b):
  
        while b:
            a, b = b, a%b
        return a


    while True:
        while True:
            n1=float(input("Enter a positive number "))
            if n1==0 or n1 < 0:
                print("Enter a valid positive number greater than zero")
                continue
            else:
                break

        while True:
            n2=float(input("Enter another number "))
            if n2==0 or n2 <0:
                print('Enter a valid positive number greater than zero')
                continue
            else:
                break
            if n1 < n2:
                print("First number should be greater than second number")
                continue
        r=gcd(n1,n2)
        print("gcd(%d,%d) is %d \n" %(n1,n2,r))
        
main()
