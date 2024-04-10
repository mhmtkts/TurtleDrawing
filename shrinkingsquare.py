import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("red")

def shrinkinSqaure(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5


shrinkinSqaure(200)
shrinkinSqaure(180)
shrinkinSqaure(160)
shrinkinSqaure(140)
shrinkinSqaure(120)
shrinkinSqaure(100)
shrinkinSqaure(80)
shrinkinSqaure(60)
shrinkinSqaure(40)
shrinkinSqaure(20)


turtle.done()