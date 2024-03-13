import requests, os
from colorama import Fore

os.system("cls")

def send_message(webhook, message):
    payload = {
        'content': message,
        'username': "Nexus Spammer",
        'avatar_url': "https://cdn.discordapp.com/attachments/1209895707675205653/1209919950689411092/RmDJt7xVhNFTA6yvy3EWfsTbki45EeI67K93h75F_1.png?ex=65fb21c3&is=65e8acc3&hm=a6a6cbe10a14960ebb96ab983a543111b73d4b5344d534b631f9a62b798432f2&"
    }
    response = requests.post(webhook, json=payload)
    if response.status_code == 204:
        print(f"{Fore.LIGHTGREEN_EX}SUCCSES {Fore.LIGHTWHITE_EX}Message Send! -> {Fore.LIGHTBLACK_EX}({response.status_code})")
    else:
        print(f"{Fore.RED}ERROR {Fore.LIGHTWHITE_EX}FAILED! -> {Fore.LIGHTBLACK_EX}({response.status_code})")

def main():
    print(f'''{Fore.LIGHTMAGENTA_EX}
                    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                    ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗█████╗██║   ██║   ██║██║   ██║██║     ███████╗
                    ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
                    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                discord.gg/nexus-tools
    ''')
    webhook = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter Webhook: ")
    message = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter Message To Spam: ")
    while True:
        send_message(webhook, message)

main()
