#gate_classes.py


from randrange import *
from graphics import *
from logic_gates_mod import *
from ProjectI import *

class DigitalValue:

    def __init__(self,p,value):

        self.p = Point
        self.value == 0
#I set value equal to 0 but it can be modified

    def getValue(self):

        return self.value

    def setValue(self,value):

        self.value = 0+value

    def draw(self,win,type):

        self.win = GraphWin("object",300,300)
        I = Entry(self.p,10)
        O = Text(self.p,10)

        if self.type == "I":
            I.draw(win)

        else:
            O.draw(win)

#draws text or entry depending on the value of parameter (type)

class And:
    def __init__(self,p,a,b):
        self.p = Point
        self.a == a
        self.b == b
        # The output DigitalValue should be stored also

    def setA(self):
        self.a = and_g(a)

    def setB(self):
        self.b = and_g(b)

    def getOutput(self):
        return DigitalValue()

    def draw(self,win):
        
        self.win = GraphWin("andgate",500,500)
        draw_and(50,50,60,win)
        
        



class Or:
    def __init__(self,p,a,b):
        self.p = Point
        self.a == a
        self.b == b

    def setA(self):
        self.a = or_g(a)

    def setB(self):
        self.b = or_g(b)

    def getOutput(self):
        return DigitalValue()

    def draw(self,win):
        
        self.win = GraphWin("orgate",500,500)
        draw_or(50,150,60,win)   

    
        




class Not:
    def __init__(self,p,a,b):
        self.p = Point
        self.a == a
        self.b == b

    def setA(self):
        self.a = not_g(a)

    def setB(self):
        self.b = not_g(b)

    def getOutput(self):
        return DigitalValue()

    def draw(self,win):
        
        self.win = GraphWin("notgate",500,500)
        draw_not(50,250,60,win)
    
        



class Xor:
    def __init__(self,p,a,b):
        self.p = Point
        self.a == a
        self.b == b

    def setA(self):
        self.a = xor_g(a)

    def setB(self):
        self.b = xor_g(b)

    def getOutput(self):
        return DigitalValue()

    def draw(self,win):
        
        self.win = GraphWin("xorgate",500,500)
        draw_xor(50,350,60,win)



class Nand:
    def __init__(self,p,a,b):
        self.p = Point
        self.a == a
        self.b == b

    def setA(self):
        self.a = nand_g(a)

    def setB(self):
        self.b = nand_g(b)

    def getOutput(self):
        return DigitalValue()

    def draw(self,win):
        
        self.win = GraphWin("nandgate",500,500)
        draw_nand(50,450,60,win)



class Connection:

    def __init__(self,frome,to):

        self.frome = frome
        self.to = to

    def getFrom(self):
        return DigitalValue()

    def getTo(self):
        return DigitalValue()
