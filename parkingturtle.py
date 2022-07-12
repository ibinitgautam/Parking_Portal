import turtle as tr
import time

t = tr.Turtle()
tr.title("Parking Map")
tr.bgcolor("red")

t.begin_fill()
#down-left
for i in range(3):
    t.rt(90)
    t.fd(90)
    t.lt(-90)
    t.bk(-90)

    #up-right
    t.lt(-90)
    t.bk(-90)
    t.rt(90)
    t.fd(90)

    t.stamp()

    t.fd(100)

#t.circle(70)

t.end_fill()

time.sleep(6)