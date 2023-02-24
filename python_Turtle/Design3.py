import math as m
from turtle import*
def heart_a(k):
    return 15*m.sin(k)**3
def heart_b(k):
    return 12*m.cos(k)-5 * \
           m.cos(2*k) - 2 * \
           m.cos(3*k)-\
           m.cos(4*k)
speed(0)
bgcolor("black")
for i in range (6000):
    goto(heart_a(i)*20,heart_b(i)*20)
    for j in range (5):
        color("#f73487")
    goto(0,0)
done()