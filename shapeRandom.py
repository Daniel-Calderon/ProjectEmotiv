from visual import *
import random
def randoColor(shape):
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
    return shape
    rate(5)
shape = box(pos = (0,0,0),axis = (0,0,1),color = (0,244,0),length =1,width =1, height =1)
while True:
    shape.visible = false
    shape=randomShape(shape)
    shape = randoColor(shape)
    rate(5)
