"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
"""


saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
sarakts2=[]
for i in saraksts1:
    x = 'Dr. ' + str(i)
    sarakts2.append(x)
print(sarakts2)

def add_dr(i):
    return 'Dr. ' + str(i)
sarakts2 = list(map(add_dr, saraksts1))
print(sarakts2)