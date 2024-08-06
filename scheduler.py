from windowsscheduler import Registry
from userpreference import UserPreference
import pyuac

if "__main__" == __name__:
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else: 
        registry = Registry()
        userPreference = UserPreference()

        registry.unregisterProgram() if userPreference.isRestrictionsActive() else registry.registerProgram()