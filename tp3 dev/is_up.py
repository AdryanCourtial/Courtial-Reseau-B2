from sys import argv
import os

def ping(ip):
    if (os.system(f"ping {ip} > NULL") == 0):
        print("UP")
    else:
        print("DOWN")