from personalcomputer import lockComputer
from globalvariables import execIntervalInSeconds, restricted_connections, restrictWhenNoWifiConnection
from programpointer import waitForSeconds
from wificontroller import isWifiConnected
import subprocess


def isConnectedToRestrictedWifiConnection():
    for dict in restricted_connections:
        if dict["SSID"] in str(subprocess.check_output("netsh wlan show interfaces")):
            return True
    return False

def main():
    while True:
        if isConnectedToRestrictedWifiConnection() or ( restrictWhenNoWifiConnection and not isWifiConnected()):
            lockComputer()
        waitForSeconds(execIntervalInSeconds)

main()