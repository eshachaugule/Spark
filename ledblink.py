from gpiozero import LED
from time import sleep

L1 = LED(22)
L2 = LED(25)


L1.on()
L2.on()
sleep(1)

    
    
    
L1.off()
L2.off()
sleep(1)
    

