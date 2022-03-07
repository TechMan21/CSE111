import math
from math import pi
from math import exp

#Finding the Volume of a tire with user input

#  v is the volume in liters,
# π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
# w is the width of the tire in millimeters,
# a is the aspect ratio of the tire, and
# d is the diameter of the wheel in inches.



width = int(input("Please enter the width of the tire (in mm- Ex: 255): " ))
aspect = int(input("Please enter the aspect ratio pf the same tire (Ex: 55): "))
diameter = int(input("Please also enter the diameter of that wheel in inches (Ex: 18): "))

volume = math.pi * (width ** 2) * aspect * (width * aspect + (2540 * diameter))/10000000000
print()
print(f"The volume of the tire is about {volume:.2f} liters.")
print()

#WEEK 2 PROVE ADD-ON AFTER THIS LINE
# interested = input("With the dimensions you have entered, are you interested in buying tires with that size? Yes/No  ")
phone = int(input("Please enter a valid phone number to which we may contact you about the tires we have in stock in that size: (Ex:2085912651) If you do not wish to do so, please enter 0 to skip. "))
# if interested == "Yes" or "yes":
#     phone = int(input("Please enter a valid phone number to which we may contact you about the tires we have in stock in that size: (Ex:2085912651) "))
#     print()
#     print("Thank you for using the tire volume calulator. You will be contacted within the next two bussiness days by one of our representatives. We hope you have a woderful day! ")
    
# else:
#     print("No problem. Thank you for using the tire volume calulator. Have a wonderful day!")
print()
print("Thank you for using the tire volume calulator. If you entered your number you will be contacted within the next two bussiness days by one of our representatives. We hope you have a woderful day! ")

from datetime import datetime


with open("volumes.txt", mode = "at") as tire_volumes:
    current_date = datetime.now()
    print(f"Date: {current_date:%Y-%m-%d}, Width: {width}, Aspect ratio: {aspect}, Diameter of wheel: {diameter}, Volume of tire: {volume:.2f} ", file=tire_volumes)
   
    print(f"Customer phone number:{phone}  ", file=tire_volumes)
