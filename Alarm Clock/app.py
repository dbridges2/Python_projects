from datetime import timedelta, datetime
from playsound import playsound

miliAlarm = input("What time would you like the alarm to go off? (Military Time) ")
def alarmClock():
    global current_time
    while True:
       current_time = datetime.now()
       current_time = current_time + timedelta(seconds=1)
       militime = current_time.strftime("%H:%M")
       displaytime =current_time.strftime("%H:%M:%S")
       print(displaytime, end='\r')
       if(str(militime) == str(miliAlarm)):
            playsound('/Users/ultrabeast/Documents/Python_projects/Alarm Clock/alarm.wav')
            print("Your alarm is going off!")
            
            
alarmClock()