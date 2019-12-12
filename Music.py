#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from threading import *
import random
from time import time
random.seed(int(time()))

def MusicPlay():
    while True:
        # create variables for note and duration and set them to 0 and 1, then create delay as 2.
        # This will call the first and second items from the list. 0 is always the first item.    
        track = random.randint(0,2)
        if track == 0:
            trackmusic = MKombat
        elif track == 1:
            trackmusic = bevCop
        elif track == 2:
            trackmusic = misImpo
        trackmusic = misImpo
        print(track)
        print(trackmusic)
        note = 0
        duration = 1
        delay = 2
        #Determines the length of the music so the program doesn't crash
        length = len(trackmusic) /3
        lentest = 0
        # using the FOR loop we can say that for every item in a list do something...
        for x in trackmusic:
            # play the note and duration on the brick, then wait the listed delay
            brick.sound.beep(trackmusic[note], trackmusic[duration])
            wait(trackmusic[delay])
            # move to the next note and duration in the list by adding 3 to each variable
            note += 3
            duration += 3
            # test the length of the song compared to how much has been played
            lentest += 1
            if lentest == length:
                break
            #Pause button, this grabs the TOUCHED function from the pause thread then puts this function
            #into an endless loop until unpaused

N1 = 220
N2 = 261
N3 = 293
N4 = 329
N5 = 196
N6 = 174
N7 = 246
N8 = 392
N9 = 164
N10 = 659
N11 = 784
N12 = 740
N13 = 587
N14 = 880
N15 = 494
N16 = 988
N17 = 1047
N18 = 1318
N19 = 277
N20 = 311
N21 = 329
N22 = 349
N23 = 932.33
N24 = 830
N25 = 554
N26 = 622
N27 = 698
N28 = 523
N29 = 466
N30 = 440
N31 = 415
N32 = 370
D1 = 62
D2 = 125
D3 = 250
D4 = 500
D5 = 340


MKombat = [N1,D2,D2, N1,D2,D2, N2,D2,D2, N1,D2,D2, N3,D2,D2, N1,D2,D2, N4,D2,D2, N3,D2,D2, N2,D2,D2,
        N2,D2,D2, N4,D2,D2, N2,D2,D2, N8,D2,D2, N2,D2,D2, N4,D2,D2, N2,D2,D2, N5,D2,D2, N5,D2,D2,
        N7,D2,D2, N5,D2,D2, N2,D2,D2, N5,D2,D2, N3,D2,D2, N2,D2,D2, N6,D2,D2, N6,D2,D2, N1,D2,D2,
        N6,D2,D2, N2,D2,D2, N6,D2,D2, N2,D2,D2, N7,D2,D2, N1,D2,D2, N1,D2,D2, N2,D2,D2, N1,D2,D2,
        N3,D2,D2, N1,D2,D2, N4,D2,D2, N3,D2,D2, N2,D2,D2, N2,D2,D2, N4,D2,D2, N2,D2,D2, N8,D2,D2,
        N2,D2,D2, N4,D2,D2, N2,D2,D2, N5,D2,D2, N5,D2,D2, N7,D2,D2, N5,D2,D2, N2,D2,D2, N5,D2,D2,
        N3,D2,D2, N2,D2,D2, N6,D2,D2, N6,D2,D2, N1,D2,D2, N6,D2,D2, N2,D2,D2, N6,D2,D2, N2,D2,D2,
        N7,D2,D2, N1,D3,D3, N1,D3,D3, N1,D3,D3, N1,D3,D3, N5,D2,D2, N2,D2,D2, N1,D3,D3, N1,D3,D3,
        N1,D3,D3, N1,D3,D3, N5,D2,D2, N9,D2,D2, N1,D3,D3, N1,D3,D3, N1,D3,D3, N1,D3,D3, N5,D2,D2,
        N2,D2,D2, N1,D3,D3, N1,D3,D3, N1,D3,D3, N1,D3,D3, N1,D3,D3, N1,D3,D3, N1,D3,D3, N1,D3,D3,
        N1,D3,D3, N5,D2,D2, N2,D2,D2, N1,D3,D3, N1,D3,D3, N1,D3,D3, N1,D3,D3, N5,D2,D2, N9,D2,D2,
        N1,D3,D3, N1,D3,D3, N1,D3,D3, N1,D3,D3, N5,D2,D2, N2,D2,D2, N1,D3,D3, N1,D3,D3, N1,D3,D3,
        N1,D3,D3, N1,D3,D3, N1,D1,D1, N4,D2,D2, N1,D1,D1, N2,D2,D2, N1,D1,D1, N7,D2,D2, N1,D1,D1,
        N2,D2,D2, N1,D1,D1, N7,D1,D1, N5,D2,D2, N1,D1,D1, N4,D2,D2, N1,D1,D1, N2,D2,D2, N1,D1,D1,
        N7,D2,D2, N1,D1,D1, N2,D2,D2, N1,D1,D1, N7,D1,D1, N5,D2,D2, N1,D1,D1, N4,D2,D2, N1,D1,D1,
        N2,D2,D2, N1,D1,D1, N7,D2,D2, N1,D1,D1, N2,D2,D2, N1,D1,D1, N7,D1,D1, N5,D2,D2, N1,D1,D1,
        N4,D2,D2, N1,D1,D1, N2,D2,D2, N5,D1,D1, N5,D2,D2, N5,D1,D1, N1,D2,D2, N1,D1,D1, N4,D2,D2,
        N1,D1,D1, N2,D2,D2, N1,D1,D1, N7,D2,D2, N1,D1,D1, N2,D2,D2, N1,D1,D1, N7,D1,D1, N5,D2,D2,
        N1,D1,D1, N4,D2,D2, N1,D1,D1, N2,D2,D2, N1,D1,D1, N7,D2,D2, N1,D1,D1, N2,D2,D2, N1,D1,D1,
        N7,D1,D1, N5,D2,D2, N1,D1,D1, N4,D2,D2, N1,D1,D1, N2,D2,D2, N1,D1,D1, N7,D2,D2, N1,D1,D1,
        N2,D2,D2, N1,D1,D1, N7,D1,D1, N5,D2,D2, N1,D1,D1, N4,D2,D2, N1,D1,D1, N2,D2,D2, N5,D1,D1,
        N5,D2,D2, N5,D1,D1, N1,25,25]

