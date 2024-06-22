import os
import time
import subprocess
from colorama import init, Fore, Style

os.system("color 4")

def load_proxies():
    print("Conecting to server...")
    for i in range(5):
        time.sleep(0.1)
        print(".", end='', flush=True)
    time.sleep(1)
    print("\nConecting succes!")
    time.sleep(0.5)
    print("Disabeling security...")
    for i in range(5):
        time.sleep(0.1)
        print(".", end='', flush=True)
    time.sleep(1)
    print("\nSecurity disabeld!")
    time.sleep(0.5)

with open('Tools/proxies.txt') as f:
    proxies = f.readlines()
    
load_proxies()

init(autoreset=True)


options = [
    "TokenBruteforce",
    "WebhookSpam",
    "NitroCheck",
    "Vanity Checker",
    "Gmail BruteForce",
    "Server Nuker",
    "Email Spam",
    "Ip ImageLogger",
    "TokenLogger",
    "DDOS",
    "NitroGen",
    "ServerJoiner",
    "TokenGen",
    "Discord Spam",
    "ID To Token",
    "Token Checker",
    "BotNetDDOS",
    "Stresser",
    "IP Pinger",
    "Spammer",
    "Image logger grabber",
]


print(F"{Fore.RED}     ███████        ████████        ████████           ████████        ████████   ██          ██")
print(F"{Fore.RED}    ██            ██               ██      ██         ██      ██       ██     ██    ██      ██")
time.sleep(0.1) 
print(F"{Fore.RED}    ██          ██                ██        ██       ██        ██      ██     ██      ██  ██")
time.sleep(0.1)
print(F"{Fore.RED}     ██████    ██                ██          ██     ██          ██     ████████         ██")
time.sleep(0.1)   
print(F"{Fore.RED}          ██    ██                ██        ██       ██        ██      ██     ██        ██")
time.sleep(0.1)          
print(F"{Fore.RED}          ██      ██               ██      ██         ██      ██       ██     ██        ██")
time.sleep(0.1)
print(F"{Fore.RED}    ███████         ████████        ████████           ████████        ████████         ██")
time.sleep(0.1)

print(F"{Fore.RED}Made by monkeydanceboy!")
time.sleep(2)                                     

os.system("color 4")



print(F"{Fore.RED}If Your Done Using a Tool Press Control + C To Go back to Menu")


def menu():
    while True:
        
        print(Fore.RED + "\nChoose an option:\n")
        for i in range(len(options)):
            print(Fore.RED + str(i+1) + ". " + options[i])

        # Get the user's choice
        choice = input(Fore.RED + "\nEnter the number of your choice: ")

        # Run the chosen script, if it exists
        try:
            script_name = options[int(choice)-1]
            if script_name == "TokenBruteforce":
                subprocess.call(["python", "Tools/TokenBruteforce.py"])
            elif script_name == "WebhookSpam":
                subprocess.call(["python", "Tools/WebhookSpam.py"])
            elif script_name == "NitroCheck":
                subprocess.call(["python", "Tools/NitroCheck.py"])
            elif script_name == "Vanity Checker":
                subprocess.call(["python", "Tools/Vanity Checker.py"])
            elif script_name == "Gmail BruteForce":
                subprocess.call(["python", "Tools/Gmail BruteForce.py"])
            elif script_name == "Server Nuker":
                subprocess.call(["python", "Tools/Server Nuker.py"])
            elif script_name == "Email Spam":
                subprocess.call(["python", "Tools/Email Spam.py"])
            elif script_name ==  "Ip ImageLogger":
                subprocess.call(["python", "Tools/Ip ImageLogger.py"])
            elif script_name ==  "TokenLogger":
                subprocess.call(["python", "Tools/TokenLogger.py"])
            elif script_name ==  "DDOS":
                subprocess.call(["python", "Tools/DDOS.py"])
            elif script_name ==  "NitroGen":
                subprocess.call(["python", "Tools/NitroGen.py"])
            elif script_name ==  "ServerJoiner":
                subprocess.call(["python", "Tools/ServerJoiner.py"])
            elif script_name ==  "TokenGen":
                subprocess.call(["python", "Tools/TokenGen.py"])
            elif script_name ==  "Discord Spam":
                subprocess.call(["python", "Tools/Discord Spam.py"])
            elif script_name ==  "ID To Token":
                subprocess.call(["python", "Tools/ID To Token.py"])
            elif script_name ==  "Token Checker":
                subprocess.call(["python", "Tools/Token Checker.py"])
            elif script_name ==  "BotNetDDOS":
                subprocess.call(["python", "Tools/BotNetDDOS.py"])
            elif script_name ==  "Stresser":
                subprocess.call(["python", "Tools/Stresser.py"])
            elif script_name ==  "IP Pinger":
                subprocess.call(["python", "Tools/IP Pinger.py"])
            elif script_name == "Spammer":
                subprocess.call(["python", "Spammer.py"])
            elif script_name == "Image logger grabber":
                subprocess.call(["vbs", "Image logger grabber.vbs"])
                
        except:
            print

if __name__ == "__main__":
    menu()
