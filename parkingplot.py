import turtle as tr
import time

t = tr.Turtle()

tr.title("Parking Plot")
tr.bgcolor("red")


t.penup()
t.goto(350, 100)
t.pendown()

#parking 1-5
for i in range(6):
    t.rt(90)
    t.fd(100)
    t.lt(-90)
    t.bk(-100)

    t.bk(-100)
    t.lt(-90)
    t.fd(100)
    t.rt(90)

    t.stamp()
    t.fd(100)

t.fd(500)
t.stamp()
t.fd(100)

t.penup()
t.goto(350, -150)
t.pendown()
t.bk(70)
t.lt(90)
t.fd(90)


time.sleep(6)