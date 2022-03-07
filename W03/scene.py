# Import the functions from the Draw 2-D library
# so that they can be used in this program.
#we are using "Canvas" not turtle
from turtle import clear, color, width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    draw_grid(canvas, scene_width, scene_height, 50)
    # Call your drawing functions such
    # as draw_sky and draw_ground here.


    sky = draw_sky(canvas)
    clouds = draw_clouds(canvas)
    cloud= draw_cloud(canvas)
    mountains = draw_mountains(canvas)
    ground = draw_ground(canvas, scene_width, scene_height)
    
    trees = draw_pine_tree(canvas)
    lake = draw_lake(canvas)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)





# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, width, height, interval, color="black"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color) 

def draw_sky(canvas):
    #darkest part of the sky
    draw_rectangle(canvas, 0, 450, 800, 500,
        width=1, fill="midnightBlue")

    #getting brighter...
    # draw_rectangle(canvas, 0, 400, 800, 450,
    #     width=1, outline="", fill="blue4")
    # draw_rectangle(canvas, 0, 375, 800, 400,
    #     width=1, outline="", fill="skyBlue1")
    draw_rectangle(canvas, 0, 325, 800, 450,
        width=1, outline="midnightBlue", fill="blueViolet")
    draw_rectangle(canvas, 0, 50, 800, 325,
        width=1, outline="", fill="coral1")
        #multiple colors of sky as to a sunset: the highest part of the sky is darkest and the closes to the setting sun in the brightest, and so on.
    
def draw_clouds(canvas):
    draw_oval(canvas, 75, 300, 150, 350, outline="hotPink1", fill="orchid1")
    draw_oval(canvas, 300, 500, 365, 550, outline="hotPink1", fill="orchid1")
   


#This one is for a single cloud using multiple overlaps.
def draw_cloud(canvas): #draw_cloud(canvas, width, height, x_min, x_max, y_min, y_max)
    min_diam= 20
    max_diam= 40
    
    for i in range(40):
        x_start = random.randint(200, 320 ) #(x_min, x_max)
        y_start = random.randint(400, 450) #(y_min, y_max)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x_start, y_start, x_start + diameter, y_start + diameter, outline="", fill="orchid1")
        #left patch of clouds
    for i in range(20):
        x_start = random.randint(500, 720 ) #(x_min, x_max)
        y_start = random.randint(375, 425) #(y_min, y_max)
        diameter = random.randint(min_diam, max_diam)    
        draw_oval(canvas, x_start, y_start, x_start + diameter, y_start + diameter, outline="", fill="orchid1")
        #right patch of clouds
        
#     for i in range(100):
#         x = random.randint(0, scene_width - max_diam)
#         y = random.randint(0, half_height)
#         diameter = random.randint(min_diam, max_diam)
#         draw_oval(canvas, x, y, x + diameter, y + diameter,
#                 fill="mediumOrchid1")
# # your code...

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, 800, 120, width=1,outline="", fill="forestGreen")
    # draw_rectangle(canvas, 0, 450, 800, 500,
    #     width=1, fill="midnightBlue")

def draw_mountains(canvas):
    draw_polygon(canvas, 580, 110, 710, 110, 640, 248, width=1, outline="lightCyan4", fill="lightCyan4")
    draw_polygon(canvas, 635, 110, 735, 110, 675, 265, width=1,outline="lightCyan4", fill="lightCyan4")
    #^^ right pair
    draw_polygon(canvas, 120, 110, 240, 110, 205, 270, width=1,outline="lightCyan4", fill="lightCyan4")
    draw_polygon(canvas, 200, 110, 285, 110, 235, 258, width=1,outline="lightCyan4", fill="lightCyan4")
    draw_polygon(canvas, 230, 110, 310, 110, 265, 280, width=1,outline="lightCyan4", fill="lightCyan4")
                        #Left-x,left-y,right-x,right-y,top-x,top-y 

def draw_lake(canvas):
    draw_oval(canvas, 210, 80, 500, -30, width=1, outline="blue3", fill="dodgerBlue2")

def draw_pine_tree(canvas):
    draw_rectangle(canvas, 70, 28, 85, 80, width=1, outline="tan4", fill="tan3")
    draw_polygon(canvas, 50, 50, 110, 50, 80, 150, width=1, outline="", fill="darkGreen")
    #far left tree ^^
    draw_rectangle(canvas, 150, 38, 160, 90, width=1, outline="tan4", fill="tan3")
    draw_polygon(canvas, 125, 60, 185, 60, 155, 150, width=1, outline="", fill="darkGreen")
    #^^ to the right of the left tree
    draw_rectangle(canvas, 170, 48, 185, 100, width=1, outline="tan4", fill="tan3")
    draw_polygon(canvas, 150, 70, 210, 70, 180, 190, width=1, outline="", fill="darkGreen")
    #tall of pair under left mountains
   
    draw_rectangle(canvas, 370, 85, 385, 140, width=1, outline="tan4", fill="tan3")
    draw_polygon(canvas, 350, 100, 410, 100, 380, 200, width=1, outline="", fill="darkGreen")
    #above lake

    draw_rectangle(canvas, 570, 85, 585, 140, width=1, outline="tan4", fill="tan3")
    draw_polygon(canvas, 550, 100, 610, 100, 580, 200, width=1, outline="", fill="darkGreen")
    #left of right mountain

    draw_rectangle(canvas, 470, 55, 485, 110, width=1, outline="tan4", fill="tan3")
    draw_polygon(canvas, 450, 70, 510, 70, 480, 170, width=1, outline="", fill="darkGreen")
    #to the right and above lake

    draw_rectangle(canvas, 520, 25, 535, 90, width=1, outline="tan4", fill="tan3")
    draw_polygon(canvas, 500, 50, 560, 50, 530, 150, width=1, outline="", fill="darkGreen")
    #bottom right of lake

    draw_rectangle(canvas, 670, 28, 685, 80, width=1, outline="tan4", fill="tan3")
    draw_polygon(canvas, 650, 50, 710, 50, 680, 150, width=1, outline="", fill="darkGreen")
    #far right low
    draw_rectangle(canvas, 700, 88, 715, 140, width=1, outline="tan4", fill="tan3")
    draw_polygon(canvas, 680, 110, 745, 110, 710, 210, width=1, outline="", fill="darkGreen")
    #far right high


# Call the main function so that
# this program will start executing.
main()