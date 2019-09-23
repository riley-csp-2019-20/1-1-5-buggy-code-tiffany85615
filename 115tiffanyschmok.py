print("Hello World!")
#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
#create spider body
spider.circle(20)
#configure spider legs
num_legs = 8
length = 70
space = 10000 / num_legs
spider.pensize(5)
#draw spider legs
num_loop = 0
while (num_loop < num_legs):
  spider.goto(0,20)
  spider.setheading(space*num_loop)
  spider.forward(length)
  num_loop = num_loop + 1
spider.penup()
spider.goto(-18,-16)
spider.pendown()
spider.pensize(20)

spider.circle(10)
#draw spider eyes
spider.pensize(4)
spider.pencolor("white")
spider.penup()
spider.goto(-33,-15)
spider.pendown()
spider.circle(2)
spider.penup()
spider.goto(-22,-19)
spider.pendown()
spider.color("white")
spider.circle(2)
#draw pupils for eyes
spider.pensize(4)
spider.color("black")
spider.circle(1)
spider.penup()
spider.goto(-33,-15)
spider.pendown()
spider.circle(1)
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()