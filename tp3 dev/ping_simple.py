import os

output = os.system("ping  8.8.8.8")

if (output == 0):
    print("Ping Succes")
else:
    print("Pring Failled")