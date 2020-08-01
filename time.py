from sprw.io import Assistant
from gpiozero import Button
b1 = Button(23)


spark = Assistant('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjE1ZGE5NGRiZTFmZTA4ZGQ4MTI0OWVmMTdlNzVhNzFjMjk3YmFmZGU0NTI0MWFiMjQ1Yjc2MmI5MzYwYTIzYTA4NDBlNTkyNzJkOGJjZGU4In0')
while True:
    
    if b1.value == 1:

        now = spark.get_current_datetime()

        print(now)

        month = spark.get_month_in_words(now.month)

        time=spark.get_time_in_words(now.hour, now.minute)

        spark.speak("today is")
        spark.speak(now.day)
        spark.speak(month)
        spark.speak("and the time is")
        spark.speak(time)


