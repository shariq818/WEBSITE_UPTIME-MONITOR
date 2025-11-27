# Website Uptime Monitor v1.1
# Author: Paradox (shariq818)

import requests
import time
from datetime import datetime
from colorama import Fore, Style

def check_websites(urls, interval=10):
    urls = [u.strip() for u in urls if u.strip()]

    while True:
        print("\n--- Checking Websites ---")
        with open("uptime_log.txt", "a") as log:
            for url in urls:
                try:
                    start = time.time()
                    r = requests.get(url, timeout=5)
                    elapsed = round((time.time() - start) * 1000, 2)

                    status = "UP" if r.status_code == 200 else f"DOWN ({r.status_code})"
                    color = Fore.GREEN if r.status_code == 200 else Fore.RED

                    print(f"{color}{url} — {status} — {elapsed} ms{Style.RESET_ALL}")
                    log.write(f"{datetime.now()} | {url} | {status} | {elapsed} ms\n")

                except Exception as e:
                    print(f"{Fore.RED}{url} — DOWN — {e}{Style.RESET_ALL}")
                    log.write(f"{datetime.now()} | {url} | DOWN | {e}\n")

        time.sleep(interval)


if __name__ == "__main__":
    raw_urls = input("Paste URLs separated by commas: ")
    interval = input("Check interval in seconds [default 10]: ")
    interval = int(interval) if interval.strip() else 10

    urls = raw_urls.split(",")
    check_websites(urls, interval)