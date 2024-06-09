import pyuac
from wificontroller import getConnectedWifiIPAddress
from personalcomputer import getCurrentHour, shutdownComputer
from terminal import log
from globalvariables import iso_hour_start, iso_hour_end, restricted_ip_addresses

def isRestrictedTime():
    hour_now = getCurrentHour(format="24-hours")
    return hour_now >= iso_hour_start and hour_now <= iso_hour_end

def isRestrictedIPAddress(ip_address: str):
    return ip_address in restricted_ip_addresses

def main():
    connected_wifi_ip_address = getConnectedWifiIPAddress()

    log("Connected Wi-Fi IP Address", connected_wifi_ip_address)

    if(isRestrictedTime() or isRestrictedIPAddress(connected_wifi_ip_address)):
        shutdownComputer()

if not pyuac.isUserAdmin():
    print("Re-launching as admin!")
    pyuac.runAsAdmin()
else:        
    main()
