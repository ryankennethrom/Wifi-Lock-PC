import subprocess
from devSettings import *
from configureSettings import *

class UserPreference():
    def __init__(self):
        pass
    
    def isRestrictionsActive(self):
        call = "powershell.exe -command \"Get-ScheduledTask | Where-Object {$_.TaskName -like" + f" '{programName+get("windowsUserName")}'"+"}\""
        output = subprocess.check_output(call, shell=True)
        if "Running" in str(output) or "Ready" in str(output):
            return True
        else:
            return False