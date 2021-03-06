from sprw.io import IOT

sp_server = IOT('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjE1ZGE5NGRiZTFmZTA4ZGQ4MTI0OWVmMTdlNzVhNzFjMjk3YmFmZGU0NTI0MWFiMjQ1Yjc2MmI5MzYwYTIzYTA4NDBlNTkyNzJkOGJjZGU4In0.eyJhdWQiOiIzIiwianRpIjoiMTVkYTk0ZGJlMWZlMDhkZDgxMjQ5ZWYxN2U3NWE3MWMyOTdiYWZkZTQ1MjQxYWIyNDViNzYyYjkzNjBhMjNhMDg0MGU1OTI3MmQ4YmNkZTgiLCJpYXQiOjE1NTk4MjQyOTcsIm5iZiI6MTU1OTgyNDI5NywiZXhwIjoxNTkxNDQ2Njk3LCJzdWIiOiIxOTEwNiIsInNjb3BlcyI6W119.eucK10HKTeAVkDT6UyvcJekvHlMuFezJeAqPJydVcFPAM1yP_2XmivTUzndNd_GYEutUOqEUw_rYRUyEBCbF2Ud9iriTFrOgyHiiTiaznwbsxpWPqwUw77BQwsAXibd6aVa5cO_GsC6lxO4OZ8tS2UztPTwmJaK2oN1P-MkpGDonXD9vuytxe9KGgCFT2C7cdhu07ll_rHOy3Khg1QyP1tzFU2d63BwcGX0WdKO3Y2YPWJhse13w0hkewzvia6V08ItPIdXB2UR0thEIM46Tgka9vvezEUC0VgFT_RNWGMuD1IcJ3GAJSX22R4iVxQbZjv5fVWFmUQc63MBPD48lwIqh6aiQJBJDjTlbkRhhgFWVHAhFs0-evzWA17txGHtQFONZefLQNQ1DMZSYBfdX0bY9gv9OasvklLLCBCYHRz1J_qwsNpKIlR_42pLEbUFCtXZ82-9pTMkSeVKvgF8oSn538a5-BI-lp-6_zN3yxsSq9M0R5rvsoKCGtxcteYYyK9aXccbT3RaceY_bY1CIAu2PwBQtCAHnPYw3gs0_y_RguEOOUf_zQm80Hh7wHy-jXVIVJ3efi2qh2CcwrWmSb5X53ZEoXUytmI9K8ECEk8wyPYJ_k0B4BYnTWV1v2K3bfPGuEW6T8D83kVxIsID9gcwOLUxPfVod85rFMqEhRfI')

sp_server.create_thing('L1', 'OUTPUT_DEVICE', 'LED')
sp_server.create_thing('L2', 'OUTPUT_DEVICE', 'LED')
sp_server.create_thing('B1', 'INPUT_DEVICE', 'BUTTON')
sp_server.create_thing('B2', 'INPUT_DEVICE', 'BUTTON')
sp_server.create_thing('M1', 'OUTPUT_DEVICE', 'MOTOR')
sp_server.create_thing('M2', 'OUTPUT_DEVICE', 'MOTOR')
sp_server.create_thing('IR Sensor', 'INPUT_DEVICE', 'PROXIMITY')
sp_server.create_thing('Light Sensor', 'INPUT_DEVICE', 'LIGHT')
sp_server.create_thing('Temperature Sensor', 'INPUT_DEVICE', 'TEMPERATURE')
sp_server.create_thing('RGB LED', 'OUTPUT_DEVICE', 'RGB_LED')

sp_server.create_thing('Spark', 'OTHERS', 'ASSISTANT')
       
