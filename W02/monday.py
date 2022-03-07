import math

def compute_circle_area(radius):
    return radius**2* math.pi

print(compute_circle_area(5))

#if want to round the decimal places, different ways are: 'f".....":.2f' 
# or 'ronud(#,dec places #)'
# ex: print(round(compute_circle_area(5),2)) or ....

