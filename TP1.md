- l'adresse MAC de votre carte WiFi :


```
PS C:\Users\happy cash> ipconfig /all

Configuration IP de Windows

Carte réseau sans fil Wi-Fi :
[...]

   Suffixe DNS propre à la connexion. . . :
   Description. . . . . . . . . . . . . . : Intel(R) Wi-Fi 6 AX201 160MHz
   Adresse physique . . . . . . . . . . . : 84-14-4D-0E-5E-B1 <====================== ici
   DHCP activé. . . . . . . . . . . . . . : Oui
   Configuration automatique activée. . . : Oui
   Adresse IPv6 de liaison locale. . . . .: fe80::bfb6:af78:1751:6490%11(préféré)
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.76.229(préféré)
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0
   Bail obtenu. . . . . . . . . . . . . . : jeudi 12 octobre 2023 14:17:47
   Bail expirant. . . . . . . . . . . . . : vendredi 13 octobre 2023 13:58:33
   Passerelle par défaut. . . . . . . . . : 10.33.79.254
   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
   IAID DHCPv6 . . . . . . . . . . . : 126096461
   DUID de client DHCPv6. . . . . . . . : 00-01-00-01-29-5A-4E-04-C8-5A-CF-B7-B4-DA
   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
   NetBIOS sur Tcpip. . . . . . . . . . . : Activé

[...]
```

l'adresse IP de votre carte WiFi :

```
PS C:\Users\happy cash> ipconfig /all

Configuration IP de Windows

Carte réseau sans fil Wi-Fi :
[...]

   Suffixe DNS propre à la connexion. . . :
   Description. . . . . . . . . . . . . . : Intel(R) Wi-Fi 6 AX201 160MHz
   Adresse physique . . . . . . . . . . . : 84-14-4D-0E-5E-B1 
   DHCP activé. . . . . . . . . . . . . . : Oui
   Configuration automatique activée. . . : Oui
   Adresse IPv6 de liaison locale. . . . .: fe80::bfb6:af78:1751:6490%11(préféré)
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.76.229(préféré) <====================== ici
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0
   Bail obtenu. . . . . . . . . . . . . . : jeudi 12 octobre 2023 14:17:47
   Bail expirant. . . . . . . . . . . . . : vendredi 13 octobre 2023 13:58:33
   Passerelle par défaut. . . . . . . . . : 10.33.79.254
   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
   IAID DHCPv6 . . . . . . . . . . . : 126096461
   DUID de client DHCPv6. . . . . . . . : 00-01-00-01-29-5A-4E-04-C8-5A-CF-B7-B4-DA
   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
   NetBIOS sur Tcpip. . . . . . . . . . . : Activé

[...]
```

le masque de sous-réseau du réseau LAN auquel vous êtes connectés en WiFi :

```
PS C:\Users\happy cash> ipconfig /all

Configuration IP de Windows

Carte réseau sans fil Wi-Fi :
[...]

   Suffixe DNS propre à la connexion. . . :
   Description. . . . . . . . . . . . . . : Intel(R) Wi-Fi 6 AX201 160MHz
   Adresse physique . . . . . . . . . . . : 84-14-4D-0E-5E-B1 
   DHCP activé. . . . . . . . . . . . . . : Oui
   Configuration automatique activée. . . : Oui
   Adresse IPv6 de liaison locale. . . . .: fe80::bfb6:af78:1751:6490%11(préféré)
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.76.229(préféré) 
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0 <====================== 10.33.76.229/20
   Bail obtenu. . . . . . . . . . . . . . : jeudi 12 octobre 2023 14:17:47
   Bail expirant. . . . . . . . . . . . . : vendredi 13 octobre 2023 13:58:33
   Passerelle par défaut. . . . . . . . . : 10.33.79.254
   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
   IAID DHCPv6 . . . . . . . . . . . : 126096461
   DUID de client DHCPv6. . . . . . . . : 00-01-00-01-29-5A-4E-04-C8-5A-CF-B7-B4-DA
   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
   NetBIOS sur Tcpip. . . . . . . . . . . : Activé

[...]
```

l'adresse de réseau du LAN auquel vous êtes connectés en WiFi:

```
    10.33.64.0
```

l'adresse de broadcast :

```
    10.33.79.255
```

le nombre d'adresses IP disponibles dans ce réseau : 

```
    4,094 Usable
```

déterminer le hostname de votre PC :

```
PS C:\Users\happy cash> hostname
Adryx-LAPTOP
```

