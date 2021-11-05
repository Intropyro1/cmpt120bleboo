#1-Bit adder
#this is a one bit adder taking into account the carry in and carry out and sum outputs
def main():
    a = input("Enter 'A' value(0-1):  ")
    b = input("Enter 'B' value(0-1): ")
    c = input("Enter 'Cin' value(0-1): ")     

    def bitadder(a,b,c):
        #Inputs(a,b,c)
        #a = input("Enter 'A' value(0-1):  ")
        #b = input("Enter 'B' value(0-1): ")
        #cin = input("Enter 'Cin' value(0-1): ")
        #Outputs(sum(a,b),co)
        #
        def xor_g(a,b):
            if a != "1":
                if b == "0":
                    if a == "0" and b == "0":
                        if a or b == "0":
                            return("0")
                        else:
                            return("1")
            if b == "1":
                if a != "0":
                    if a == "1" and b == "1":
                        if a or b == "1":
                            return("0")
                        else:
                            return("1")
            if c == "1":
                if d == "0":
                    if c == "0" and d == "1":
                        if c or d == "0":
                            return("1")
                        else:
                            return("0")
                if c == "0":
                    if d == "1":
                        if c == "1" and d == "0":
                            if c or d == "1":
                                return("1")
                            else:
                                return("0")
                       
                #XOR logic gate
        xor_g(a,b)
        def and_g(a,b):
            if a == "1" and b == "1":
                return("1")
            else:
                return("0")
                #AND logic gate
        and_g(a,b)

        def or_g(a,b):
            if a == "0" or b == "0":
                return("0")
            else:
                return("1")
                #OR logic gate
        or_g(a,b)
        d = xor_g(a,b)
        sum = xor_g(d,c)
        g = and_g(d,c)
        e = and_g(a,b)
        out = xor_g(g,e)
        print(sum,out)
        #for 'None' in sum:
            #print("the value is 1 for the sum of none")
        #else:
            #return sum
    bitadder(a,b,c)
main()
