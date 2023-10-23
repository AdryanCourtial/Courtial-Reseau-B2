afficher ses cartes réseau :

```
[Adryan@node1 baptiste]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:27:8b:bf brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe27:8bbf/64 scope link
       valid_lft forever preferred_lft forever
[Adryan@node1 baptiste]$
```

afficher sa table de routage

```
[baptiste@node1 ~]$ ip route
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.11 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s3 proto static metric 100
[baptiste@node1 ~]$
```

prouvez qu'il peut joindre node2.lan2.tp2 :

```
[baptiste@node1 ~]$ ping 10.1.2.12
PING 10.1.2.12 (10.1.2.12) 56(84) bytes of data.
64 bytes from 10.1.2.12: icmp_seq=1 ttl=63 time=2.78 ms
64 bytes from 10.1.2.12: icmp_seq=2 ttl=63 time=1.08 ms
64 bytes from 10.1.2.12: icmp_seq=3 ttl=63 time=1.24 ms
64 bytes from 10.1.2.12: icmp_seq=4 ttl=63 time=1.16 ms
64 bytes from 10.1.2.12: icmp_seq=5 ttl=63 time=1.23 ms
64 bytes from 10.1.2.12: icmp_seq=6 ttl=63 time=1.42 ms
64 bytes from 10.1.2.12: icmp_seq=7 ttl=63 time=1.30 ms
^C
--- 10.1.2.12 ping statistics ---
7 packets transmitted, 7 received, 0% packet loss, time 6012ms
rtt min/avg/max/mdev = 1.082/1.458/2.784/0.549 ms
[baptiste@node1 ~]$
```

prouvez avec un traceroute que le paquet passe bien par router.tp2 : 

```
[baptiste@node1 ~]$ traceroute 10.1.2.12
traceroute to 10.1.2.12 (10.1.2.12), 30 hops max, 60 byte packets
 1  10.1.1.254 (10.1.1.254)  4.897 ms  3.915 ms  3.740 ms
 2  10.1.2.12 (10.1.2.12)  3.381 ms !X  3.121 ms !X  2.953 ms !X
[baptiste@node1 ~]$
```

Sur router.tp2

