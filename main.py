import time
import pyuac
from taskmanager import killTaskManager
from personalcomputer import disableWifi, enableWifi, getCurrentHour, getConnectedWifiIPAddress
from terminal import log
from globalVariables import execIntervalInSeconds, iso_hour_start, iso_hour_end, restricted_ip_addresses


def isRestrictedTime():
    hour_now = getCurrentHour(format="24-hours")
    return hour_now >= iso_hour_start and hour_now <= iso_hour_end

def isRestrictedIPAddress(ip_address: str):
    return ip_address in restricted_ip_addresses

def waitForSeconds(timeInSeconds: int):
    time.sleep(timeInSeconds)

def isNoWifiConnection():
    connected_wifi_ip_address = getConnectedWifiIPAddress()
    return connected_wifi_ip_address == "127.0.0.1"

def main():

    while True:
        connected_wifi_ip_address = getConnectedWifiIPAddress()

        log("Connected Wi-Fi IP Address", connected_wifi_ip_address)

        if(isRestrictedTime() or isRestrictedIPAddress(connected_wifi_ip_address)):
            disableWifi()
            killTaskManager()
        else:
            enableWifi()
            
        waitForSeconds(execIntervalInSeconds)

if not pyuac.isUserAdmin():
    print("Re-launching as admin!")
    pyuac.runAsAdmin()
else:        
    main()
