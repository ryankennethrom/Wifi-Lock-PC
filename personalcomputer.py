import os
import ctypes
import datetime
import subprocess

# Shuts down the computer
def shutdownComputer():
    os.system("shutdown -s -f -t 0")

def rebootComputer():
    subprocess.call("shutdown /r /t 0", shell=True)
    
# Locks the computer
def lockComputer():
    ctypes.windll.user32.LockWorkStation()

def getCurrentHour(format: str):
    if(format == "24-hours"):
        now = datetime.datetime.now()
        hour_now = int(str(now.time())[:2])
        return hour_now
    else:
        raise Exception("Unsupported format argument on getCurrentHour()")