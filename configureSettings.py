from configparser import ConfigParser
import os
from pathlib import Path

def restoreDefaultConfig():
    config = ConfigParser()
    config["USER SETTINGS"] = {
        'restrictedConnections': '',
        'restrictWhenNoWifiConnection':'True',
        'windowsUserName': os.getlogin(),
        'workingDirectory': str(Path.cwd())
    }

    with open(str(Path.cwd())+"\\userSettings.ini", 'w') as f:
        config.write(f)

def restrictSSID(ssid: str):
    restrictedConnections = get("restrictedConnections") 
    if ssid in restrictedConnections:
        return 1
    elif restrictedConnections == "":
        restrictedConnections += ssid
    else:
        restrictedConnections += "," + ssid
    set("restrictedConnections", restrictedConnections)
    return 0

def unRestrictSSID(ssid: str):
    ssid_list = get("restrictedConnections").split(",")
    if ssid not in ssid_list:
        return 1
    else:
        ssid_list.remove(ssid)
        set("restrictedConnections",",".join(ssid_list))
        return 0

def whenNoWifiIsConnected(isComputerRestricted: bool):
    set("restrictWhenNoWifiConnection", str(isComputerRestricted))
    return 0

def get(field:str) -> str:
    config = ConfigParser()
    config.read(str(Path.cwd())+"\\userSettings.ini")
    config_data = config["USER SETTINGS"] 
    return str(config_data[field])

def set(field:str, value:str) -> None:
    config = ConfigParser()
    config.read(str(Path.cwd())+"\\userSettings.ini")
    config_data = config["USER SETTINGS"] 
    config_data[field] = value
    config["USER SETTINGS"] = config_data
    with open(str(Path.cwd())+"\\userSettings.ini", "w") as f:
        config.write(f)


# restrictSSID("Bee")
# restoreDefaultConfig()
# unRestrictSSID("Bee")
# whenNoWifiIsConnected(True)
# set("restrictedConnections", "#TELUS")