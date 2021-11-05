a = input("Enter a value between 0 and 1 for a: ")
b = input("Enter a value between 0 and 1 for b: ")

def xor_g(a,b):
    a = input("Enter a value between 0 and 1 for a: ")
    b = input("Enter a value between 0 and 1 for b: ")
    if a != "1":
        if b == "0":
            if a == "0" and b == "0":
                if a == "0" or b == "0":
                    print("0")
    elif a != "0":
        if b == "1":
            if a == "1" and b == "1":
                if a == "1" or b == "1":
                    print("1")   
    #if b != "0":
        #if a == "1":
            #if a == "1" and b == "1":
                #if a or b == "1":
                    #print("0")
                #else:
                    #print("1")
    #if b == "1":
        #if a == "0":
            #print("1")
       #if b == "0":
            #if a == "1":
                #print("1")
xor_g(a,b)
