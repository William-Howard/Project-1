#this allows the code to import needed mathematical symbols/equations.
from math import pi

#Using these letters allows one to easily add, subtract, multiply, and divide when needed.
h=int(input("Enter the rectangle height : "))
w=int(input("Enter the rectangle width : "))
r=int(input("Enter the cylinder radius : "))
ch=int(input("Enter the cylinder height : "))
#The beginning of the more complex parts. The math itself isn't hard, due to our imports.
rectangle_area=w*h
rectangle_perimeter=2*(w+h)
cylinder_area=((2*pi*r)*ch)+((pi*r**2)*2)
cylinder_volume=pi *r*r*ch
#Finally we are able to print the results, giving us our output. 
print("Area of a Rectangle : ",rectangle_area)
print("Perimeter of Rectangle : ",rectangle_perimeter)
print("Area of Cylinder : ",cylinder_area)
print("Volume of Cylinder : ",cylinder_volume)
