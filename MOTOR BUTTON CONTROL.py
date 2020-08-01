
from gpiozero import Motor, Button

m1=Motor(19, 26)
B1=Button(24)


while True:
    if B1.value == 1:   
        m1.forward()
    
    else:
         m1.stop()
  
