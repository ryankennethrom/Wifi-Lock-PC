from personalcomputer import lockComputer
from main import execIntervalInSeconds
from programpointer import waitForSeconds
from wifi import isWifiConnected
import subprocess
from configureSettings import *


def isConnectedToRestrictedWifiConnection():
    interface_info = str(subprocess.check_output("netsh wlan show interfaces", shell=True))
    restrictedConnections = get("restrictedConnections")
    if restrictedConnections == '':
        return False
    for ssid in restrictedConnections.split(","):
        if ssid in interface_info:
            return True
    return False

def main():
    while True:
        if isConnectedToRestrictedWifiConnection() or ( get("restrictWhenNoWifiConnection") and not isWifiConnected()):
            lockComputer()
        waitForSeconds(execIntervalInSeconds)

main()