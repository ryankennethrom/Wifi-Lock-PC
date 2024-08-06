from configureSettings import *
from devSettings import *
from wifi import *
import os
import subprocess
from taskscheduler import unregisterProgram, registerProgram
import pyuac
from personalcomputer import *
from userpreference import UserPreference

    
def menu():
    if not os.path.exists(f"{str(Path.cwd())}"+"\\userSettings.ini"):
        restoreDefaultConfig()
    userPreference = UserPreference()
    is_restrictions_active = userPreference.isRestrictionsActive()
    print("===================================================")
    print("Menu")
    print("===================================================")
    print("🛠️ Restricted connections : ")
    print()
    for ssid in get("restrictedConnections").split(","):
        print("-"+ ssid)
    print()
    print("A) Lock PC when not connected to wifi: " + get("restrictWhenNoWifiConnection"))
    print()
    print("B) Restrictions active in next boot up: " + str(is_restrictions_active))
    print()
    print("Actions: ")
    print("(1) Add a restriction")
    print("(2) Delete a restriction")
    print("(3) Restore default settings")
    print("(4) Toggle A")
    print("(5) Toggle B")
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
    else:
        input("Invalid input ❌ ( Press Any Key ) ")
        menu()
    
def optionFive():
    userPreference = UserPreference()
    if userPreference.isRestrictionsActive():
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
    userPreference = UserPreference()
    if userPreference.isRestrictionsActive() and isSameSSID(ssid, getConnectedWifiSSID()):
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