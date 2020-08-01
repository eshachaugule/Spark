from gpiozero import LED

L1 = LED(22)
L2 = LED(25)

L1.blink(on_time = 1, off_time = 1, n=5, background = False)
L2.blink(on_time = 1, off_time = 1, n= None, background = True)

