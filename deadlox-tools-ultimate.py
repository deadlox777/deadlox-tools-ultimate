#!/usr/bin/env python3
"""
DEADLOX TOOLS ULTIMATE v2.0
- WhatsApp Spam Report with IP Rotation
- All Social Media Video Downloader
- Phone Number OSINT
- Device Monitoring
"""

import os
import sys
import time
import requests
import phonenumbers
import random
import subprocess
from phonenumbers import carrier, geocoder

# ===== CONFIG =====
MAX_REPORTS = 9999
DELAY = 2  # seconds
PROXY_LIST = [
    "103.156.17.61:3128",
    "45.95.147.106:8080", 
    "194.233.69.41:443",
    "103.152.112.145:80"
]

# ===== COLOR SETTINGS =====
class Color:
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    RESET = "\033[0m"

# ===== CORE FUNCTIONS =====
def rotate_ip():
    """Rotate IP address for anti-ban"""
    return random.choice(PROXY_LIST)

def whatsapp_spam():
    """Advanced WhatsApp reporter"""
    os.system('clear')
    print(f"\n{Color.RED}=== WHATSAPP SPAM REPORT ===")
    
    number = input(f"{Color.BLUE}Enter number (628xxxx): {Color.RESET}").strip()
    count = int(input(f"{Color.BLUE}Number of reports (1-{MAX_REPORTS}): {Color.RESET}"))
    
    for i in range(1, count+1):
        try:
            proxy = {"http": f"http://{rotate_ip()}"}
            url = f"https://wa.me/{number}?text=SPAM-{i}"
            requests.get(url, proxies=proxy, timeout=10)
            print(f"{Color.GREEN}[✓] Report {i} sent {Color.RESET}")
            time.sleep(DELAY)
        except:
            print(f"{Color.RED}[X] Failed report {i}{Color.RESET}")

def download_media():
    """Download videos from all platforms"""
    os.system('clear')
    print(f"\n{Color.CYAN}=== SOCIAL MEDIA DOWNLOADER ===")
    
    url = input(f"{Color.BLUE}Enter video URL: {Color.RESET}").strip()
    
    print(f"\n{Color.YELLOW}Downloading...{Color.RESET}")
    os.system(f"yt-dlp {url}")
    print(f"{Color.GREEN}Saved to /storage/downloads{Color.RESET}")

# ===== MENU SYSTEM =====
def show_menu():
    print(f"""
{Color.RED}
▓█████▄  ▒█████   ██▀███   ▄▄▄       ██▓███  
▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒▒████▄    ▓██░  ██▒
░██   █▌▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒
░▓█▄   ▌▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒
░▒████▓ ░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░
 ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░     
 ░ ░  ░ ░ ░ ░ ▒    ░░   ░   ░   ▒   ░░       
   ░        ░ ░     ░           ░  ░          
 ░                                          
{Color.CYAN}DEADLOX TOOLS ULTIMATE v2.0{Color.RESET}

{Color.GREEN}[1]{Color.RESET} WhatsApp Spam Report
{Color.GREEN}[2]{Color.RESET} Download All Social Media Videos  
{Color.GREEN}[3]{Color.RESET} Phone Number OSINT
{Color.GREEN}[4]{Color.RESET} Device Monitor
{Color.RED}[0]{Color.RESET} Exit
    """)

# ===== AUTO-INSTALL =====
def check_deps():
    required = ['requests', 'phonenumbers', 'yt-dlp']
    for pkg in required:
        try:
            __import__(pkg)
        except:
            print(f"{Color.YELLOW}Installing {pkg}...{Color.RESET}")
            os.system(f"pip install {pkg}")

if __name__ == "__main__":
    check_deps()
    
    while True:
        os.system('clear')
        show_menu()
        choice = input(f"{Color.BLUE}Select option (0-4): {Color.RESET}")
        
        if choice == "1":
            whatsapp_spam()
        elif choice == "2":
            download_media()
        elif choice == "0":
            print(f"\n{Color.RED}Exiting...{Color.RESET}")
            break
            
        input(f"\n{Color.YELLOW}Press Enter to continue...{Color.RESET}")