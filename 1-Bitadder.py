#1-Bit adder
#this is a one bit adder taking into account the carry in and carry out and sum outputs



def main():
    a = int(input("Enter 'A' value(0-1):  "))
    b = int(input("Enter 'B' value(0-1): "))
    c = int(input("Enter 'Cin' value(0-1): "))     

    def bitadder(a,b,c):
        #Inputs(a,b,c)
        #a = input("Enter 'A' value(0-1):  ")
        #b = input("Enter 'B' value(0-1): ")
        #cin = input("Enter 'Cin' value(0-1): ")
        #Outputs(sum(a,b),co)
        #
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
        d = xor_g(a,b)
        def fox(a,b):
            if d != "1":
                if c == "0":
                    if d == "0" and c == "0":
                        print("1")
                    else:
                        xnd(d,c)
        fox(a,b)

        def and_g(a,b):
            if a == "1" and b == "1":
                print("1")
            else:
                print("0")
                #AND logic gate
        and_g(a,b)
        def xnd(d,c):
            if d == "1" and c == "1":
                print("1")
            else:
                print("0")
        xnd(d,c)
        e = and_g(a,b)
        g = and_g(d,c)
        def or_g(a,b):
            if (a == "0" and b == "0") or (e == "0" and g == "1"):
                print("0")
            else:
                print("1")
                    #OR logic gate
        or_g(a,b)
        
        #d = xor_g(a,b)
        sum = 0.0
        sum = xor_g(d,c) 
        #g = and_g(d,c)
        #e = and_g(a,b)
        out = xor_g(g,e)
        print(sum,out)
        #for 'None' in sum:
            #print("the value is 1 for the sum of none")
        #else:
            #return sum
    bitadder(a,b,c)

    #def bitadderfix(a,b,c):
        
main()
