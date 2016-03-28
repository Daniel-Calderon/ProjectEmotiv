# python version >= 2.5
import sys,os
import time
import ctypes
from visual import *
import math
from visual.controls import *
import random
 
from ctypes import cdll
from ctypes import CDLL
from ctypes import c_int
from ctypes import c_uint
from ctypes import pointer
from ctypes import c_char_p
from ctypes import c_float
from ctypes import c_double
from ctypes import byref
arr=[]
try :
    if sys.platform.startswith('win32'):     
        libEDK = cdll.LoadLibrary("edk.dll")
    if sys.platform.startswith('linux'):
        srcDir = os.getcwd()    
        libPath = srcDir + "/libedk.so.1.0.0"        
        libEDK = CDLL(libPath)
except :
    print 'Error : cannot load dll lib' 

ED_COUNTER = 0
ED_INTERPOLATED=1
ED_RAW_CQ=2
ED_AF3=3
ED_F7=4
ED_F3=5
ED_FC5=6
ED_T7=7
ED_P7=8
ED_O1=9
ED_O2=10
ED_P8=11
ED_T8=12
ED_FC6=13
ED_F4=14
ED_F8=15
ED_AF4=16
ED_GYROX=17
ED_GYROY=18
ED_TIMESTAMP=19
ED_ES_TIMESTAMP=20
ED_FUNC_ID=21
ED_FUNC_VALUE=22
ED_MARKER=23
ED_SYNC_SIGNAL=24

targetChannelList = [ED_COUNTER,ED_AF3, ED_F7, ED_F3, ED_FC5, ED_T7,ED_P7, ED_O1, ED_O2, ED_P8, ED_T8,ED_FC6, ED_F4, ED_F8, ED_AF4, ED_GYROX, ED_GYROY, ED_TIMESTAMP, ED_FUNC_ID, ED_FUNC_VALUE, ED_MARKER, ED_SYNC_SIGNAL]
header = ['COUNTER','AF3','F7','F3', 'FC5', 'T7', 'P7', 'O1', 'O2','P8', 'T8', 'FC6', 'F4','F8', 'AF4','GYROX', 'GYROY', 'TIMESTAMP','FUNC_ID', 'FUNC_VALUE', 'MARKER', 'SYNC_SIGNAL']
write = sys.stdout.write
eEvent      = libEDK.EE_EmoEngineEventCreate()
eState      = libEDK.EE_EmoStateCreate()
userID            = c_uint(0)
nSamples   = c_uint(0)
nSam       = c_uint(0)
nSamplesTaken  = pointer(nSamples)
#da = zeros(128,double)
data     = pointer(c_double(0))
user                    = pointer(userID)
composerPort          = c_uint(1726)
secs      = c_float(1)
datarate    = c_uint(0)
readytocollect    = False
option      = c_int(0)
state     = c_int(0)

input=''
print "==================================================================="
print "Example to show how to log EEG Data from EmoEngine/EmoComposer."
print "==================================================================="
print "Press '1' to start and connect to the EmoEngine                    "
print "Press '2' to connect to the EmoComposer                            "
print ">> "
#------------------------------------------------------------------------------------------------------------------------------------------------------------
option = int(raw_input())


if option == 1:
    print libEDK.EE_EngineConnect("Emotiv Systems-5")
    if libEDK.EE_EngineConnect("Emotiv Systems-5") != 0:
        print "Emotiv Engine start up failed."
elif option == 2:
    if libEDK.EE_EngineRemoteConnect("127.0.0.1", composerPort) != 0:
        print "Cannot connect to EmoComposer on"
else :
    print "option = ?"
    
print "Start receiving EEG Data! Press any key to stop logging...\n"

    
hData = libEDK.EE_DataCreate()
libEDK.EE_DataSetBufferSizeInSec(secs)
print "Buffer size in secs:"
array = [5129.230769,5808.205128,7804.102564,5249.74359,3983.589744,6991.794872,1689.230769,6770.25641,5193.333333,4081.538462,2437.948718,7184.615385,130.7692308,6263.589744,6666.3245]
def randomDimension(number,shape):
    randomNumber = random.randrange(2,15)
    randomNumber1 = random.randrange(2,15)
    randomNumber2 = random.randrange(2,15)
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
        #print shape.color
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
while (1):
    state = libEDK.EE_EngineGetNextEvent(eEvent)
    if state == 0:
        eventType = libEDK.EE_EmoEngineEventGetType(eEvent)
        libEDK.EE_EmoEngineEventGetUserId(eEvent, user)
        if eventType == 16: #libEDK.EE_Event_enum.EE_UserAdded:
            print "User added"
            libEDK.EE_DataAcquisitionEnable(userID,True)
            readytocollect = True

    if readytocollect==True:    
        libEDK.EE_DataUpdateHandle(0, hData)
        libEDK.EE_DataGetNumberOfSample(hData,nSamplesTaken)
        print "Updated :",nSamplesTaken[0]
        if nSamplesTaken[0] != 0:
            nSam=nSamplesTaken[0]
            arr=(ctypes.c_double*nSamplesTaken[0])()
            ctypes.cast(arr, ctypes.POINTER(ctypes.c_double))
            #libEDK.EE_DataGet(hData, 3,byref(arr), nSam)                         
            #data = array('d')#zeros(nSamplesTaken[0],double)
            for sampleIdx in range(nSamplesTaken[0]): 
                for i in range(22): 
                    libEDK.EE_DataGet(hData,targetChannelList[i],byref(arr), nSam)
                    #print arr[sampleIdx],",",
                    if i<14:
                        array[i]=arr[i]
                #print '\n'
                x=x+1
                y=y+1
                z=z+1
                rate(20)
                #ball.rotate(angle=pi/4, axis=axis, origin=pos)
                ball.rotate(angle=120)
                #***********Ball 1***********************************************
                ball.pos= vector(sin(x)*number1,sin(x)*number1,cos(z)*number1) #pi*1/4
                ball.radius = number1/7
                ball = randomColor(ball)
                ball.trail_object.color = ball2.color
                #***********Ball 2***********************************************
                ball9.pos=vector(cos(x)*number1,-cos(x)*number1,sin(x)*number1)#pi*3/4
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
                ball5.pos=vector(sin(x)*number1*1.2,cos(y)*number1*1.5,0)#increase .1
                ball5.radius = number1/7
                ball5 = randomColor(ball5)
                ball5.trail_object.color = ball2.color
                #***********Ball 7***********************************************
                ball10.pos=vector(sin(x)*number1*1.8,cos(y)*number1*1.8,0)#increase .2
                ball10.radius = number1/7
                ball10 = randomColor(ball10)
                ball10.trail_object.color = ball2.color
                #***********Ball 8***********************************************
                ball6.pos=vector(sin(x)*number1*2.0,cos(y)*number1*2.0,0)#decrease .1
                ball6.radius = number1/7
                ball6 = randomColor(ball6)
                ball6.trail_object.color = ball2.color
                #***********Ball 9***********************************************
                ball7.pos=vector(sin(x)*number1*2.2,cos(y)*number1*2.2,0)#decrease .2
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
            
                #other.setarray(arr)
    
    time.sleep(0.2)

    #rate(5)
libEDK.EE_DataFree(hData)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
libEDK.EE_EngineDisconnect()
libEDK.EE_EmoStateFree(eState)
libEDK.EE_EmoEngineEventFree(eEvent)
def statusA():
    return arr


