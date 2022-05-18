import requests
from discord import Webhook, RequestsWebhookAdapter
import colorama
from colorama import Fore
import threading
import time



colorama.init()
def WebHook():
 url = input("Webhook url: ")
 message = input("Message: ")
 threading.Thread(target=WebHook).start()
 while True:
  webhook = Webhook.from_url(f"{url}", adapter=RequestsWebhookAdapter())
  webhook.send(f"{message}")
  print(f"{Fore.GREEN}[+] Sent {message}")
  print(f"{Fore.CYAN}[+] Sent {message}")
  print(f"{Fore.RED}[+] Sent {message} |")
  print(f"{Fore.BLUE}[+] Sent {message} |")
  print(f"{Fore.YELLOW}[+] Sent {message} |")
  print(f"{Fore.WHITE}[+] Sent {message} |")
  print(f"{Fore.GREEN}[+] Sent {message}")
  print(f"{Fore.CYAN}[+] Sent {message}")
  print(f"{Fore.RED}[+] Sent {message} |")
  print(f"{Fore.BLUE}[+] Sent {message} |")
  print(f"{Fore.YELLOW}[+] Sent {message} |")
  print(f"{Fore.WHITE}[+] Sent {message} |")
  print(f"{Fore.GREEN}[+] Sent {message}")
  print(f"{Fore.CYAN}[+] Sent {message}")
  print(f"{Fore.RED}[+] Sent {message} |")
  print(f"{Fore.BLUE}[+] Sent {message} |")
  print(f"{Fore.YELLOW}[+] Sent {message} |")
  print(f"{Fore.WHITE}[+] Sent {message} |")
  print(f"{Fore.GREEN}[+] Sent {message}")
  print(f"{Fore.CYAN}[+] Sent {message}")
  print(f"{Fore.RED}[+] Sent {message} |")
  print(f"{Fore.BLUE}[+] Sent {message} |")
  print(f"{Fore.YELLOW}[+] Sent {message} |")
  print(f"{Fore.WHITE}[+] Sent {message} |")
print(f"""

       {Fore.RED}       ╔═╗╦╦  ╔═╗╔═╗╔═╗╔═╗╔╗╔╔╦╗  ╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═
    {Fore.CYAN}          ╠╣ ║║  ║╣ ╠═╣║ ╦║╣ ║║║ ║   ║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗
   {Fore.BLUE}           ╚  ╩╩═╝╚═╝╩ ╩╚═╝╚═╝╝╚╝ ╩   ╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩

                                                                
{Fore.GREEN}                          ╔═╗╔═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗
{Fore.RED}                          ╚═╗╠═╝╠═╣║║║║║║║╣ ╠╦╝
{Fore.WHITE}                          ╚═╝╩  ╩ ╩╩ ╩╩ ╩╚═╝╩╚═

  
                                                                   


 
                              [1] Start Webhook Spammer
                              [2] Exit 
                                                                             
                                                                            | Github: https://github.com/fileagent
                                                                             | Discord: Faked#2377 """)

allah = input("Select: ")
if allah == '1': 
 WebHook()

