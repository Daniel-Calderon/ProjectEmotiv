# python version >= 2.5
#this code is based off of an emotiv example given on the emotiv site we modify to
#the extract the data from the headset to give a visualization of a random channel using Vpython
#Authors: Brandan Lockwood,Brock D` Amico,Daniel,Daniel CalderonManriquez
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

#try to make sure libraries can load into python
try :
    if sys.platform.startswith('win32'):     
        libEDK = cdll.LoadLibrary("edk.dll")
    if sys.platform.startswith('linux'):
        srcDir = os.getcwd()    
        libPath = srcDir + "/libedk.so.1.0.0"        
        libEDK = CDLL(libPath)
except :
    print 'Error : cannot load dll lib' 
#setup variables for emotiv epoc+ from example
arr=[]
    
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

#check if emtoiv system is working properly
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
#random channel chooses channel based off array
def randomDimension(number,shape):
    #get random numbers
    randomNumber = random.randrange(2,15)
    randomNumber1 = random.randrange(2,15)
    randomNumber2 = random.randrange(2,15)
    #based on random number then chooose random channels
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
#chooses random color
def randomColor(shape):
    #get random color Vpython ranges its color from 0 to 1
    randomNumber1 = random.randrange(0,2)
    randomNumber2 = random.randrange(0,2)
    randomNumber3 = random.randrange(0,2)
    #if black choose force a different color
    if(randomNumber3==0 and randomNumber2==0 and randomNumber1==0):
        randonNumber1=1
        randomNumber3=1
    shape.color= (randomNumber1,randomNumber2,randomNumber3)
    return shape
#make a new shape
def randomShape(shape):
    #get random number
    randomNumber = random.randrange(1,9)
    #change shape based on the random number
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
#setup spheres on the screen
ball = sphere(pos=(1,1,1), radius=0.1,make_trail=True, trail_type="points",
              interval=10, retain=50)
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
    #begin getting event information this how emotiv gets information about the user
    state = libEDK.EE_EngineGetNextEvent(eEvent)
    if state == 0:
        eventType = libEDK.EE_EmoEngineEventGetType(eEvent)
        libEDK.EE_EmoEngineEventGetUserId(eEvent, user)
        if eventType == 16:
            print "User added"
            libEDK.EE_DataAcquisitionEnable(userID,True)
            readytocollect = True
    #checks to make sure data is ready to collect
    if readytocollect==True:    
        libEDK.EE_DataUpdateHandle(0, hData)
        libEDK.EE_DataGetNumberOfSample(hData,nSamplesTaken)
        print "Updated :",nSamplesTaken[0]
        if nSamplesTaken[0] != 0:
            nSam=nSamplesTaken[0]
            arr=(ctypes.c_double*nSamplesTaken[0])()
            ctypes.cast(arr, ctypes.POINTER(ctypes.c_double))
            #get information from emotiv epoc+ to get 
            for sampleIdx in range(nSamplesTaken[0]): 
                for i in range(22): 
                    libEDK.EE_DataGet(hData,targetChannelList[i],byref(arr), nSam)
                    #set array to channels
                    if i<15:
                        array[i]=arr[i]
                x=x+1
                y=y+1
                z=z+1
                rate(20)
                ball.rotate(angle=120)
                #balls length away from center object is based off of random channel
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
                ball5.pos=vector(sin(x)*number1*1.5,cos(y)*number1*1.5,0)#increase by 1.5
                ball5.radius = number1/7
                ball5 = randomColor(ball5)
                ball5.trail_object.color = ball2.color
                #***********Ball 7***********************************************
                ball10.pos=vector(sin(x)*number1*1.8,cos(y)*number1*1.8,0)#increase 1.8
                ball10.radius = number1/7
                ball10 = randomColor(ball10)
                ball10.trail_object.color = ball2.color
                #***********Ball 8***********************************************
                ball6.pos=vector(sin(x)*number1*2.0,cos(y)*number1*2.0,0)#increase 2.0
                ball6.radius = number1/7
                ball6 = randomColor(ball6)
                ball6.trail_object.color = ball2.color
                #***********Ball 9***********************************************
                ball7.pos=vector(sin(x)*number1*2.2,cos(y)*number1*2.2,0)#increase2.2
                ball7.radius = number1/7
                ball7 = randomColor(ball7)
                ball7.trail_object.color = ball2.color
                #change if mouse is clicked within window
                if scene.mouse.clicked:
                    ball2.visible = false
                    ball2,number = randomShape(ball2)
                    number1 = array[number]
                    m = scene.mouse.getclick()
                    loc = m.pos
                ball2 = randomColor(ball2)
                ball2 = randomDimension(number,ball2)
    #sleep thread
    time.sleep(0.2)
libEDK.EE_DataFree(hData)
#disconnect emotive epoc+ from program
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
libEDK.EE_EngineDisconnect()
libEDK.EE_EmoStateFree(eState)
libEDK.EE_EmoEngineEventFree(eEvent)


