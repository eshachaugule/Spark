from pygame import mixer
import signal

mixer.init()

mixer.music.load('bensound-epic.mp3')
mixer.music.play()

signal.pause()
