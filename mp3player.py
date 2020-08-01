from gpiozero import Button
from pygame import mixer

import signal

mixer.init()

b1 = Button(23)

x=0

music = ['bensound-epic.mp3', 'bensound-happyrock.mp3', 'bensound-hey.mp3']

def playmusic():
    global x
    mixer.music.load(music[x])
    mixer.music.play()
    x=x+1
    if x==3:
        x=0

b1.when_pressed=playmusic

signal.pause()
