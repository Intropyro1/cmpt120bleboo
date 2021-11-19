#Shuffle

from random import *

def main():

    mylist = [3,4,4,57,453,42,424,556,455,344,2,9]

    def shuffle(mylist):
        newlist = mylist
        for i in range(len(mylist)):
            move = randrange(0, len(mylist))
            newlist.append(mylist[move])
            mylist.pop(move)
        return newlist

    print(shuffle(mylist))

main()
