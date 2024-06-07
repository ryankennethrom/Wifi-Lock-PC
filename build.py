import subprocess
from globalVariables import programName

subprocess.call(f"python -m PyInstaller --noconsole --name {programName} main.py")