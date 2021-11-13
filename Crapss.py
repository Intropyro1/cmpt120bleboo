import random
n = input("Enter the amount of rolls: ")
def roll():
   dice = (random.randrange(1,7) + random.randrange (1,7))
   return dice

def testCraps(n):
    dice = roll()
    total = 0
    count = 0.0
    Counts = float(count)
    return(float(Counts/total)) # This will always fail
testCraps(n)

def loop():
    for i in range (n):
        total = total + 1
    while dice1 != 7 or dice1 != dice:
        if dice == 2 or dice == 3 or dice == 12:
            count = float(count) + 0
            print("player loss")
        elif dice == 7 or dice == 11:
            count = float(count) + 1
        else:
            dice1 = roll()
    while True: # Loop until either lost or won
        if dice1 == 7:
            break # Player lost, don't do anything
        elif dice1 == dice:
            count += 1 # Player won, increase count
            break
        else:
            dice1 = roll()           
                    #return(float(count/total))

