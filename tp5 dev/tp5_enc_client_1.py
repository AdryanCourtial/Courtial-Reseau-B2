import socket
from re import compile

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.11', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

# Récupération d'une string utilisateur
calc = input("Calcul à envoyer: ")
mapping_table = str.maketrans({'+': ' ', '-': ' ', '*': ' '})

re = compile(r"^[0-9]{1,10} *[+x\-\*] *[0-9]{1,10}$")
newcalc = calc.translate(mapping_table)
op = newcalc.split(sep=' ') 3 3 --> 0[op1] 1[op2]

if re.match(calc) == None:
    raise ValueError("Syntaxe Mauvaise")

if  int(op[0]) > 4294967295 or int(op[1]) > 4294967295 :
    raise ValueError('Tu utilise des valeurs trop grandes')
    
calc = calc.encode()
header = len(calc)
end = "0".encode()

print(header.to_bytes(4, byteorder="big") + calc + end )
s.send(header.to_bytes(4, byteorder="big") + calc + end )

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()


# A quoi sert le Big concretement () pas compris 
#Coflin ?
#Mon erreur ? 