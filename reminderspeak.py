from sprw.io import Assistant, IOT
from time import sleep

spark = Assistant('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjE1ZGE5NGRiZTFmZTA4ZGQ4MTI0OWVmMTdlNzVhNzFjMjk3YmFmZGU0NTI0MWFiMjQ1Yjc2MmI5MzYwYTIzYTA4NDBlNTkyNzJkOGJjZGU4In0.eyJhdWQiOiIzIiwianRpIjoiMTVkYTk0ZGJlMWZlMDhkZDgxMjQ5ZWYxN2U3NWE3MWMyOTdiYWZkZTQ1MjQxYWIyNDViNzYyYjkzNjBhMjNhMDg0MGU1OTI3MmQ4YmNkZTgiLCJpYXQiOjE1NTk4MjQyOTcsIm5iZiI6MTU1OTgyNDI5NywiZXhwIjoxNTkxNDQ2Njk3LCJzdWIiOiIxOTEwNiIsInNjb3BlcyI6W119.eucK10HKTeAVkDT6UyvcJekvHlMuFezJeAqPJydVcFPAM1yP_2XmivTUzndNd_GYEutUOqEUw_rYRUyEBCbF2Ud9iriTFrOgyHiiTiaznwbsxpWPqwUw77BQwsAXibd6aVa5cO_GsC6lxO4OZ8tS2UztPTwmJaK2oN1P-MkpGDonXD9vuytxe9KGgCFT2C7cdhu07ll_rHOy3Khg1QyP1tzFU2d63BwcGX0WdKO3Y2YPWJhse13w0hkewzvia6V08ItPIdXB2UR0thEIM46Tgka9vvezEUC0VgFT_RNWGMuD1IcJ3GAJSX22R4iVxQbZjv5fVWFmUQc63MBPD48lwIqh6aiQJBJDjTlbkRhhgFWVHAhFs0-evzWA17txGHtQFONZefLQNQ1DMZSYBfdX0bY9gv9OasvklLLCBCYHRz1J_qwsNpKIlR_42pLEbUFCtXZ82-9pTMkSeVKvgF8oSn538a5-BI-lp-6_zN3yxsSq9M0R5rvsoKCGtxcteYYyK9aXccbT3RaceY_bY1CIAu2PwBQtCAHnPYw3gs0_y_RguEOOUf_zQm80Hh7wHy-jXVIVJ3efi2qh2CcwrWmSb5X53ZEoXUytmI9K8ECEk8wyPYJ_k0B4BYnTWV1v2K3bfPGuEW6T8D83kVxIsID9gcwOLUxPfVod85rFMqEhRfI')

sp_server = IOT('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjE1ZGE5NGRiZTFmZTA4ZGQ4MTI0OWVmMTdlNzVhNzFjMjk3YmFmZGU0NTI0MWFiMjQ1Yjc2MmI5MzYwYTIzYTA4NDBlNTkyNzJkOGJjZGU4In0.eyJhdWQiOiIzIiwianRpIjoiMTVkYTk0ZGJlMWZlMDhkZDgxMjQ5ZWYxN2U3NWE3MWMyOTdiYWZkZTQ1MjQxYWIyNDViNzYyYjkzNjBhMjNhMDg0MGU1OTI3MmQ4YmNkZTgiLCJpYXQiOjE1NTk4MjQyOTcsIm5iZiI6MTU1OTgyNDI5NywiZXhwIjoxNTkxNDQ2Njk3LCJzdWIiOiIxOTEwNiIsInNjb3BlcyI6W119.eucK10HKTeAVkDT6UyvcJekvHlMuFezJeAqPJydVcFPAM1yP_2XmivTUzndNd_GYEutUOqEUw_rYRUyEBCbF2Ud9iriTFrOgyHiiTiaznwbsxpWPqwUw77BQwsAXibd6aVa5cO_GsC6lxO4OZ8tS2UztPTwmJaK2oN1P-MkpGDonXD9vuytxe9KGgCFT2C7cdhu07ll_rHOy3Khg1QyP1tzFU2d63BwcGX0WdKO3Y2YPWJhse13w0hkewzvia6V08ItPIdXB2UR0thEIM46Tgka9vvezEUC0VgFT_RNWGMuD1IcJ3GAJSX22R4iVxQbZjv5fVWFmUQc63MBPD48lwIqh6aiQJBJDjTlbkRhhgFWVHAhFs0-evzWA17txGHtQFONZefLQNQ1DMZSYBfdX0bY9gv9OasvklLLCBCYHRz1J_qwsNpKIlR_42pLEbUFCtXZ82-9pTMkSeVKvgF8oSn538a5-BI-lp-6_zN3yxsSq9M0R5rvsoKCGtxcteYYyK9aXccbT3RaceY_bY1CIAu2PwBQtCAHnPYw3gs0_y_RguEOOUf_zQm80Hh7wHy-jXVIVJ3efi2qh2CcwrWmSb5X53ZEoXUytmI9K8ECEk8wyPYJ_k0B4BYnTWV1v2K3bfPGuEW6T8D83kVxIsID9gcwOLUxPfVod85rFMqEhRfI')

fetch_time = spark.get_current_datetime() - spark.datetime_offset(minutes=10)

while True:

    now = spark.get_current_datetime()

    if now.minute - fetch_time.minute >= 10 or now.minute - fetch_time.minute < 0:

        condition = {
            'time': spark.get_current_datetime() + spark.datetime_offset(hours=2),
            'status': 'ACTIVE'
            }

        virtual_assistant = sp_server.get_thing_multi_state_attributes(thing_id = 1329, reminder_condition = condition)
        fetch_time = spark.get_current_datetime()


    for reminder in virtual_assistant.reminders:

        if spark.get_current_datetime() >= reminder.time and reminder.status == 'ACTIVE':

            spark.speak("hey esha i have a reminder for you")
            spark.speak(reminder.message)
            reminder.status = 'DISMISSED'
            sp_server.update_thing_multi_state_attributes(thing_id = 1329, reminder = reminder)
            sleep(3)
            
