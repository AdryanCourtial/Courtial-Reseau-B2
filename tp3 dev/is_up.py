from sys import argv
import os


if(os.system(f"ping {argv[1]} > NULL && rm ./NULL") == 0):
    print("UP")
else:
        print("DOWN")

def ping(ip):
    if (os.system(f"ping {ip} > NULL && rm ./NULL") == 0):
        print("UP")
    else:
        print("DOWN")