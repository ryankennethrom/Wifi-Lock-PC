import sys
import subprocess
from devSettings import *
from pathlib import Path 

def buildMonitorExeFile():
    subprocess.call(f"python -m PyInstaller --distpath {str(Path.cwd())} -F --noconsole --name Monitor monitor.py")

def buildMainExeFile():
    subprocess.call(f"python -m PyInstaller --distpath {str(Path.cwd())} -F --name {programName} main.py")

def buildSchedulerExeFile():
    subprocess.call(f"python -m PyInstaller --distpath {str(Path.cwd())} -F --noconsole --name Scheduler scheduler.py")

if "__main__" == __name__:

    if "All" in sys.argv:
        buildMonitorExeFile()
        buildMainExeFile()
        buildSchedulerExeFile()
    else :
        if "Monitor" in sys.argv:
            buildMonitorExeFile()

        if "Main" in sys.argv:
            buildMainExeFile()

        if "Scheduler" in sys.argv:
            buildSchedulerExeFile()