bevCop = [N10,D4,D2, N11,D5,D2, N10,D3,D2, N10,D2,D2, N14,D3,D2, N10,D3,D2, N13,D3,D2, N10,D4,D4,
        N16,D5,D2, N10,D3,D2, N10,D2,D2, N17,D3,D2, N16,D3,D2, N11,D3,D2, N10,D3,D2, N16,D3,D3,
        N18,D3,D2, N10,D2,D2, N13,D3,D2, N13,D2,D2, N15,D3,D2, N12,D3,D2, N10,D4,D2]

misImpo = [N8,D2,D2, N8,D3,D3, N8,D2,D2, N8,D2,D2, N29,D2,D2, N2,D2,D2, N8,D2,D2, N8,D2,D2, N8,D2,D2, N8,D2,D2, N22,D2,D2,
        N32,D2,D2, N8,D3,D3, 10,D3,D3, N8,D2,D2, N8,D3,D3, N8,D2,D2, N8,D2,D2, N29,D2,D2, N2,D2,D2, N8,D2,D2, N8,D2,D2,
        N8,D2,D2, N8,D2,D2, N22,D2,D2, N32,D2,D2, N8,D3,D3, 10,D3,D3, N8,D2,D2, N8,D3,D3, N8,D2,D2, N8,D2,D2, N29,D2,D2, N2,D2,D2, N8,D2,D2, N8,D2,D2, N8,D2,D2, N8,D2,D2, N22,D2,D2,
        N32,D2,D2, N8,D3,D3, 10,D3,D3, N8,D2,D2, N8,D3,D3, N8,D2,D2, N8,D2,D2, N29,D2,D2, N2,D2,D2, N8,D2,D2, N8,D2,D2,
        N8,D2,D2, N8,D2,D2, N22,D2,D2, N32,D2,D2, N8,D3,D3, 10,D3,D3, N8,D2,D2, N8,D3,D3, N8,D2,D2, N8,D2,D2, N29,D2,D2, N2,D2,D2, N8,D2,D2, N8,D2,D2, N8,D2,D2, N8,D2,D2, N22,D2,D2,
        N32,D2,D2, N8,D3,D3, 10,D3,D3, N8,D2,D2, N8,D3,D3, N8,D2,D2, N8,D2,D2, N29,D2,D2, N2,D2,D2, N8,D2,D2, N8,D2,D2,
        N8,D2,D2, N8,D2,D2, N22,D2,D2, N32,D2,D2, N8,D3,D3, 10,D3,D3, N8,D2,D2, N8,D3,D3, N8,D2,D2, N8,D2,D2, N29,D2,D2, N2,D2,D2, N8,D2,D2, N8,D2,D2, N8,D2,D2, N8,D2,D2, N22,D2,D2,
        N32,D2,D2, N8,D3,D3, 10,D3,D3, N8,D2,D2, N8,D3,D3, N8,D2,D2, N8,D2,D2, N29,D2,D2, N2,D2,D2, N8,D2,D2, N8,D2,D2,
        N8,D2,D2, N8,D2,D2, N22,D2,D2, N32,D2,D2, N8,D3,D3, 10,D3,D3]

MusicPlay()