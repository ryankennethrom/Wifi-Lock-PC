import subprocess
from globalvariables import programName

subprocess.call(f"python -m PyInstaller -F --noconsole --name {programName} main.py")