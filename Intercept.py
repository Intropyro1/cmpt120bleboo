#Intersection of a circle

#program that computes the intersection of a circle with a horizontal line and displays the information textually and graphically.

from graphics import *
import math

def main():
   
      
        h = Graph('Circle intersection',600,300)
        h.setCoords(0,0,24,12)
        h.setBackground('White')
       
       
     
        chart = Rectangle(Point(1,11),Point(11,1))
        chart.setFill('grey')
        chart.draw(h)
       
        Line(Point(6,1),Point(6,11)).draw(h)
        Line(Point(1,6),Point(11,6)).draw(h)
       
     
        for i in range(2,23):
            i = i/2
            Line(Point(0.75,i),Point(1.25,i)).draw(h)
            Line(Point(i,10.75),Point(i,11.25)).draw(h)
       
       

        z = q = 6
       
        for i in range(0,11):
            num = Text(Point(0.5,z),i)
            num.setSize(6)
            num.draw(h)
           
            num2 = Text(Point(z,11.5),i)
            num2.setSize(6)
            num2.draw(h)
           
            num3 = Text(Point(q,11.5),i*-1)
            num3.setSize(6)
            num3.draw(h)
           
            num3 = Text(Point(0.5,q),i*-1)
            num3.setSize(6)
            num3.draw(h)
           
            z = z+0.5
            q = q-0.5

       
     
        intro1 = Text(Point(17.40,10.75),'Program to calculate X value where')
        intro1.setStyle('bold')
        intro1.draw(h)
       
        intro2 = Text(Point(15.8,10),'Y intersection with circle.')
        intro2.setStyle('bold')
        intro2.draw(h)
       
     
        Text(Point(15.75,8.5),'Circle radius (value 0 to 0): ').draw(h)
        inputR = Entry(Point(14,7.5),0)
        inputR.setText('0')
        inputR.draw(h)
       
     
        Text(Point(18,6),'Horizon line intersection (value 10 to -10): ').draw(h)
        inputY = Entry(Point(14,5),10)
        inputY.setText('0')
        inputY.draw(h)
       
  
        Text(Point(14.5,3.5),'X intersection at: ').draw(h)
        Text(Point(12.2,2.70),'+').draw(h)
        Text(Point(12.2,2.25),'-').draw(h)
       
        answerX = Entry(Point(14.5,2.5),10)
        answerX.setText('?')
        answerX.draw(h)
       
           
        Fbutton = Rectangle(Point(19,2),Point(23.5,0.5))
        Fbutton.setFill('green')
        Fbutton.draw(h)
       
        FbuttonT = Text(Point(21.25,1.25),'Find Answer!')
        FbuttonT.draw(h)
       
        h.getMouse()
       
        
        R = eval(inputR.getText())
        Y = eval(inputY.getText())
       
      
        X = math.sqrt(R**2-Y**2)
       
      
        X = round(X,2)

       
        
        answerX.setText(X)
       
      
        R = R/2  
        resultC = Circle(Point(6,6),R)
        resultC.setFill('yellow')
        resultC.draw(h)
       
      
        Line(Point(6,1),Point(6,11)).draw(h)
        Line(Point(1,6),Point(11,6)).draw(h)
       
      
        Y = Y/2+6     
        lineY = Line(Point(1,Y),Point(11,Y))
        lineY.setFill('green')
        lineY.draw(h)
       
   
        X = X/2       
        Xa = X+6      
        Xb = 6-X
       
        resultPa = Circle(Point(Xa,Y),0.1)
        resultPa.setFill('red')
        resultPa.draw(h)
       
        resultPb = Circle(Point(Xb,Y),0.1)
        resultPb.setFill('red')
        resultPb.draw(h)

        FbuttonT.setText('Quit')
               
        exit
        h.getMouse()
        h.close()
   
main()

