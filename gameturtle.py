import turtle as tr
import time
import random

t = tr.Turtle()
c = t.clone()
l = c.clone()
tr.title("BINIT")

#finish line
l.penup()
l.goto(200, 70)
l.pendown()
l.rt(200)
l.goto(200, -70)
l.color("white")

#turtle 1
tr.bgcolor("red")
t.penup()
t.goto(-350, 40)
t.color("white")
t.shape("turtle")
t.pensize(10)

#turtle 2
c.penup()
c.goto(-350, -40)
c.color("blue")
c.shape("turtle")
c.pensize(10)


i = 19
while(i > 1):
    t.fd(i*random.randint(1, 6))
    t.speed(2)
    c.fd(i*random.randint(1, 6))
    c.speed(2)

    i -= 1

time.sleep(2)