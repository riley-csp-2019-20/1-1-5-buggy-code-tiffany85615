#   a115_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
#draw ladybug body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
# draw a line to define ladybug wings
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# configure dots
num_dots = 0
dot1position = -20
dot2position = -55
ladybug.pensize(10)

# draw one sets of dots
while (num_dots < 1 ):
  ladybug.penup()
  ladybug.goto(dot1position, dot2position)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(dot1position + 30, dot2position + 20)
  ladybug.pendown()
  ladybug.circle(3)
  num_dots = num_dots + 1

  # position another dot
  dot1position = dot1position
  dot2position = dot2position+30
  num_dots=0
  while (num_dots < 1):
    ladybug.penup()
    ladybug.goto(dot1position, dot2position)
    ladybug.pendown()
    ladybug.circle(3)
    num_dots=num_dots+1



    
  num_dot = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()