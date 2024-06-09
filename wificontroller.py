import subprocess
import socket

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