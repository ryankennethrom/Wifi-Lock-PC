import pyuac
from wificontroller import getConnectedWifiIPAddress
from personalcomputer import getCurrentHour, shutdownComputer
from terminal import log
from globalvariables import execIntervalInSeconds, iso_hour_start, iso_hour_end, restricted_ip_addresses
from programpointer import waitForSeconds

def isRestrictedTime():
    hour_now = getCurrentHour(format="24-hours")
    return hour_now >= iso_hour_start and hour_now <= iso_hour_end

def isRestrictedIPAddress(ip_address: str):
    for dict in restricted_ip_addresses:
        if dict["IP Address"] == ip_address:
            return True
    return False

def main():
    while True:
        connected_wifi_ip_address = getConnectedWifiIPAddress()

        log("Connected Wi-Fi IP Address", connected_wifi_ip_address)

        if(isRestrictedIPAddress(connected_wifi_ip_address)):
            shutdownComputer()
        
        waitForSeconds(execIntervalInSeconds)

if not pyuac.isUserAdmin():
    print("Re-launching as admin!")
    pyuac.runAsAdmin()
else:        
    main()
