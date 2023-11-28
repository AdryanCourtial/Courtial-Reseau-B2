import socket
from re import compile, match

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.11', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

# Récupération d'une string utilisateur
calc = input("Calcul à envoyer: ")
calc = calc.strip()

re = compile(r"^[0-9]{1,10} *[+x\-\*] *[0-9]{1,10}$")

if re.match(calc):
    op = calc.split(sep='+')
    print(f"{len(str(op[0].encode('UTF-8')))}")
    if len(str(op[0].encode('UTF-8'))) > 2 or len(str(op[1].encode('UTF-8'))) > 2:
        raise ValueError('Tu utilise des valeurs trop grandes')
    else:
        s.send(calc.encode('UTF-8'))

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
