#List_func


myList = [1,3,4,8,0,9]
newList = []

#for i in range(0,len(myList)):
   # myList = [int(i)for i in myList]
    #print ("progress : " + str(myList))
    #newList.append(int(myList[i]))
print ("New list: " + str(newList))
    






def count(myList, x):
    c = 0
    for i in range(len(myList)):
        if x == myList[1]:
            c += 1
        return c



def isin(myList, x):
    for i in range(len(myList)):
        if x == myList[i]:
            return True
        return False



def index(myList, x):
    for i in range(len(myList)):
        if x == myList[i]:
            return 1
        return -1


def reverse(myList):
    r = []
    for i in range(len(myList)-1,-1,-1):
        r.append(myList[i])
    return r


def sort(myList):
    newList = []
    myList = [int(i)for i in myList]
    for i in range(0,len(myList)):
        if myList[i] <= myList[i]:
            newList.append(int(myList[i]))
            newList.pop(i)
            return newList.append(int(myList[i]))
        return newList.append(sort(myList))
    print("list" + str(newList))

    
    
