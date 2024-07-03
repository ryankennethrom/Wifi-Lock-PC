import subprocess
import socket
from devSettings import *

def disableWifi():
    subprocess.run('netsh interface set interface "Wi-Fi" admin=disable', shell=True)

def enableWifi():
    subprocess.run('netsh interface set interface "Wi-Fi" admin=enable', shell=True)

def getConnectedWifiIPAddress() -> str:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return str(ip_address)

def isWifiConnected():
    connected_wifi_ip_address = getConnectedWifiIPAddress()
    return connected_wifi_ip_address != "127.0.0.1"

def isSameSSID(ssid1: str, ssid2: str):
    return ssid1 == ssid2

def getConnectedWifiSSID():
    if not isWifiConnected():
        return None
    else:
        wifi_interface_info = str(subprocess.check_output("netsh wlan show interface", shell=True))
        ssid_index = wifi_interface_info.split().index("SSID")
        ssid_value_index = ssid_index + 2
        acquired_ssid = wifi_interface_info.split()[ssid_value_index][:-4]
        if debugEnabled == True:
            print("Acquired Wifi SSID = " + acquired_ssid)
        return acquired_ssid