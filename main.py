from configureSettings import *
from devSettings import *
from wifi import *
import os
import subprocess
from taskscheduler import unregisterProgram, registerProgram
import pyuac
from personalcomputer import *


def process_exists(process_name): 
    call = 'TASKLIST', '/FI', f'imagename eq {process_name}'
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())

def menu():
    if not os.path.exists(f"{str(Path.cwd())}"+"\\userSettings.ini"):
        restoreDefaultConfig()
    print("===================================================")
    print("Menu")
    print("===================================================")
    print("🛠️ Restricted connections : ")
    print()
    for ssid in get("restrictedConnections").split(","):
        print("-"+ ssid)
    print()
    print("🛠️ Restrict when not connected to wifi: " + get("restrictWhenNoWifiConnection"))
    print()
    print("🛠️ Restrictions active: " + str(process_exists(connectionCheckerName+".exe")))
    print()
    print("Actions: ")
    print("(1) Add a restriction")
    print("(2) Delete a restriction")
    print("(3) Restore default settings")
    print("(4) Toggle restriction when not connected to wifi")
    print("(5) Activate/deactivate restrictions ")
    print("(6) Restrict connected network")
    print("(7) Unrestrict connected network")
    print()
    user_input = str(input("Enter action : "))
    if user_input == "1":
        optionOne()
    elif user_input == "2":
        optionTwo()
    elif user_input == "3":
        optionThree()
    elif user_input == "4":
        optionFour()
    elif user_input == "5":
        if not pyuac.isUserAdmin():
            print("Running as administrator on another window")

            cmd = f"""   Start-Process PowerShell -Verb RunAs "-NoExit -NoProfile -Command `"cd {str(Path.cwd())}; ./{programName+'.exe;5'}`""  """
            
            # Use a list to make it easier to pass argument to subprocess
            listProcess = [
                "powershell.exe",
                "-command",
                cmd
            ]

            # Enjoy the magic
            subprocess.run(listProcess, check=True)
            response = input("You changes will be active in the next start up. Reboot now ? (Y/N) ")
            if (response == "Y"):
                rebootComputer()
            else:
                menu()
        else:
            optionFive()
    elif user_input == "6":
        optionSix()
    elif user_input == "7":
        optionSeven()
    else:
        input("Invalid input ❌ ( Press Any Key ) ")
        menu()

def optionSix():
    ssid = getConnectedWifiSSID()
    result = restrictSSID(ssid)
    if result == 0:
        input("Success ✅ ( Press Any Key ) ")
    elif result == 1:
        input("SSID already restricted ❌ ( Press Any Key ) ")
    menu()

def optionSeven():
    ssid = getConnectedWifiSSID()
    result = unRestrictSSID(ssid)
    if result == 0:
        input("Success ✅ ( Press Any Key ) ")
    elif result == 1:
        input("SSID not restricted in the first place ❌ ( Press Any Key ) ")
    menu()
    
def optionFive():
    if process_exists(connectionCheckerName+".exe"):
        unregisterProgram()
    else:
        registerProgram()

def optionFour():
    if 'True'== get("restrictWhenNoWifiConnection"):
        set("restrictWhenNoWifiConnection", "False")
    else:
        set("restrictWhenNoWifiConnection", "True")
    input("Success ✅ ( Press Any Key ) ")
    menu()

def optionOne():
    ssid = str(input("Enter SSID to restrict: "))
    if process_exists(connectionCheckerName+".exe") and isSameSSID(ssid, getConnectedWifiSSID()):
        user_input = input("Are you sure ? You will immediately be locked out. (Y/N) ")
        if user_input != "Y":
            input("Network not restricted ❌ ( Press Any Key ) ")
            menu()
        else:
            result = restrictSSID(ssid)
            if result == 0:
                input("Success ✅ ( Press Any Key ) ")
            elif result == 1:
                input("SSID already restricted ❌ ( Press Any Key ) ")
            menu() 
    else:
        result = restrictSSID(ssid)
        if result == 0:
            input("Success ✅ ( Press Any Key ) ")
        elif result == 1:
            input("SSID already restricted ❌ ( Press Any Key ) ")
        menu()

def optionTwo():
    ssid = str(input("Enter SSID to unrestrict : "))
    result = unRestrictSSID(ssid)
    if result == 0:
        input("Success ✅ ( Press Any Key ) ")
    elif result == 1:
        input("SSID not restricted ❌ ( Press Any Key ) ")
    menu()

def optionThree():
    user_input = input("Type 'Yes' to restore default setting : ")
    if user_input == "Yes":
        restoreDefaultConfig()
        input("Success ✅ ( Press Any Key ) ")
    else:
        input("Wrong input. Restorement failed. ❌ ( Press Any Key ) ")
    menu()

if __name__ == "__main__":
    menu()