from gpiozero import Button, LED

L1 = LED(22)

B1=Button(23)
B1.when_pressed = L1.on
B1.when_released = L1.off
