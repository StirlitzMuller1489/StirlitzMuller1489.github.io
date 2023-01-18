
#6
s=0
from turtle import *
left(90)
for i in range(1):
    forward(300)
    right(90)
    forward(300)
for i in range(1):
    right(135)
    forward(424)
pu()
for x in range(1,15):
    for y in range(1,15):
        goto(x*20,y*20)
        dot(5)
for z in range(1,14):
    s=s+z
print(s)
done()
