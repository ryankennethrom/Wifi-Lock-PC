import subprocess
from devSettings import *
from pathlib import Path 

def buildMonitorExeFile():
    subprocess.call(f"python -m PyInstaller --distpath {str(Path.cwd())} -F --noconsole --name Monitor monitor.py")

def buildMainExeFile():
    subprocess.call(f"python -m PyInstaller --distpath {str(Path.cwd())} -F --name {programName} main.py")

buildMainExeFile()
# buildMonitorExeFile()