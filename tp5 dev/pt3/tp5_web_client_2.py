import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.11', 13337))

request = input("Quelle demmande veut-tu faire au server ?")



s.close()