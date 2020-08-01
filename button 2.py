from gpiozero import Button, LED

B1 = Button(23)
L1 = LED(22)
L2 = LED(25)

while True:
        
    if B1.value == 1:
        L1.on()
        L2.on()

    if B1.value == 0:
        L1.off()
        L2.off()


