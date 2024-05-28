# import requests

# ip_address = requests.get('http://api.ipify.org').text

# print(ip_address)

# response = requests.get(f'http://ip-api.com/json/{ip_address}?fields=status,message,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,query').json()

# print(response)



import socket
import ctypes
import time

restricted_ip_addresses = ["192.168.1.75"]
program_execution_interval_seconds = 10

while True:
    hostname = socket.gethostname()

    ip_address = socket.gethostbyname(hostname)

    if str(ip_address) in restricted_ip_addresses:
        ctypes.windll.user32.LockWorkStation()
    
    time.sleep(program_execution_interval_seconds)
