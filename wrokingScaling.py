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
        #if randomNumber > 6000:
  #          radomNumber = 6000;
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
ball4 = sphere(pos=(1,1,1), radius=0.11 ,make_trail=True, trail_type="points",interval=2, retain=10)
ball5 = sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",interval=2, retain=10)
ball6 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",interval=2, retain=10)
ball7 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",interval=2, retain=10)
ball8 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",interval=2, retain=10)
ball9 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",interval=2, retain=10)
ball10 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",interval=2, retain=10)
ball11 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",interval=2, retain=10)
ball12 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",interval=2, retain=10)
ball13 =sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",interval=2, retain=10)
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
    #***********Ball 1***********************************************
    ball.pos= vector(sin(x)*number1,sin(x)*number1,cos(z)*number1) #pi*1/4
    ball.radius = number1/7
    ball = randomColor(ball)
    ball.trail_object.color = ball2.color
    #***********Ball 2***********************************************
    ball9.pos=vector(cos(x)*number1,-cos(x),sin(x)*number1)#pi*3/4
    ball9.radius = number1/7
    ball9 = randomColor(ball9)
    ball9.trail_object.color=ball2.color
    #***********Ball 3***********************************************
    ball3.pos=vector(0,1.2*cos(y)*number1,1.2*sin(z)*number1) #y axis
    ball3.radius = number1/7
    ball3 = randomColor(ball3)
    ball3.trail_object.color = ball2.color
    #/ball7.pos=vector(0.1,cos(y),sin(z))
    #***********Ball 4***********************************************
    ball8.pos=vector(1.2*sin(x)*number1,0,1.2*cos(z)*number1)#zero on x axis
    ball8.radius = number1/7
    ball8 = randomColor(ball8)
    ball8.trail_object.color = ball2.color
    #***********Ball 5***********************************************
    ball4.pos=vector(sin(x)*number1*2,cos(y)*number1*2,0) #circle around object
    ball4.radius = number1/7
    ball4 = randomColor(ball4)
    ball4.trail_object.color = ball2.color
    #***********Ball 6***********************************************
    ball5.pos=vector(sin(x)*1.1,cos(y)*1.1,0)#increase .1
    ball5.radius = number1/7
    ball5 = randomColor(ball5)
    ball5.trail_object.color = ball2.color
    #***********Ball 7***********************************************
    ball10.pos=vector(sin(x)*1.2,cos(y)*1.2,0)#increase .2
    ball10.radius = number1/7
    ball10 = randomColor(ball10)
    ball10.trail_object.color = ball2.color
    #***********Ball 8***********************************************
    ball6.pos=vector(sin(x)*0.9,cos(y)*0.9,0)#decrease .1
    ball6.radius = number1/7
    ball6 = randomColor(ball6)
    ball6.trail_object.color = ball2.color
    #***********Ball 9***********************************************
    ball7.pos=vector(sin(x)*0.8,cos(y)*0.9,0)#decrease .2
    ball7.radius = number1/7
    ball7 = randomColor(ball7)
    ball7.trail_object.color = ball2.color
    #/ball5.pos=vector((1.1)*sin(x),(1.1)*cos(y),0)
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

     
    
