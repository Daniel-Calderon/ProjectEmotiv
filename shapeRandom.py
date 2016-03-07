from visual import *
import random
def randoColor(shape):
    randomNumber1 = random.randrange(0,256)
    randomNumber2 = random.randrange(0,256)
    randomNumber3 = random.randrange(0,256)
    shape.color= (randomNumber1,randomNumber2,randomNumber3)
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
    #elif randomNumber == 5:
        #shape = helix(pos=(0,0,0), axis=(0,1,1),color =(255,0,0), radius=0.5)
    elif randomNumber == 6:
        shape = pyramid(pos=(0,0,0),axis =(0,.2,.2),color =(0,244,0), size=(2,2,2))
    elif randomNumber == 7:
        shape = ring(pos=(0,0,0), axis=(0,0,1),color =(0,244,0), radius=0.5, thickness=0.1)
    elif randomNumber == 8:
        shape = sphere(pos=(0,0,0),color =(0,244,0), radius=0.5)
    print randomNumber
    return shape
    #randomColor(shape)
    rate(5)
shape = box(pos = (0,0,0),axis = (0,0,1),color = (0,244,0),length =1,width =1, height =1)
for i in range (0,10):
   shape=randomShape(shape)

