from visual import *
import math
from visual.controls import *
import random
array = [5129.230769,5808.205128,7804.102564,5249.74359,3983.589744,6991.794872,1689.230769,6770.25641,5193.333333,4081.538462,2437.948718,7184.615385,130.7692308,6263.589744]
def randomDimension(number,shape):
    randomNumber = random.randrange(1,14)
    randomNumber1 = random.randrange(1,14)
    randomNumber2 = random.randrange(1,14)
    if(number == 1):
        shape.size = (array[randomNumber],array[randomNumber1],array[randomNumber2])
    elif number == 2:
        shape.radius = array[randomNumber1]
    elif number == 3:
        shape.radius = array[randomNumber1]
    elif number == 4:
        shape.size = (array[randomNumber1],array[randomNumber2],array[randomNumber])
    elif number == 5:
        shape.radius = array[randomNumber]
    elif number == 6:
        shape.size = (array[randomNumber],array[randomNumber1],array[randomNumber2])
    elif number == 7:
        shape.radius = array[randomNumber]
        shape.thickness = array[randomNumber1]
    elif number == 8:
        shape.radius = array[randomNumber]
    return shape     
def randomColor(shape):
    randomNumber1 = random.randrange(0,2)
    randomNumber2 = random.randrange(0,2)
    randomNumber3 = random.randrange(0,2)
    if(randomNumber3==0 and randomNumber2==0 and randomNumber1==0):
        print shape.color
        randonNumber1=1
        randomNumber3=1
    shape.color= (randomNumber1,randomNumber2,randomNumber3)
    return shape
def randomShape(shape):
    randomNumber = random.randrange(1,9)   
    if randomNumber == 1:
        shape = box(pos = (0,0,0),axis = (0,0,1),color =(0,244,0),length =1,width =1, height =1)
    elif randomNumber == 2:
        shape =cone(pos=(0,0,0),color =(0,244,0), axis=(0,1,1),radius=1)
    elif randomNumber == 3:
        shape = cylinder(pos=(0,0,0),color =(0,244,0), axis=(0,1,1), radius=1)
    elif randomNumber == 4:
        shape = ellipsoid(pos=(0,0,0),color =(0,244,0),length=1, height=1, width=1)
    elif randomNumber == 5:
        shape = helix(pos=(0,0,0), axis=(0,1,1),color =(255,0,0), radius=0.5)
    elif randomNumber == 6:
        shape = pyramid(pos=(0,0,0),axis =(0,.2,.2),color =(0,244,0), size=(2,2,2))
    elif randomNumber == 7:
        shape = ring(pos=(0,0,0), axis=(0,0,1),color =(0,244,0), radius=0.5, thickness=0.1)
    elif randomNumber == 8:
        shape = sphere(pos=(0,0,0),color =(0,244,0), radius=0.5)
    return shape,randomNumber
    rate(5)

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
number1 = 0
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
    
    ball4.pos=vector(sin(x)*number1*2,cos(y)*number1*2,0) #circle around object
    ball4.radius = number1 /10
    ball5.pos=vector(sin(x)*1.1,cos(y)*1.1,0)#increase .1
    ball10.pos=vector(sin(x)*1.2,cos(y)*1.2,0)#increase .2
    ball6.pos=vector(sin(x)*0.9,cos(y)*0.9,0)#decrease .1
    ball7.pos=vector(sin(x)*0.8,cos(y)*0.9,0)#decrease .2
    #ball5.pos=vector((1.1)*sin(x),(1.1)*cos(y),0)
    if scene.mouse.clicked:
        ball2.visible = false
        ball2,number = randomShape(ball2)
        number1 = array[number]
        m = scene.mouse.getclick()
        loc = m.pos
        print(loc)
    ball2 = randomColor(ball2)
    ball2 = randomDimension(number,ball2)
    rate(5)

     
    