l'adresse IP de la passerelle du réseau :
```
PS C:\Users\happy cash> ipconfig
[...]

Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . :
   Adresse IPv6. . . . . . . . . . . . . .: 2a04:cec0:1130:fee8:c389:9875:1c07:ed1
   Adresse IPv6 temporaire . . . . . . . .: 2a04:cec0:1130:fee8:a468:c8e7:d69c:d0f2
   Adresse IPv6 de liaison locale. . . . .: fe80::bfb6:af78:1751:6490%11
   Adresse IPv4. . . . . . . . . . . . . .: 172.20.10.2
   Masque de sous-réseau. . . . . . . . . : 255.255.255.240
   Passerelle par défaut. . . . . . . . . : fe80::3853:9cff:fecb:f64%11 <================== Ici
                                       172.20.10.1 =====================ici
[...]
```
```
PS C:\Users\happy cash> arp -a
[...]
Interface : 172.20.10.2 --- 0xb
  Adresse Internet      Adresse physique      Type
  172.20.10.1           3a-53-9c-cb-0f-64     dynamique <====== ici
  172.20.10.15          ff-ff-ff-ff-ff-ff     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique
  [...]
```

l'adresse IP du serveur DHCP qui vous a filé une IP : 

```
PS C:\Users\happy cash> ipconfig
[...]

Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . :
   Description. . . . . . . . . . . . . . : Intel(R) Wi-Fi 6 AX201 160MHz
   Adresse physique . . . . . . . . . . . : 84-14-4D-0E-5E-B1
   DHCP activé. . . . . . . . . . . . . . : Oui
   Configuration automatique activée. . . : Oui
   Adresse IPv6 de liaison locale. . . . .: fe80::bfb6:af78:1751:6490%11(préféré)
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.76.229(préféré)
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0
   Bail obtenu. . . . . . . . . . . . . . : jeudi 19 octobre 2023 13:32:59
   Bail expirant. . . . . . . . . . . . . : vendredi 20 octobre 2023 13:32:18
   Passerelle par défaut. . . . . . . . . : 10.33.79.254
   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254 ============ Ici le Server DHCP
   IAID DHCPv6 . . . . . . . . . . . : 126096461
   DUID de client DHCPv6. . . . . . . . : 00-01-00-01-29-5A-4E-04-C8-5A-CF-B7-B4-DA
   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8 ============ Ici le Server DNS
                                       1.1.1.1
   NetBIOS sur Tcpip. . . . . . . . . . . : Activé
[...]
```

dans votre table de routage, laquelle est la route par défaut :

```
PS C:\Users\happy cash> route print -4
[...]

IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0     10.33.79.254     10.33.76.229     30
         10.3.2.0    255.255.255.0         On-link          10.3.2.1    281
[...]
```
```
PS C:\Users> cd ..
PS C:\> cd .\Windows\
PS C:\Windows> cd .\System32\
PS C:\Windows\System32> cd .\drivers\
PS C:\Windows\System32\drivers> cd .\etc\
PS C:\Windows\System32\drivers\etc> cat .\hosts
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#       127.0.0.1       localhost
#       255.255.255.255 broadcasthost
#       ::1             localhost
192.168.56.102      mon-super-site.local
10.3.1.11       node1
10.3.1.203 rooter1.tp4.b1
10.105.1.11     web.tp5.linux
1.1.1.1 b2.hello.adryan
```

```
PS C:\Windows\System32\drivers\etc> ping b2.hello.adryan

Envoi d’une requête 'ping' sur b2.hello.adryan [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=17 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=11 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=11 ms TTL=57

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 10ms, Maximum = 17ms, Moyenne = 12ms
```

```
91.68.245.14
```

```
PS C:\WINDOWS\system32> netstat 91.68.245.14 -ab | Select-String 10.33.76.229:139 -Context 0,1

>   TCP    10.33.76.229:139       Adryx-LAPTOP:0         LISTENING
```



à quelle adresse IP correspond le nom de domaine www.ynov.com

```
PS C:\WINDOWS\system32> nslookup ynov.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    ynov.com
Addresses:  2606:4700:20::681a:be9
          2606:4700:20::681a:ae9
          2606:4700:20::ac43:4ae2
          104.26.11.233
          172.67.74.226
          104.26.10.233
```

à quel nom de domaine correspond l'IP 174.43.238.89

```
PS C:\WINDOWS\system32> nslookup 174.43.238.89
Serveur :   dns.google
Address:  8.8.8.8

Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```


par combien de machines vos paquets passent quand vous essayez de joindre www.ynov.com

```
PS C:\WINDOWS\system32> tracert ynov.com

Détermination de l’itinéraire vers ynov.com [172.67.74.226]
avec un maximum de 30 sauts :

  1     3 ms     2 ms     1 ms  10.33.79.254
  2     3 ms     2 ms     2 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     3 ms     2 ms     3 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     3 ms     4 ms     3 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    11 ms    11 ms    11 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  6    11 ms    10 ms    10 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  7    11 ms    11 ms    14 ms  141.101.67.48
  8    10 ms    11 ms    10 ms  172.71.124.4
  9    11 ms    11 ms    11 ms  172.67.74.226

Itinéraire déterminé.
```

combien il y a de machines dans le LAN auquel vous êtes connectés : 
```
Faire un NMAP mais je suis sur Windows doonc je peux faire un boucle qui ping tout el reseau et ensuite faire un arp -a pour tous les voirs
```

III. Le requin

capturez un échange ARP entre votre PC et la passerelle du réseau : [arp.pcap](./img/arp.pcap)





