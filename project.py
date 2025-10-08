# # Alarm Clock
import datetime
import time
from playsound import playsound


alarmHour = int(input("Enter Hour (1-12): "))
alarmMin = int(input("Enter Minutes (0-59): "))
alarmAm = input("am/pm: ").strip().lower()


if alarmAm == "pm" and alarmHour != 12:
    alarmHour += 12
elif alarmAm == "am" and alarmHour == 12:
    alarmHour = 0

print(f"Alarm set for {alarmHour:02d}:{alarmMin:02d}")


while True:
    now = datetime.datetime.now()
    if now.hour == alarmHour and now.minute == alarmMin:
        print(" Alarm ringing...")
        playsound(r"D:\Html\pythonVS\ko_tamil_new.mp3")  
        break
    time.sleep(1)
