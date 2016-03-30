import random
import Tkinter
from Tkinter import Button
from Tkinter import Label
from Tkinter import PhotoImage
import threading
import pygame
import time

#initialize variables
#setup the root for TKInter
root = Tkinter.Tk()
root.title("Emotiv")
#initialize pygame
pygame.init()
# get images from local file location
play = PhotoImage(file="play.png")
pause = PhotoImage(file="pause.png")
refresh = PhotoImage(file="refresh.png")
song = None

#if 0 (first play), 1 play, 2 is pause
playorpause = 0;

#function to run on the thread to play music
def playMusic():
    #setup global variables for use in function
    global song
    global play
    global playorpause
    #if a song is meant to start over
    if(playorpause == 0):
	#create a list of songs from in the local files of the project
        songs  = ['warp.mp3', 'Rapgod.mp3', 'ILoveItWhenYouCry.mp3']
	#select a song in the list of songs
        rand = random.randint(0, len(songs) - 1)
        songatnum = songs[rand]
	#create a pygame Sound object from the song picked in the file
        song = pygame.mixer.Sound(songatnum)
	#load the song into the pygame music player
        pygame.mixer.music.load(songatnum)
	#play the song
        pygame.mixer.music.play() 
	#set the image to a pause image
        playbutton.config(image=pause)
        playorpause = 1
    #if the event is 1, pause the song
    elif(playorpause == 1):
	#set the button to the play image
        playbutton.config(image=play)
        playorpause = 2
	#pause the pygame music player
        pygame.mixer.music.pause()
    #if the event is 2, unpause the song
    else:
	#set the button to the pause image
        playbutton.config(image=pause)
	#unpause the pygame music player
        pygame.mixer.music.unpause()
        playorpause = 1

#function when play button is clicked
def button_clicked():
    #plays the music from pygame (random list of songs)  
    #start a thread so the UI doesn't freeze (worker thread)    
    t = threading.Thread(target=playMusic())
    t.start()

#function when refresh button is clicked
def button_refresh():
    #get global variables
    global playorpause
    #set the button to be a pause button (playing)
    playbutton.config(image=pause)
    #reset variable to be first run
    playorpause = 0
    #start a thread to play a song
    t = threading.Thread(target=playMusic())
    t.start()

#add a tkinter button to the main panel (play button)
playbutton = Button(root, command=button_clicked, image=play)
playbutton.pack()

#refresh tkinter button
refreshbutton = Button(root, command=button_refresh, image=refresh)
refreshbutton.pack()

#start the main root loop
root.mainloop()


