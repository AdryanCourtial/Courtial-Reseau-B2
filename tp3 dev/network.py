from is_up import ping
from lookup import lookup
from get_ip import ip
from sys import argv

if(argv[1] == "ping"):
    ping(argv[2])
elif(argv[1] == "lookup"):
    lookup(argv[2])
elif(argv[1] == "ip"):
    ip()