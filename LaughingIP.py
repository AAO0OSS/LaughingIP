import os
import urllib.request
from colorama import init, Fore, Back

init(autoreset=True)

def clear_screen():
    if os.name == 'posix':  
        os.system('clear')
    elif os.name == 'nt':   
        os.system('cls')

def ask_to_exit():
    while True:
        user_input = input("Do you really want to exit? (yes/no): ")
        if user_input.lower() == 'yes':
            exit()
        elif user_input.lower() == 'no':
            return

while True: 
    clear_screen()

    print(Back.RED + Fore.WHITE + "LaughingIP")
    print("Made by AAO0OSS")
    print("FOLLOW ME IN GITHUB :)")
    print("https://www.github.com/AAO0OSS")

    try:
        target = input("\nEnter The IP Here...It Can Be IPv4 Or IPv6 : ")
    except KeyboardInterrupt:
        ask_to_exit()
        continue

    url = "http://ip-api.com/json/" + target
    data = urllib.request.urlopen(url).read().decode("utf-8")
    data2 = eval(data)

    print("\n" + Back.RED + Fore.WHITE + "[ # ] LET'S FUCKING GO!!! >>>")

    print(Fore.RED + "[ $ ] AS:", str(data2["as"]))
    print(Fore.RED + "[ $ ] COUNTRY:", str(data2["country"]))
    print(Fore.RED + "[ $ ] CITY:", str(data2["city"]))
    print(Fore.RED + "[ $ ] COUNTRY CODE:", str(data2["countryCode"]))
    print(Fore.RED + "[ $ ] ISP:", str(data2["isp"]))
    print(Fore.RED + "[ $ ] LATITUDE:", str(data2["lat"]))
    print(Fore.RED + "[ $ ] LONGITUDE:", str(data2["lon"]))
    print(Fore.RED + "[ $ ] ORG:", str(data2["org"]))
    print(Fore.RED + "[ $ ] QUERY:", str(data2["query"]))
    print(Fore.RED + "[ $ ] REGION:", str(data2["region"]))
    print(Fore.RED + "[ $ ] REGION NAME:", str(data2["regionName"]))
    print(Fore.RED + "[ $ ] TIME ZONE:", str(data2["timezone"]))
    print(Fore.RED + "[ $ ] ZIP:", str(data2["zip"]))
    print(Fore.RED + "[ $ ] STATUS:", str(data2["status"]))
    print(Fore.CYAN + "[ $ ] SAY THANKS FOR USING")

    try:
        another = input("\nDo you want to enter another IP? (yes/no): ")
    except KeyboardInterrupt:
        ask_to_exit()
        continue

    if another.lower() != "yes":
        ask_to_exit()