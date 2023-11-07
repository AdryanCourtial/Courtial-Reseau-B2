🌞 [bs_client_I1.py](bs_client_I1.py)

🌞 [bs_server_I1.py](bs_server_I1.py)

🌞 Commandes SERVER ...

```
[baptiste@Server ~]$ sudo firewall-cmd --zone=public --permanent --add-port 13337/tcp
success
[baptiste@Server ~]$ sudo firewall-cmd --reload
success
[baptiste@Server ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3 enp0s8
  sources:
  services: cockpit dhcpv6-client ssh
  ports: 13337/tcp
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
[...]
  cd home/baptiste/
[baptiste@Server ~]$ ls
[baptiste@Server ~]$ git pull https://github.com/AdryanCourtial/Courtial-Reseau-B2
fatal: not a git repository (or any of the parent directories): .git
[baptiste@Server ~]$ git clone https://github.com/AdryanCourtial/Courtial-Reseau-B2
Cloning into 'Courtial-Reseau-B2'...
remote: Enumerating objects: 71, done.
remote: Counting objects: 100% (71/71), done.
remote: Compressing objects: 100% (53/53), done.
remote: Total 71 (delta 14), reused 66 (delta 9), pack-reused 0
Receiving objects: 100% (71/71), 18.02 KiB | 1.80 MiB/s, done.
Resolving deltas: 100% (14/14), done.
[baptiste@Server ~]$ ls
Courtial-Reseau-B2
[...]
[baptiste@Server tp4 dev]$ python bs_server_I1.py
Connected by ('10.1.1.12', 45100)
Données reçues du client : b'Meooooo !'
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Données reçues du client : b''
Error Occured.
[...]
[baptiste@Server ~]$ ss -tal  | grep 13337
LISTEN 0      1          10.1.1.11:13337      0.0.0.0:*
[baptiste@Server ~]$


```

