# https://www.fesliyanstudios.com/
from playsound import playsound
import time

def alarm(seconds):
    time_elasped = 0
    
    while time_elasped < seconds:
        time.sleep(1)
        time_elasped += 1
        
        time_left = seconds - time_elasped
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{minutes_left:02d}:{seconds_left:02d}")
        
alarm(10)


#playsound("tokyo_lofi_alarm.mp3")