a = input("Enter a value between 0 and 1 for a: ")
b = input("Enter a value between 0 and 1 for b: ")
def xor_g(a,b):
        
    def qne(a,b):
        if a != "1":
            if b == "0":
                if a == "0" and b == "0":
                    if a == "0" or b == "0":
                        print("0")
                    else:
                        one(a,b)
    qne(a,b)

    def one(a,b):
        if a != "1":
            if b == "1":
                if a == "0" and b == "1":
                    if a == "1" or b == "1":
                        print("1")
                    else:
                        zero(a,b)
    one(a,b)

    def zero(a,b):
        if a != "0":
            if b == "0":
                if a == "1" and b == "0":
                    if a == "1" or b == "0":
                        print("1")
                    else:
                        xne(a,b)
    zero(a,b)

    def xne(a,b):
        if a != "0":
            if b == "1":
                if a == "1" and b == "1":
                    if a == "1" or b == "1":
                        print("0")
                    else:
                        xero(a,b)
    xne(a,b)

xor_g(a,b)
