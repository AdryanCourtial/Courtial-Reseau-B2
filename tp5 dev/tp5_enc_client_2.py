import socket
import re 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.11', 13337))


# Récupération d'une string utilisateur
calc = input("Calcul à envoyer: ")
mapping_table = str.maketrans({'+': ' ', '-': ' ', '*': ' '})

re = compile(r"^[0-9]{1,10} *[+x\-\*] *[0-9]{1,10}$")
newcalc = calc.translate(mapping_table)
op = newcalc.split(sep=' ')

op1 = int(op[0])
op2 = int(op[1])

if re.match(calc) == None:
    raise ValueError("Syntaxe Mauvaise")

if  op1 > 4294967295 or op2 > 4294967295 :
    raise ValueError('Tu utilise des valeurs trop grandes')

operator = re.findall(r"[+*-]", calc)
operator = operator[0]
print(operator)

if operator == "+":
    operator = 1 
    operator = operator.to_bytes(1, "big")
elif operator == "-":
    operator = 2
    operator = operator.to_bytes(1, 'big')
elif operator == "*":
    operator = 3
    operator = operator.to_bytes(1, 'big')
else:
    raise InterruptedError("Erreur pas de signe aproprié")

op1 = op1.to_bytes(2, 'big')
op2 = op2.to_bytes(2, 'big')

headerop1 = len(op1).to_bytes(1, "big")
headerop2 = len(op2).to_bytes(1, "big")

end = "0".encode()


print(operator + headerop1 + op1 + headerop2 + op2 + end) #Trame a envoyer : SIGNE (EN FORME DE 01,10,11 PREDEFINIE) / Header op1 / op 1 / Headerop2 / op 2 
s.send(operator + headerop1 + op1 + headerop2 + op2 + end)



# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
