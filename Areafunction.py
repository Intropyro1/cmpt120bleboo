#Area function
#this program returns the sphereArea(radius) and sphereVolume(radius) with a given radius



#import pi from math package
from math import pi

#defination for area of sphere
def sphere_area(r):
    return (4*pi*r*r)

#defination for volume of sphere
def sphere_volume(r):
    return((4/3)*pi*r*r*r)

#Getting the radius from user
r=float(input("Enter the radius of spehere: "))
#calling the both function and getting the return value in variable area and spehere
area=sphere_area(r)
volume=sphere_volume(r)

#Displaying the area and volume
print("Area of the sphere is : ",area)
print("Volume of the sphere is : ",volume)
