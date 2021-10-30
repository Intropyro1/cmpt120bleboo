from graphics import *
import math

def main():
        
    win=GraphWin(width=500,height=400)

    win.setBackground('white')

    
    text=Text(Point(250,100),'Click two points to denote the end points of the line')
   
    text.draw(win)

    
    p1=win.getMouse()
    p2=win.getMouse()

    
    line=Line(p1,p2)
    line.draw(win)

    
    midX=(p1.x+p2.x)/2
    midY=(p1.y+p2.y)/2

    
    dot=Circle(Point(midX,midY),3)
    dot.setFill('cyan')
    dot.draw(win)

    
    dx=abs(p1.x-p2.x)
    dy=abs(p1.y-p2.y)

    
    slope=dy/dx
    length=math.sqrt(dx*dx+dy*dy)

    
    text.setText('Slope: {:.2f}, length: {:.2f}. click anywhere to exit'.format(slope,length))

    
    win.getMouse()

main()

