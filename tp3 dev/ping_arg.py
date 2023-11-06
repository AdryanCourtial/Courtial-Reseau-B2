from sys import argv
import os


output = os.system(f"ping {argv[1]}")

if (output == 0):
    print("Ping Succes")
else:
    print("Pring Failled")