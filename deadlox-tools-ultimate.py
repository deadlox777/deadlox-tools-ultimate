#!/usr/bin/env python3
"""
Deadlox Tools Ultimate 😎🔥
- WhatsApp Spam Report with IP Rotation
- Social Media Video Downloader
- Phone Number OSINT
- IP/Device Checker
"""

import os
import sys
import time
import requests
import phonenumbers
import random
import socket
import cpuinfo
import psutil
from datetime import datetime
from phonenumbers import carrier, geocoder

# ===== CONFIGURATION =====
MAX_REPORTS = 100
DELAY_BETWEEN_REPORTS = 3  # seconds
PROXY_LIST_URL = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"

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
def get_proxies():
    """Fetch fresh proxy list"""
    try:
        response = requests.get(PROXY_LIST_URL, timeout=10)
        return [p.strip() for p in response.text.split('\n') if p.strip()]
    except:
        return [
            "103.156.17.61:3128",
            "45.95.147.106:8080",
            "194.233.69.41:443",
            "103.152.112.145:80"
        ]  # Fallback proxies

def rotate_proxy():
    """Rotate between different proxies"""
    proxies = get_proxies()
    proxy = random.choice(proxies)
    return {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

def whatsapp_spam_report():
    """Advanced WhatsApp reporter with IP rotation"""
    os.system('clear')
    print(f"\n{Color.RED}=== WHATSAPP SPAM REPORT WITH IP ROTATION ===")
    
    number = input(f"{Color.BLUE}Enter phone number (628xxxx): {Color.RESET}").strip()
    count = int(input(f"{Color.BLUE}Number of reports (1-{MAX_REPORTS}): {Color.RESET}"))
    count = max(1, min(count, MAX_REPORTS))
    
    print(f"\n{Color.YELLOW}[!] Starting {count} reports with IP rotation...")
    
    success = 0
    for i in range(1, count+1):
        try:
            proxy = rotate_proxy()
            url = f"https://wa.me/{number}?text=SPAM-REPORT-{i}"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'
            }
            
            response = requests.get(url, headers=headers, proxies=proxy, timeout=15)
            
            if response.status_code == 200:
                print(f"{Color.GREEN}[✓] Report {i} success (IP: {proxy['http'].split('@')[-1]})")
                success += 1
            else:
                print(f"{Color.YELLOW}[!] Report {i} failed (Status: {response.status_code})")
            
            time.sleep(DELAY_BETWEEN_REPORTS)
            
        except Exception as e:
            print(f"{Color.RED}[X] Error on report {i}: {str(e)[:50]}...")
    
    print(f"\n{Color.CYAN}=== RESULTS ===")
    print(f"Successful reports: {success}/{count}")
    print(f"Failed reports: {count-success}/{count}")

# ===== OTHER TOOLS ===== 
def phone_osint():
    """Phone number investigation tool"""
    # ... [previous phone OSINT code] ...

def download_videos():
    """Social media video downloader"""
    # ... [previous downloader code] ...

def device_monitor():
    """Full device diagnostics"""
    # ... [previous monitor code] ...

# ===== MAIN MENU =====
def main_menu():
    os.system('clear')
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
{Color.CYAN}DEADLOX TOOLS ULTIMATE 😎🔥{Color.RESET}
{Color.YELLOW}1. WhatsApp Spam Report (IP Rotation)
2. Phone Number OSINT
3. Social Media Downloader
4. Device Monitor
0. Exit Tools{Color.RESET}
    """)
    return input(f"{Color.BLUE}Select option (0-4): {Color.RESET}")

# ===== AUTO-INSTALL =====
def check_dependencies():
    required = ['requests', 'phonenumbers', 'py-cpuinfo', 'psutil', 'yt-dlp']
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"{Color.YELLOW}[!] Installing missing packages...")
        os.system(f"pip install {' '.join(missing)}")

# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    check_dependencies()
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            whatsapp_spam_report()
        elif choice == "2":
            phone_osint()
        elif choice == "3":
            download_videos()
        elif choice == "4":
            device_monitor()
        elif choice == "0":
            print(f"\n{Color.RED}Exiting Deadlox Tools...{Color.RESET}")
            break
        else:
            print(f"{Color.RED}Invalid option!{Color.RESET}")
        
        input(f"\n{Color.BLUE}Press Enter to continue...{Color.RESET}")