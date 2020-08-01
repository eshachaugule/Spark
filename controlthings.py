from sprw.io import IOT
from gpiozero import PWMLED, RGBLED, Motor, MCP3008, Button, DigitalInputDevice
from time import sleep

sp_server = IOT('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjE1ZGE5NGRiZTFmZTA4ZGQ4MTI0OWVmMTdlNzVhNzFjMjk3YmFmZGU0NTI0MWFiMjQ1Yjc2MmI5MzYwYTIzYTA4NDBlNTkyNzJkOGJjZGU4In0.eyJhdWQiOiIzIiwianRpIjoiMTVkYTk0ZGJlMWZlMDhkZDgxMjQ5ZWYxN2U3NWE3MWMyOTdiYWZkZTQ1MjQxYWIyNDViNzYyYjkzNjBhMjNhMDg0MGU1OTI3MmQ4YmNkZTgiLCJpYXQiOjE1NTk4MjQyOTcsIm5iZiI6MTU1OTgyNDI5NywiZXhwIjoxNTkxNDQ2Njk3LCJzdWIiOiIxOTEwNiIsInNjb3BlcyI6W119.eucK10HKTeAVkDT6UyvcJekvHlMuFezJeAqPJydVcFPAM1yP_2XmivTUzndNd_GYEutUOqEUw_rYRUyEBCbF2Ud9iriTFrOgyHiiTiaznwbsxpWPqwUw77BQwsAXibd6aVa5cO_GsC6lxO4OZ8tS2UztPTwmJaK2oN1P-MkpGDonXD9vuytxe9KGgCFT2C7cdhu07ll_rHOy3Khg1QyP1tzFU2d63BwcGX0WdKO3Y2YPWJhse13w0hkewzvia6V08ItPIdXB2UR0thEIM46Tgka9vvezEUC0VgFT_RNWGMuD1IcJ3GAJSX22R4iVxQbZjv5fVWFmUQc63MBPD48lwIqh6aiQJBJDjTlbkRhhgFWVHAhFs0-evzWA17txGHtQFONZefLQNQ1DMZSYBfdX0bY9gv9OasvklLLCBCYHRz1J_qwsNpKIlR_42pLEbUFCtXZ82-9pTMkSeVKvgF8oSn538a5-BI-lp-6_zN3yxsSq9M0R5rvsoKCGtxcteYYyK9aXccbT3RaceY_bY1CIAu2PwBQtCAHnPYw3gs0_y_RguEOOUf_zQm80Hh7wHy-jXVIVJ3efi2qh2CcwrWmSb5X53ZEoXUytmI9K8ECEk8wyPYJ_k0B4BYnTWV1v2K3bfPGuEW6T8D83kVxIsID9gcwOLUxPfVod85rFMqEhRfI')

L1 = PWMLED(22)
L2=PWMLED(25)

RGB = RGBLED(18, 12, 13)

M1 = Motor(19, 26)

prev_direction = 'FORWARD'

ldr = MCP3008(channel = 6)
temp = MCP3008(channel = 7)
b1 = Button(23)
b2 = Button(24)

ir = DigitalInputDevice(16)

while True:
    L1_virtual = sp_server.get_thing_state_attributes(1319)
    L2_virtual = sp_server.get_thing_state_attributes(1320)
    RGB_virtual = sp_server.get_thing_state_attributes(1328)
    M1_virtual = sp_server.get_thing_state_attributes(1323)


    if L1.value != L1_virtual.value:  
        L1.value = L1_virtual.value
        sp_server.acknowledge_thing_state_attribute(1319, value = L1_virtual.value)

    if L2.value != L2_virtual.value:
        L2.value = L2_virtual.value
        sp_server.acknowledge_thing_state_attribute(1320, value = L2_virtual.value)

    if RGB.color != (RGB_virtual.value_r, RGB_virtual.value_g, RGB_virtual.value_b):
        RGB.color = (RGB_virtual.value_r, RGB_virtual.value_g, RGB_virtual.value_b)
        sp_server.acknowledge_thing_state_attribute(1328, value_r = RGB_virtual.value_r, value_g = RGB_virtual.value_g, value_b = RGB_virtual.value_b)

    if prev_direction!= M1_virtual.direction:
        
        if M1_virtual.direction == 'FORWARD':
            M1.forward()
        elif M1_virtual.direction == 'BACKWARD':
            M1.backward()
        else:
            M1.stop()

    sp_server.acknowledge_thing_state_attribute(1323, direction = M1_virtual.direction)
    prev_direction = M1_virtual.direction

            

    temp_final_value = (temp.value*3*50)-3
    sp_server.update_thing_state_attributes(1327,value=temp_final_value)
    
    if ldr.value<0.5:
        sp_server.update_thing_state_attributes(1326, value=0)
    else:
        sp_server.update_thing_state_attributes(1326, value=1)

    sp_server.update_thing_state_attributes(1321, value = b1.value)
    sp_server.update_thing_state_attributes(1322, value = b2.value)

    sp_server.update_thing_state_attributes(1325, value = ir.value)       
        
    sleep(1)
    
