from gpiozero import PWMLED

L1=PWMLED(22)
L2=PWMLED(25)

L1.value=0.1
L2.value=0.75

L1.pulse(fade_in_time=1, fade_out_time=1, n=None, background=True)
L2.pulse(fade_in_time=1, fade_out_time=1, n=None, background=True)
