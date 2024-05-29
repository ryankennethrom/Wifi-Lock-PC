# import requests

# ip_address = requests.get('http://api.ipify.org').text

# print(ip_address)

# response = requests.get(f'http://ip-api.com/json/{ip_address}?fields=status,message,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,query').json()

# print(response)



import socket
import ctypes
import time
import subprocess
import pyuac
import tkinter
from tkinter.filedialog import askdirectory

# Public Variables
# 192.168.223.102 for printer
# 127.0.0.1 for no wifi
restricted_ip_addresses = ["192.168.1.75", "192.168.223.102", "127.0.0.1"]
path_to_exe_file = "C:\\Users\\ryanr\\IP-Lock-PC\\dist\\IPLockPC.exe"

# Private Variables
taskName = "IPLockPC"
program_execution_interval_seconds = 10

def main():
    while True:
        hostname = socket.gethostname()

        ip_address = socket.gethostbyname(hostname)

        print("IP address: " + ip_address)

        if str(ip_address) in restricted_ip_addresses:
            ctypes.windll.user32.LockWorkStation()
        
        time.sleep(program_execution_interval_seconds)

def registerScheduledTask():

    # Use triple quotes string literal to span PowerShell command multiline
    STR_CMD = f"""
    $action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "{path_to_exe_file}"
    $description = "Lock the PC when connected to a restricted wifi IP address."
    $settings = New-ScheduledTaskSettingsSet -RestartCount 3 -RestartInterval (New-TimeSpan -Seconds 60)
    $taskName = "{taskName}"
    $trigger = New-ScheduledTaskTrigger -AtLogOn
    Register-ScheduledTask -TaskName $taskName -Description $description -Action $action -RunLevel Highest -Settings $settings -Trigger $trigger | Out-Null
    """

    # Use a list to make it easier to pass argument to subprocess
    listProcess = [
        "powershell.exe",
        "-NoExit",
        "-NoProfile",
        "-Command",
        STR_CMD
    ]

    # Enjoy the magic
    subprocess.run(listProcess, check=True)

def unregisterScheduledTask():

    STR_CMD = f"""
    Unregister-ScheduledTask -TaskName "{taskName}"
    """

    listProcess = [
        "powershell.exe",
        "-NoExit",
        "-NoProfile",
        "-Command",
        STR_CMD
    ]
    
    subprocess.run(listProcess, check=True)

main()

# if not pyuac.isUserAdmin():
#     print("Re-launching as admin!")
#     pyuac.runAsAdmin()
# else:        
#     main() # Already an admin here.

# root = tkinter.Tk()
# root.title("IPLockPC")

# def addIP():
#     pass

# def askDirectory():
#     path = '{}'.format(askdirectory(title="IPLockPC.exe Path", mustexist=True))

# labelTitle = tkinter.Label(root, text="IPLockPC", bg="white")
# labelTitle.pack()

# ipTextInput = tkinter.Entry(root, width=15)
# ipTextInput.pack()

# addIPButton = tkinter.Button(root, text="Add IP", fg="green", bg="white", command=addIP)
# addIPButton.pack()

# saveButton = tkinter.Button(root, text="Save", fg="green", bg="white", command=None)
# saveButton.pack()

# saveAndRunButton = tkinter.Button(root, text="Save and Run", fg="green", bg="white", command=None)
# saveAndRunButton.pack()

# ipLockPCExeFilePath = tkinter.Button(root, text="Set Path", fg="green", bg="white", command=askDirectory)
# ipLockPCExeFilePath.pack()

# root.mainloop()