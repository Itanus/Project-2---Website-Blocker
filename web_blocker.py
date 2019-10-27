import time
from datetime import datetime as dt


host_path = r"C:\Windows\System32\drivers\etc\hosts"                #directory in which needed file is located
redirect = "127.0.0.1"
websites = ["www.amazon.com", "amazon.com"]                         #list of websites that are going to be blocked
hour_start = input("Starting hour of the blockade?:\n")
hour_end = input("Ending hour of the blockade?:\n")

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, int(hour_start)) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, int(hour_end)):
        print("Blocking\n")
        with open(host_path, "r+") as file:
            content = file.read()
            for website in websites:
                if website in  content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Blockade lifted\n")
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)