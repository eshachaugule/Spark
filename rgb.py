from gpiozero import RGBLED
from time import sleep

rgb = RGBLED(18, 12, 13)
while True:
    
    rgb.color = (1, 0, 1)
    sleep(1)
    rgb.color = (1, 1, 0)
    sleep(1)
    rgb.color = (1, 0.5, 0)
    sleep(1)
