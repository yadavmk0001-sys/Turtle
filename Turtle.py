import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num_sides = 8
side_lenght = 70
angle = 360.0/num_sides

for i in range(num_sides):
    polygon.forward(side_lenght)
    polygon.right(angle)

turtle.done()