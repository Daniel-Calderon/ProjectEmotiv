from visual import *
import math

ball = sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
#scene1=display(width=300,height=300)
ball3 = sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
ball2 = sphere(pos=(0,0,0), radius=1)
ball4 = sphere(pos=(1,1,1), radius=0.11 ,make_trail=True, trail_type="points",
              interval=10, retain=50)
ball5 = sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
ball6 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
ball7 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
ball8 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
ball9 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
ball10 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
ball11 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
ball12 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
ball13 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
x=1
y=1
z=1
while 1:
    x=x+1
    y=y+1
    z=z+1
    rate(20)
   # ball.rotate(angle=pi/4, axis=axis, origin=pos)
    ball.rotate(angle=120)
    ball.pos= vector(sin(x),sin(x),cos(z)) #pi*1/4
    
    ball9.pos=vector(cos(x),-cos(x),sin(x))#pi*3/4
   
   
    
    ball3.pos=vector(0,1.2*cos(y),1.2*sin(z)) #y axis

    
    #ball7.pos=vector(0.1,cos(y),sin(z))
   
    ball8.pos=vector(1.2*sin(x),0,1.2*cos(z))#zero on x axis
    
    ball4.pos=vector(sin(x),cos(y),0)#circle around object
    ball5.pos=vector(sin(x)*1.1,cos(y)*1.1,0)#increase .1
    ball10.pos=vector(sin(x)*1.2,cos(y)*1.2,0)#increase .2
    ball6.pos=vector(sin(x)*0.9,cos(y)*0.9,0)#decrease .1
    ball7.pos=vector(sin(x)*0.8,cos(y)*0.9,0)#decrease .2
    #ball5.pos=vector((1.1)*sin(x),(1.1)*cos(y),0)
    
    
     
    
