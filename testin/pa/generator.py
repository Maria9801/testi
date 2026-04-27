import turtle

window = turtle.Screen()

turtle.up()
turtle.forward(0)
cell_size = 50

def cross(x, y):
  turtle.pensize(3)
  turtle.color('red')
  turtle.up()
  turtle.goto(x, y)
  turtle.setheading(0)
  turtle.down()
  turtle.left(45)
  for i in range(4):
    turtle.forward(50)
    turtle.back(50)
    turtle.left(90)
  turtle.setheading(0)

window.onclick(cross, 1)
turtle.done()