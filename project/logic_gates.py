a = input("Enter a value between 0 and 1: ")
b = input("Enter a value between 0 and 1: ")
print("These values are not applicable just to help the bypass the error")





def and_g(a,b):
    print("This is the and logic gate")
    if a == 1 and b == 1:
        print(1)
    else:
        print(0)
        #AND logic gate
and_g(a,b)

def or_g(a,b):
    a = input("Enter a value between 0 and 1 for a: ")
    b = input("Enter a value between 0 and 1 for b: ")
    if a == 0 or b == 0:
        print(0)
    else:
        print(1)
        #OR logic gate
or_g(a,b)

def not_g(a,b):
    a = input("Enter a value between 0 and 1 for a: ")
    if a != 1:
        print(1)
    else:
        print(0)
        #Not logic gate
not_g(a,b)

def nand_g(a,b):
    a = input("Enter a value between 0 and 1 for a: ")
    b = input("Enter a value between 0 and 1 for b: ")
    if a == "1" and b == "1":
        if a != "0":
            print("0")
        else:
            print("1")
    else:
        print("1")
        #NAND logic gate
nand_g(a,b)

def xor_g(a,b):
    a = input("Enter a value between 0 and 1 for a: ")
    b = input("Enter a value between 0 and 1 for b: ")
    if a != "1":
        if b == "0":
            if a == "0" and b == "0":
                if a or b == "0":
                    print("0")
                else:
                    print("1")
    if a == "1":
        if b != "0":
            if a == "1" and b == "1":
                if a or b == "1":
                    print("0")
                else:
                    print("1")
    if b == "1":
        if a == "0":
            print("1")
        if b == "0":
            if a == "1":
                print("1")
                
        #XOR logic gate
xor_g(a,b)
