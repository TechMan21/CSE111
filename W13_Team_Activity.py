
import math

shape = True
print('What shape do you want to find the area of? ')
def main():  
    shape = input('Please enter Square, Rectangle, Circle, or Quit ')
    while shape != True:
        if shape.lower() == 'square':
            length_of_square = float(input('What is the length of a side of the square? '))
            area_of_square = compute_area_square(length_of_square)
            print(f'The area of this square is {area_of_square:.2f}.')

        elif shape.lower == 'rectangle':
            length_of_rectangle = float(input('What is the length of a side of the rectangle? '))
            width_of_rectangle = float(input('What is the width of a side of the rectangle? '))
            area_of_rectangle = compute_area_rectangle(length_of_rectangle, width_of_rectangle)
            print(f'The area of this rectangle is {area_of_rectangle:.2f}.')

        elif shape.lower == 'circle':
            radius_of_circle = float(input('What is the radius of the circle? '))
            area_of_circle = compute_area_circle(radius_of_circle)
            print(f'The area of this circle is {area_of_circle:.2f}.')

        elif shape.lower() == 'quit':
            print = input('Press ENTER to exit. ')
            shape = False

#area of square
def compute_area_square(side):
    return side * side
#Area of a rectangle:
def compute_area_rectangle(length, width):
    return length * width
#Area of circle:
def compute_area_circle(radius):
    return math.pi * (radius**2)

while shape == True:
    main()