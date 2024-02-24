#An application that attempts to connect to a website or server every so many minutes or a given time and check if it is up. If it is down, it will notify you by posting a notice on screen. 

import requests
import time
from datetime import datetime

def check_website(url):
    try:
        response = requests.get(url)
        # Check if the status code is 2xx (indicating success)
        if response.status_code // 100 == 2:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

def notify():
    print(f"[{datetime.now()}] Website is down! Notify the user.")

def main():
    website_url = input("Enter the website URL to monitor: ")
    check_interval_minutes = int(input("Enter the check interval in minutes: "))

    while True:
        if not check_website(website_url):
            notify()

        time.sleep(check_interval_minutes * 60)  # Sleep for the specified interval

if __name__ == "__main__":
    main()
