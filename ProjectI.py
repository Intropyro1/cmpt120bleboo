#Project 2.py

from graphics import *
from button import *

def draw_and(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    # Outline
    Line(Point(x1,y1),Point(x1,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    # Connectors
    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

def draw_or(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    # Outline
    Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    # Connectors
    Line(Point(x1,y3),Point(x-2,y3)).draw(win)
    Line(Point(x1,y4),Point(x-2,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

def draw_not(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    x3 = x2 + 15
    
    Polygon(Point(x1,y1), Point(x1,y2), Point(x2,y)).draw(win)
    Circle(Point(x3,y), 10).draw(win)
    #Connectors
    Line(Point(x1,y),Point(x1-10,y)).draw(win)
    Line(Point(x3+10,y),Point(x3+20,y)).draw(win)

def draw_xor(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    #Outline
    bodyArc = Arc(Point(x1-15,y1),Point((x1+size/2)-15,y2)).draw(win)
    secondArc = Arc(Point(x1-25,y1),Point((x1+size/2)-20,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x2-15,y1),Point((x2+size/2)-15,y2)).draw(win)
    #Connectors
    Line(Point(x1-12,y3),Point(x1+12,y3)).draw(win)
    Line(Point(x1-12,y4),Point(x1+12,y4)).draw(win)
    Line(Point((x+size)-15,y),Point(x+size+10,y)).draw(win)
   
def draw_nand(x, y, size, win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    # Outline
    Line(Point(x1,y1),Point(x1,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    Circle(Point(x+size+10,y), 10).draw(win)
    # Connectors
    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Line(Point(x+size+20,y),Point(x+size+30,y)).draw(win)


def main():
    #Create Window and Draw Buttons
    win = GraphWin("Logic Board", 600, 600)
    #win.set.coords(

    andButton = Button(win, Point(120,50), 50, 25, "AND")
    andButton.activate()

    orButton = Button(win, Point(125,100), 50, 25, "OR")
    orButton.activate()

    notButton = Button(win, Point(130,150), 50, 25, "NOT")
    notButton.activate()

    xorButton = Button(win, Point(135,200), 50, 25, "XOR")
    xorButton.activate()

    nandButton = Button(win, Point(140,250), 50, 25, "NAND")
    nandButton.activate()

    pt = win.getMouse()
    while True:
        #Event Loop
        if andButton.clicked(pt):
            drawPoint = win.getMouse()

            x = drawPoint.getX()
            y = drawPoint.getY()
           
            draw_and(x,y,50,win)

        pt = win.getMouse()

        if orButton.clicked(pt):
            drawPoint = win.getMouse()

            x = drawPoint.getX()
            y = drawPoint.getY()

            draw_or(x,y,50,win)

        elif notButton.clicked(pt):
            drawPoint = win.getMouse()

            x = drawPoint.getX()
            y = drawPoint.getY()

            draw_not(x,y,50,win)

        elif xorButton.clicked(pt):
            drawPoint = win.getMouse()

            x = drawPoint.getX()
            y = drawPoint.getY()

            draw_xor(x,y,60,win)

        elif nandButton.clicked(pt):
            drawPoint = win.getMouse()

            x = drawPoint.getX()
            y = drawPoint.getY()

            draw_nand(x,y,50,win)

       
main()