prouvez que vous avez un accès internet (ping d'une IP publique) :

```
[baptiste@router ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=56 time=15.0 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=56 time=14.2 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=56 time=15.3 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=56 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=56 time=13.8 ms
64 bytes from 8.8.8.8: icmp_seq=6 ttl=56 time=14.3 ms
^C
--- 8.8.8.8 ping statistics ---
6 packets transmitted, 6 received, 0% packet loss, time 5011ms
rtt min/avg/max/mdev = 13.584/14.357/15.270/0.610 ms
[baptiste@router ~]$
```

prouvez que vous pouvez résoudre des noms publics (ping d'un nom de domaine public) :

```
[baptiste@router ~]$ ping google.com
PING google.com (142.250.200.206) 56(84) bytes of data.
64 bytes from mrs08s17-in-f14.1e100.net (142.250.200.206): icmp_seq=1 ttl=56 time=12.5 ms
64 bytes from mrs08s17-in-f14.1e100.net (142.250.200.206): icmp_seq=2 ttl=56 time=13.3 ms
64 bytes from mrs08s17-in-f14.1e100.net (142.250.200.206): icmp_seq=3 ttl=56 time=13.6 ms
64 bytes from mrs08s17-in-f14.1e100.net (142.250.200.206): icmp_seq=4 ttl=56 time=13.5 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 12.486/13.243/13.644/0.451 ms
[baptiste@router ~]$
```

ajoutez une route par défaut sur les deux machines du LAN1 : 
```
[baptiste@node2 ~]$ sudo ip route add default via 10.1.1.254 dev enp0s3
[sudo] password for baptiste:
[baptiste@node2 ~]$ ip route
default via 10.1.1.254 dev enp0s3
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.12 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s3 proto static metric 100
[baptiste@node2 ~]$
```
```
[baptiste@node2 ~]$ sudo ip route add default via 10.1.2.254 dev enp0s3
[sudo] password for baptiste:
[baptiste@node2 ~]$ ip route
default via 10.1.2.254 dev enp0s3
10.1.1.0/24 via 10.1.2.254 dev enp0s3 proto static metric 100
10.1.2.0/24 dev enp0s3 proto kernel scope link src 10.1.2.12 metric 100
[baptiste@node2 ~]$
```

ajoutez une route par défaut sur les deux machines du LAN2 : 

```
[baptiste@node1 ~]$ sudo ip route add default via 10.1.2.254 dev enp0s3
[sudo] password for baptiste:
[baptiste@node1 ~]$ ip route
default via 10.1.2.254 dev enp0s3
10.1.1.0/24 via 10.1.2.254 dev enp0s3 proto static metric 100
10.1.2.0/24 dev enp0s3 proto kernel scope link src 10.1.2.11 metric 100
[baptiste@node1 ~]$
```

```
[baptiste@node2 ~]$ sudo ip route add default via 10.1.2.254 dev enp0s3
[sudo] password for baptiste:
[baptiste@node2 ~]$ ip route
default via 10.1.2.254 dev enp0s3
10.1.1.0/24 via 10.1.2.254 dev enp0s3 proto static metric 100
10.1.2.0/24 dev enp0s3 proto kernel scope link src 10.1.2.12 metric 100
[baptiste@node2 ~]$
```

dans le compte-rendu, mettez-moi que la conf des points précédents sur node2.lan1.tp2 :

```
[baptiste@node2 ~]$ cat /etc/resolv.conf
nameserver 8.8.8.8
[baptiste@node2 ~]$
```
prouvez que node2.lan1.tp2 a un accès internet :

il peut ping une IP publique : 

```
[baptiste@node1 ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=55 time=15.5 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=55 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=55 time=17.0 ms
^C
--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 13.575/15.377/17.042/1.418 ms
[baptiste@node1 ~]$
```


il peut ping un nom de domaine public :

```
[baptiste@node2 ~]$ ping google.com
PING google.com (172.217.21.14) 56(84) bytes of data.
64 bytes from muc11s13-in-f14.1e100.net (172.217.21.14): icmp_seq=1 ttl=114 time=14.7 ms
64 bytes from mrs09s10-in-f14.1e100.net (172.217.21.14): icmp_seq=2 ttl=114 time=14.7 ms
64 bytes from mrs09s10-in-f14.1e100.net (172.217.21.14): icmp_seq=3 ttl=114 time=14.3 ms
^C
--- google.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 14.280/14.536/14.676/0.181 ms
[baptiste@node2 ~]$
```

changez son adresse IP en 10.1.1.253 : 

```
[baptiste@DHCP ~]$ sudo nano /etc/sysconfig/network-scripts/ifcfg-enp0s3
[baptiste@DHCP ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:75:1b:41 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.12/24 brd 10.1.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe75:1b41/64 scope link
       valid_lft forever preferred_lft forever
[baptiste@DHCP ~]$ sudo nmcli con reload
[baptiste@DHCP ~]$ nmcli con up enp0s3
```

setup du serveur DHCP : 

```
[baptiste@DHCP ~]$ sudo dnf -y install dhcp-server
Rocky Linux 9 - BaseOS                                                7.9 kB/s | 4.1 kB     00:00
Rocky Linux 9 - BaseOS                                                3.4 MB/s | 1.9 MB     00:00
Rocky Linux 9 - AppStream                                              14 kB/s | 4.5 kB     00:00
Rocky Linux 9 - AppStream                                             9.5 MB/s | 7.1 MB     00:00
Rocky Linux 9 - Extras                                                9.1 kB/s | 2.9 kB     00:00
Rocky Linux 9 - Extras                                                 17 kB/s |  11 kB     00:00
Dependencies resolved.
```


```
[baptiste@DHCP ~]$ cat /etc/dhcp/dhcpd.conf
cat: /etc/dhcp/dhcpd.conf: Permission denied
[baptiste@DHCP ~]$ sudo !!
sudo cat /etc/dhcp/dhcpd.conf
# create new
# specify domain name
option domain-name     "srv.world";
# specify DNS server's hostname or IP address
option domain-name-servers     dlp.srv.world;
# default lease time
default-lease-time 600;
# max lease time
max-lease-time 7200;
# this DHCP server to be declared valid
authoritative;# specify network address and subnetmask
subnet 10.1.1.0 netmask 255.255.255.0 {
    # specify the range of lease IP address
    range dynamic-bootp 10.1.1.100 10.1.1.200;
    # specify broadcast address
    option broadcast-address 10.1.1.255;
    option domain-name-servers 1.1.1.1;
    # specify gateway
    option routers 10.1.1.254;
}#
[baptiste@DHCP ~]$
```

```
[baptiste@node1 ~]$ sudo dnf -y install dhcp-client
[sudo] password for baptiste:
Last metadata expiration check: 0:35:54 ago on Mon 23 Oct 2023 09:37:03 PM CEST.
Dependencies resolved.
========================================================================================================================
 Package                         Architecture          Version                           Repository                Size
========================================================================================================================
Installing:
 dhcp-client                     x86_64                12:4.4.2-18.b1.el9                baseos                   788 k
Installing dependencies:
 dhcp-common                     noarch                12:4.4.2-18.b1.el9                baseos                   128 k
 ipcalc                          x86_64                1.0.0-5.el9                       baseos                    41 k
Installing weak dependencies:
 geolite2-city                   noarch                20191217-6.el9                    appstream                 23 M
 geolite2-country

 [...]

[baptiste@node1 ~]$ sudo nmcli connection modify enp0s3 ipv4.method auto
[baptiste@node1 ~]$ nmcli connection down enp0s3; nmcli connection up enp0s3
Error: 'enp0s3' is not an active connection.
[baptiste@node1 ~]$ sudo nmcli connection down enp0s3; sudo nmcli connection up enp0s3
Error: 'enp0s3' is not an active connection.
Error: no active connection provided.
client_loop: send disconnect: Connection reset
```

```
[baptiste@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:27:8b:bf brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.100/24 brd 10.1.1.255 scope global dynamic noprefixroute enp0s3
       valid_lft 326sec preferred_lft 326sec
    inet6 fe80::a00:27ff:fe27:8bbf/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
[baptiste@node1 ~]$
```

```
[baptiste@node1 ~]$ ip route
default via 10.1.1.254 dev enp0s3 proto dhcp src 10.1.1.100 metric 100
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.100 metric 100
[baptiste@node1 ~]$
```

