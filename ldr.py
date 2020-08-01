from gpiozero import MCP3008, RGBLED

rgb=RGBLED(18, 12, 13)

ldr = MCP3008(channel = 6)
while True:
    if ldr.value > 0.15:
        rgb.pulse(fade_in_time=1, fade_out_time=1, on_color=(1, 0, 0), off_color=(0, 0, 1), n=1, background=False)
        gn = 0

    if ldr.value<0.15 and gn==0:
       
        rgb.color=(0,0,0)
        gn = 1

