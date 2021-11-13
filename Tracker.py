#Tracker + projectile
from graphics import *
from Projectile import *
from time import *

class Tracker:
    def __init__(self, window, objToTrack,update):
        self.xpos = 10.0
        self.ypos = 10.0
    def window(self): #create window
        window = GraphWin('Tracker',400,400)
        return window
    # window is a graphWin and objToTrack is an object whose position is to be shown in the window. objToTrack must be
    # an object that has getX() and getY() methods that report its current position.
    def objToTrack(self):
        Tracker = Circle(Point(self.xpos,self.ypos),25)
        window = GraphWin('Tracker',400,400)
        Tracker.draw(window)
    def getX(self):
        self.xpos1 = Projectile.getX(self)
        self.xpos = self.xpos1
        return self.xpos
            
    def getY(self):
        self.ypos1 = Projectile.getY(self)
        self.ypos = self.ypos1
        return self.ypos
    
    # Creates a Tracker object and draws a circle in window at the
    # current position of objToTrack.

    def update(self):
    # Moves the circle in the window to the current position of the
    # object being tracked.
        Tracker = Circle(Point(self.xpos,self.ypos),25)
        Tracker.move(Point(Projectile.update(self.xpos,time),Projectile.update(self.ypos,time)))
        Projectile.update()
        return Tracker.draw(window)




#def main():
    #create window
    #win = GraphWin('Projectile+tracker',400,400)
    #object(Projectile())
    
