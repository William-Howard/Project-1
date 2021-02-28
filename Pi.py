from math import pi

h=int(input("Enter the rectangle height : "))
w=int(input("Enter the rectangle width : "))
r=int(input("Enter the cylinder radius : "))
ch=int(input("Enter the cylinder height : "))
rectangle_area=w*h
rectangle_perimeter=2*(w+h)
cylinder_area=((2*pi*r)*ch)+((pi*r**2)*2)
cylinder_volume=pi *r*r*ch
print("Area of a Rectangle : ",rectangle_area)
print("Perimeter of Rectangle : ",rectangle_perimeter)
print("Area of Cylinder : ",cylinder_area)
print("Volume of Cylinder : ",cylinder_volume)
