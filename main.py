import requests
import time
from datetime import datetime
import colorama

#------Settings------#

channel = 187 # Replace this with your channel ID (Enable Discord Developer Tools and copy the ID)
token = "YOUR-TOKEN-HERE" # Replace this with your token (https://www.youtube.com/watch?v=YEgFvgg7ZPI)

#--------------------#

data = {
    "Authorization": token
}

url = f"https://discord.com/api/v9/channels/{channel}/typing"

print(colorama.Fore.CYAN + "Running...")

while True:
    r = requests.post(url, headers=data)
    if r.status_code == 204:
        color = colorama.Fore.GREEN
    else:
        color = colorama.Fore.RED
    print(colorama.Fore.LIGHTBLACK_EX + str(datetime.now()) + colorama.Fore.RESET +  " | " + color + str(r.status_code))
    time.sleep(7)