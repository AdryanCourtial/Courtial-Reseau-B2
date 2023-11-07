from is_up import ping
from lookup import lookup
from get_ip import ip
# import argparse
from sys import argv

if argv[1] == 'ping':
    result = ping(argv[2])

if argv[1] == 'lookup':
    result = lookup(argv[2])

if argv[1] == 'ip':
    result = ip()

print(result)

# parser = argparse.ArgumentParser()
# parser.add_argument("-p", "--ping", action="store")
# parser.add_argument("-l", "--lookup", action="store_true")
# parser.add_argument("-i", "--ip", action="store_true")
# args = parser.parse_args()
# args['ip'] 
# print(args["ping"])