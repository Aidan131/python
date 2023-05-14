import turtle
import random
from time import sleep
#sceen
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("white")
screen.title("貪吃蛇")

#gamearea
t0=turtle.Turtle()
size=360
t0.hideturtle()
t0.speed(0)
t0.penup()
t0.goto(size,size)
t0.pendown()
for i in range(4):
    t0.right(90)
    t0.forward(size*2)


food=turtle.Turtle()
food.shape("circle")
food.speed(0)
food.color("red")
food.penup()
x = random.randint(-180, -180)
y = random.randint(-180, 180)
food.goto(x, y)
    
#main character setting
t=turtle.Turtle()
speed = 1
t.shape('turtle')
t.speed(speed)
t.penup()

#main character movement
def t_up():
   t.setheading(90)
def t_down():
    t.setheading(270)
def t_right(): 
    t.setheading(180)
def t_left():
    t.setheading(0)
    
screen.onkey(t_up,"w")
screen.onkey(t_down,"s")
screen.onkey(t_left,"d")
screen.onkey(t_right,"a")
screen.listen()

score1 = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 180)
pen.write("Score1:" + str(score1),
          align="center",
          font=("Courier", 14, "normal"))

pen2 = turtle.Turtle()
pen.speed(0)
pen2.color("black")
pen2.hideturtle()
pen2.goto(0,0)

timer = 0

i=100
while i>10:
    t.forward(10)
    screen.update()
    xcor = t.xcor()
    ycor = t.ycor()
        # Turtle 1 hit food
    if xcor >= 360 or xcor <= -360:
        pen2.write("you lost",        
                  align="center",
                  font=("Courier", 20, "normal")) 
        sleep(1)
        turtle.bye()
    if ycor >= 360 or ycor <= -360:
        pen2.write("you lost",
                  align="center",
                  font=("Courier", 20, "normal"))
        sleep(1)
        turtle.bye()
    if score1 == 10 :
         pen2.write("you won",
                  align="center",
                  font=("Courier", 20, "normal"))
         sleep(1)
         turtle.bye()
         
    if t.distance(food) <= 20:
        score1 = score1 + 1
        pen.clear()
        pen.write("Score1:" + str(score1),
                  align="center",
                  font=("Courier", 14, "normal"))
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)
        food.goto(x, y)
        speed=speed+1
        t.speed(speed)
        sleep(0.1)
    if xcor == 360 or xcor == -360:
        pen2.write("you lost",        
                  align="center",
                  font=("Courier", 20, "normal")) 
        sleep(1)
        turtle.bye()
    if ycor == 360 or ycor == -360:
        pen2.write("you lost",
                  align="center",
                  font=("Courier", 20, "normal"))
        sleep(1)
        turtle.bye()
    if score1 == 10 :
         pen2.write("you won",
                  align="center",
                  font=("Courier", 20, "normal"))
         sleep(1)
         turtle.bye()
         
    
    
        
        
        



screen.mainloop()













