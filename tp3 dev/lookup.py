import socket
from sys import argv

# result = socket.gethostbyname(f"{argv[1]}")
# print(result)

def lookup(a):
    result = socket.gethostbyname(f"{a}")
    print(result)