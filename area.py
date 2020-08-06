#First task
#program to find area of circle using functions
import math

#Function that calculates area of circle
def area_of_circle(r): 
    a = r**2 * math.pi
    return a

r = float(input("Enter the radius of the circle: "))
print("%.2f" %area_of_circle(r))
print("--------------------------------------------------------------------------------------")

#second task
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
