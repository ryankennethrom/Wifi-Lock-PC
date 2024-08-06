import subprocess
from devSettings import *
from configureSettings import *
from pathlib import Path   

class Registry():
    def __init__(self):
        pass

    def registerProgram(self):
        # Use triple quotes string literal to span PowerShell command multiline
        STR_CMD = f"""
        $action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "{str(Path.cwd())+"\\"+connectionCheckerName}.exe" -WorkingDirectory "{get("workingDirectory")}";
        $description = "Lock the PC when connected to a restricted wifi IP address.";
        $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -RestartCount 3 -RestartInterval (New-TimeSpan -Seconds 60);
        $taskName = "{programName+get("windowsUserName")}";
        $user = "{get("windowsUserName")}";
        $trigger = New-ScheduledTaskTrigger -AtLogOn -User "{get("windowsUserName")}";
        Register-ScheduledTask -User $user -TaskName $taskName -Description $description -Action $action -RunLevel Highest -Settings $settings -Trigger $trigger | Out-Null
        """

        if debugEnabled == True:
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
        else:
                # Use a list to make it easier to pass argument to subprocess
            listProcess = [
                    "powershell.exe",
                    "-NoProfile",
                    "-WindowStyle",
                    "Hidden",
                    "-Command",
                    STR_CMD
                ]

            # Enjoy the magic
            subprocess.run(listProcess, check=True) 

    def unregisterProgram(self):
        STR_CMD = f"""
        Unregister-ScheduledTask -TaskName "{programName+get("windowsUserName")}"
        """

        if debugEnabled == True:
            print("unregisterProgram() > STR_CMD = " + STR_CMD)

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
        else:
            # Use a list to make it easier to pass argument to subprocess
            listProcess = [
                    "powershell.exe",
                    "-NoProfile",
                    "-WindowStyle",
                    "Hidden",
                    "-Command",
                    STR_CMD
                ]

                # Enjoy the magic
            subprocess.run(listProcess, check=True)