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