#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from threading import *

#Rightside touch, used as Pause and TrackSelect
touch = TouchSensor(Port.S1)
#Leftside touch, used as Track Change
SelectButton = TouchSensor(Port.S4)
#Left and Right are backwards, please input negative velocity
left = Motor(Port.D)
right = Motor(Port.A)
TOUCHED = True
selectionMade = 0

#pause function monitors the touch sensor for pause inputs. Changes the TOUCHED global variable
#from true to false and back again. On start should be True for music selection.
def pause():
    #Call in the touchSensor into scope
    global touch
    while True:
        if touch.pressed():
            global TOUCHED
            if TOUCHED == False:
                TOUCHED = True
            elif TOUCHED == True:
                TOUCHED = False
            #Call a while loop so holding the trigger doesn't cause repeated triggering,
            #only distinct touches
            while touch.pressed():
                wait(5)


# The following is a list of notes arranged in a list.
# note, duration, and delay(440,40,80, 349,350,40 etc...)
#Darude Sandstorm
darudeList = [440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 80, 160,
        440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 80, 160,
        587.33, 40, 80, 587.33, 40, 80, 587.33, 40, 80, 587.33, 40, 80, 587.33, 40, 80, 587.33, 40, 80, 587.33, 80, 160,
        523.25, 40, 80, 523.25, 40, 80, 523.25, 40, 80, 523.25, 40, 80, 523.25, 40, 80, 523.25, 40, 80, 523.25, 80, 160, 392, 80, 160,
        440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 80, 160,
        440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 80, 160, 587.33, 40, 80, 587.33, 40, 80,
        440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 80, 160,
        440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 80, 160, 587.33, 40, 80, 587.33, 40, 80,
        440, 40, 80, 440, 40, 80, 440, 80, 160, 440, 80, 160, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80,
        440, 80, 160, 523.25, 160, 320, 440, 40, 80, 440, 40, 80, 440, 80, 160, 440, 80, 160, 440, 40, 80, 440, 40, 80,
        440, 40, 80, 440, 40, 80, 440, 80, 160, 523.25, 80, 160, 523.25, 80, 160,440, 40, 80, 440, 40, 80,
        440, 80, 160, 440, 80, 160, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 80, 160, 440, 80, 160, 
        587.33, 40, 80, 587.33, 40, 80, 587.33, 40, 80, 587.33, 40, 80, 587.33, 80, 160, 587.33, 80, 160,
        523.25, 40, 80, 523.25, 40, 80, 523.25, 40, 80, 523.25, 40, 80, 523.25, 80, 160, 523.25, 80, 160, 392, 80, 160,
        440, 40, 80, 440, 40, 80, 440, 80, 160, 440, 80, 160, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 80, 160,
        523.25, 80, 160, 523.25, 80, 160, 440, 40, 80, 440, 40, 80, 440, 80, 160, 440, 80, 160, 
        440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 40, 80, 440, 80, 160, 523.25, 80, 160, 523.25, 80, 160,
        440, 40, 80, 440, 40, 80, 440, 80, 160, 523.25, 80, 160, 523.25, 80, 160,
        440, 40, 80, 440, 40, 80, 440, 80, 160, 523.25, 80, 160, 523.25, 80, 160,
        440, 40, 80, 440, 40, 80, 440, 80, 160, 523.25, 80, 160, 523.25, 80, 160,
        440, 40, 80, 440, 40, 80, 440, 80, 160, 523.25, 80, 160, 523.25, 80, 160,
        440, 40, 80, 440, 40, 80, 523.25, 80, 160, 440, 40, 80, 440, 40, 80, 523.25, 80, 160,
        440, 40, 80, 440, 40, 80, 523.25, 80, 160, 440, 40, 80, 440, 40, 80, 523.25, 80, 160,
        440, 40, 80, 440, 40, 80, 523.25, 80, 160, 440, 40, 80, 440, 40, 80, 523.25, 80, 160,
        440, 40, 80, 440, 40, 80, 523.25, 80, 160, 440, 40, 80, 440, 40, 80, 523.25, 80, 160,
        587.33, 2560, 1]
