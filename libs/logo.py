# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
\033[34m▪   ▐ ▄ .▄▄ · ▄▄▄▄▄ ▄▄▄·  ▄▄ • ▄▄▄   ▄▄▄· • ▌ ▄ ·.    \033[35m ▄▄▄  ▄▄▄ . ▄▄▄·      ▄▄▄  ▄▄▄▄▄
\033[34m██ •█▌▐█▐█ ▀. •██  ▐█ ▀█ ▐█ ▀ ▪▀▄ █·▐█ ▀█ ·██ ▐███▪   \033[35m ▀▄ █·▀▄.▀·▐█ ▄█▪     ▀▄ █·•██  
\033[34m▐█·▐█▐▐▌▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▄█ ▀█▄▐▀▀▄ ▄█▀▀█ ▐█ ▌▐▌▐█·   \033[35m ▐▀▀▄ ▐▀▀▪▄ ██▀· ▄█▀▄ ▐▀▀▄  ▐█.▪
\033[34m▐█▌██▐█▌▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▄▪▐█▐█•█▌▐█ ▪▐▌██ ██▌▐█▌   \033[35m ▐█•█▌▐█▄▄▌▐█▪·•▐█▌.▐▌▐█•█▌ ▐█▌·
\033[34m▀▀▀▀▀ █▪ ▀▀▀▀  ▀▀▀  ▀  ▀ ·▀▀▀▀ .▀  ▀ ▀  ▀ ▀▀  █▪▀▀▀   \033[35m .▀  ▀ ▀▀▀ .▀    ▀█▄▀▪.▀  ▀ ▀▀▀   """



def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.YELLOW + "      https://discord.gg/WMhdGvBWA8"+ Style.RESET_ALL + Style.BRIGHT)
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
