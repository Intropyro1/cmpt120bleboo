#Attendance



class Attendee:
    def __init__(self,name,company,state,email):
        self.name = name
        self.company = company
        self.state = state
        self.email = email

    def getname(self):
        return self.name
    def getcompany(self):
        return self.company
    def getstate(self):
        return self.state
    def getemail(self):
        return self.email



def storage():
    stor = []
    attendees = open("attendees.txt","r+")
    for line in attendees:
        line = line.split(",")
        A = Attendee(line[0],line[1],line[2],line[3])
        stor.append(A)
    return stor

# JA: It's generlly not a good idea to have the input of the data
# in this class methods.
# JA: What about find and find by state?
def getAttendee():
    name = input("Enter the name of attendee: ")
    company = input("Enter the name of the Company: ")
    state = input("Enter the state of the attendee: ")
    email = input("Enter the email of the attendee: ")
    return Attendee(name,company,state,email)

def printAttendee(attendees):
    name = input("Enter the name of the attendee you want to search for: ")
    for i in attendees:
        if i.getName() == name:
            i.printDetail()

def printNameEmailOfAll(attendees):
    for a in attendees:
        s = str("NAME: "+a.getName()).ljust(25) + str("E-MAIL: "+a.getEmail()).ljust(40)
        print(s)

def printNameEmailOfAllFromAState(attendees):
    state = input("Enter the state to search for attendees: ")
    for a in attendees:
        if a.getState() == state:
            s = str("NAME: "+a.getName()).ljust(25) + str("E-MAIL: "+a.getEmail()).ljust(40)
            print(s)


def deleteAttendee(attendees):
    name = input("Enter the name of the attendee you want to delete: ")
    deleteIndex = []
    for i in range(len(attendees)):
        if attendees[i].getName() == name:
            deleteIndex.append(i)
        for e in deleteIndex:
            attendees.pop(e)
