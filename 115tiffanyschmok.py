print("Hello World!")
#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
#create spider body
spider.circle(20)
#configure spider legs
num_legs = 4
length = 70
space = 140 / num_legs
spider.pensize(5)
#draw spider legs
num_loop = 0
while (num_loop < num_legs):
  spider.goto(0,20)
  spider.setheading(space*num_loop)
  spider.forward(length)
  num_looptwo=0
  while(num_looptwo < num_legs):
    spider.goto(0,20)
  num_loop = num_loop + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()