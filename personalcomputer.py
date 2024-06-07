import os
import ctypes
import subprocess
import datetime
import socket

# Shuts down the computer
def shutdownComputer():
    os.system("shutdown /s /t 0")

# Locks the computer
def lockComputer():
    ctypes.windll.user32.LockWorkStation()

def disableWifi():
    subprocess.run('netsh interface set interface "Wi-Fi" admin=disable', shell=True)

def enableWifi():
    subprocess.run('netsh interface set interface "Wi-Fi" admin=enable', shell=True)

def getCurrentHour(format: str):
    if(format == "24-hours"):
        now = datetime.datetime.now()
        hour_now = int(str(now.time())[:2])
        return hour_now
    else:
        raise Exception("Unsupported format argument on getCurrentHour()")

def getConnectedWifiIPAddress() -> str:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return str(ip_address)