#Megalovania
megaList = [293,70,70, 293,61,61, 587,124,124, 440,184,184, 415,128,128,
            392,121,121, 349,126,126, 293,61,61, 349,61,61, 392,64,64,
            261,70,70, 261,61,61, 587,124,124, 440,184,184, 415,128,128,
            392,121,121, 349,126,126, 293,61,61, 349,61,61, 392,128,64,
            246,70,70, 246,61,61, 587,124,124, 440,184,184, 415,128,128,
            392,121,121, 349,61,126, 293,61,61, 349,64,64, 392,64,64,
            233,70,70, 233,61,61, 587,124,124, 440,184,184, 415,128,128,
            392,121,121, 349,126,126, 293,61,61, 349,61,61, 392,64,64,
            293,70,70, 293,61,61, 587,124,124, 440,184,184, 415,128,128,
            392,121,121, 349,126,126, 293,61,61, 349,61,61, 392,64,64,
            261,70,70, 261,61,61, 587,124,124, 440,184,184, 415,128,128,
            392,121,121, 349,126,126, 293,61,61, 349,61,61, 392,128,64,
            246,70,70, 246,61,61, 587,124,124, 440,184,184, 415,128,128,
            392,121,121, 349,61,126, 293,61,61, 349,64,64, 392,64,64,
            233,70,70, 233,61,61, 587,124,124, 440,184,184, 415,128,128,
            392,121,121, 349,126,126, 293,61,61, 349,61,61, 392,64,64]
#Current Track
list = []
#List of Tracks, to allow music selection to loop
trackList = ['Sandstorm', 'Megalovania']

def Music():
    global list
    global darudeList
    global megaList
    changeSong = False
    list = darudeList
    MusicVar = False
    global SelectButton
    global selectionMade
    global touch
    while True:
        changeSong = False
        #Changes to the next track, then rolls track back to start if too many
        if SelectButton.pressed():
            brick.sound.beep(1000,100)
            if MusicVar == False:
                MusicVar = True
            else:
                MusicVar = False
            print('triggeredSelect')
            while SelectButton.pressed():
                wait(5)
        #Detects if Pause has been triggered off (starts on for music selection)
        #then creates a loop of the select track
        if not TOUCHED:
            selectionMade = 1
            print(MusicVar)
        if selectionMade == 1:
            if MusicVar == False:
                list = darudeList
            else:
                list = megaList
            while True:
                MusicPlay()
                break

def MusicPlay():
    # create variables for note and duration and set them to 0 and 1, then create delay as 2.
    # This will call the first and second items from the list. 0 is always the first item.    
    note = 0
    duration = 1
    delay = 2
    #Determines the length of the music so the program doesn't crash
    length = len(list) /3
    lentest = 0
    # using the FOR loop we can say that for every item in a list do something...
    for x in list:
        # play the note and duration on the brick, then wait the listed delay
        brick.sound.beep(list[note], list[duration])
        wait(list[delay])
        # move to the next note and duration in the list by adding 3 to each variable
        note += 3
        duration += 3
        delay += 3
        # test the length of the song compared to how much has been played
        lentest += 1
        if lentest == length:
            break
        #Pause button, this grabs the TOUCHED function from the pause thread then puts this function
        #into an endless loop until unpaused
        global changeSong
        if SelectButton.pressed():
            break
        global TOUCHED
        while TOUCHED:
            wait(5)


#Program begins here
#Start music thread
m = Thread(target=Music)
m.start()
#Start pause thread
p = Thread(target=pause)
p.start()
#Start motor
while selectionMade == 0:
    wait(5)
left.dc(-60)
right.dc(-60)
while True:
    while TOUCHED:
        left.stop()
        right.stop()
    left.dc(-60)
    right.dc(-60)
    wait(5)

#Program Ends