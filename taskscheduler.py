import subprocess
from globalvariables import programName
from globalvariables import path_to_exe_file
import os

def registerProgram():

    # Use triple quotes string literal to span PowerShell command multiline
    STR_CMD = f"""
    $action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "{path_to_exe_file}"
    $description = "Lock the PC when connected to a restricted wifi IP address."
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -RestartCount 3 -RestartInterval (New-TimeSpan -Seconds 60)
    $taskName = "{programName+os.getlogin()}"
    $user = "{os.getlogin()}"
    $trigger = New-ScheduledTaskTrigger -AtLogOn -User "{os.getlogin()}"
    Register-ScheduledTask -User $user -TaskName $taskName -Description $description -Action $action -RunLevel Highest -Settings $settings -Trigger $trigger | Out-Null
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

def unregisterProgram():

    STR_CMD = f"""
    Unregister-ScheduledTask -TaskName "{programName}"
    """

    listProcess = [
        "powershell.exe",
        "-NoExit",
        "-NoProfile",
        "-Command",
        STR_CMD
    ]
    
    subprocess.run(listProcess, check=True)

import pyuac
if not pyuac.isUserAdmin():
    print("Re-launching as admin!")
    pyuac.runAsAdmin()
else:        
    registerProgram()