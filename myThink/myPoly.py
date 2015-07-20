from swampy.TurtleWorld import *
import math
world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.01

def square(t, length):
    fd(t, length)
    lt(t)
    fd(t, length)
    lt(t)
    fd(t, length)
    lt(t)
    fd(t, length)

def polygon(t, length, n):
    angle = 360/ n
    for i in range(n):
        fd(t, length)
        lt(t, angle)
    
def circle(t, r):
    circumference = math.pi * 2 * r
    n = 12
    angle = 360/ n
    length = int(circumference / n)
    polygon(t, length, n)
        
def arc(t, r, angle):
    circumference = math.pi * 2 * r
    n = 12			#n of polygon sides approaching arc
    partial_arc_angle = (angle/ 360) / n
    length = int((circumference * angle / 360) / partial_arc_angle)
    polygon(t, length, n)
    
arc(bob, 200.0, 100)

wait_for_user()
