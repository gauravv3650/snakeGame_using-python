from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle") # set the shape of the turtle to circle
        self.penup() # lift the pen so that nothing is drawn
        self.shapesize(stretch_len= 0.5, stretch_wid=0.5) # stretch the size of the circle
        self.color("yellow") # set the color of the circle to yellow
        self.speed("fastest") # set the speed of the turtle to the fastest

    def refresh(self):
        random_x = random.randint(-280, 280) # generate a random x-coordinate within the screen boundaries
        random_y = random.randint(-280, 280) # generate a random y-coordinate within the screen boundaries
        self.goto(random_x, random_y) # move the turtle to the random position



#The Food class inherits from the Turtle class, which is part of the turtle module. The random module is also imported to generate 
#random coordinates for the food turtle. The __init__ method initializes the food turtle with a circle shape, yellow color, 
#and stretched size. The refresh method generates random coordinates within the screen boundaries and moves the food turtle to 
#that position.