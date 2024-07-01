from personalcomputer import lockComputer
from globalvariables import execIntervalInSeconds, restricted_connections, restrictWhenNoWifiConnection
from programpointer import waitForSeconds
from wificontroller import isWifiConnected
import subprocess


def isConnectedToRestrictedWifiConnection():
    interface_info = str(subprocess.check_output("netsh wlan show interfaces"))
    ssid_index = interface_info.split().index("SSID")
    ssid_value_index = ssid_index + 2
    for dict in restricted_connections:
        if dict["SSID"] in interface_info.split()[ssid_value_index]:
            return True
    return False

def main():
    while True:
        if isConnectedToRestrictedWifiConnection() or ( restrictWhenNoWifiConnection and not isWifiConnected()):
            # lockComputer()
            print("locked")
            pass
        waitForSeconds(execIntervalInSeconds)

main()