import os

hosts = ["8.8.8.8", "google.com", "localhost"]

for host in hosts:
    print(f"Pinging {host}")
    os.system(f"ping -n 2 {host}")
