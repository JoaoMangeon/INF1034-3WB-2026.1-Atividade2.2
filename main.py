from turtle import *
from time import sleep

t = Turtle()
t.speed(50)

t.pu()
t.goto(-250,125)
t.pd()
t.color("blue")
t.begin_fill()
t.fillcolor("blue")
for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(126)
 t.rt(90)
t.end_fill()

t.pu()
t.goto(-250,-1)
t.pd()
t.color("yellow")
t.begin_fill()
t.fillcolor("yellow")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(126)
 t.rt(90)
t.end_fill()
sleep(2)
t.clear()

t.pu()
t.goto(-250,125)
t.pd()
t.color("black")
t.begin_fill()
t.fillcolor("white")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(84)
 t.rt(90)
t.end_fill()

t.pu()
t.goto(-250,41)
t.pd()
t.color("blue")
t.begin_fill()
t.fillcolor("blue")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(84)
 t.rt(90)
t.end_fill()

t.pu()
t.goto(-250,-43)
t.pd()
t.color("red")
t.begin_fill()
t.fillcolor("red")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(84)
 t.rt(90)
t.end_fill()
sleep(2)
t.clear()

t.pu()
t.goto(-250,125)
t.pd()
t.color("#E05206")
t.begin_fill()
t.fillcolor("#E05206")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(84)
 t.rt(90)
t.end_fill()

t.pu()
t.goto(-250,41)
t.pd()
t.color("black")
t.begin_fill()
t.fillcolor("white")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(84)
 t.rt(90)
t.end_fill()

t.pu()
t.goto(-250,-43)
t.pd()
t.color("#0DB02B")
t.begin_fill()
t.fillcolor("#0DB02B")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(84)
 t.rt(90)
t.end_fill()

t.pu()
t.goto(-50,-30)
t.pd()
t.color("#E05206")
t.begin_fill()
t.fillcolor("#E05206")
t.circle(30)
t.end_fill()
sleep(2)
t.clear()

t.pu()
t.goto(-250,125)
t.pd()
t.color("#00205B")
t.begin_fill()
t.fillcolor("#00205B")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(42)
 t.rt(90)
t.end_fill()

t.pu()
t.goto(-250,83)
t.pd()
t.color("black")
t.begin_fill()
t.fillcolor("white")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(42)
 t.rt(90)
t.end_fill()

t.pu()
t.goto(-250,41)
t.pd()
t.color("#EF3340")
t.begin_fill()
t.fillcolor("#EF3340")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(84)
 t.rt(90)
t.end_fill()

t.pu()
t.goto(-250,-43)
t.pd()
t.color("black")
t.begin_fill()
t.fillcolor("white")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(42)
 t.rt(90)
t.end_fill()

t.pu()
t.goto(-250,-85)
t.pd()
t.color("#00205B")
t.begin_fill()
t.fillcolor("#00205B")

for _ in range(2):
 t.fd(400)
 t.rt(90)
 t.fd(42)
 t.rt(90)
t.end_fill()































mainloop()
