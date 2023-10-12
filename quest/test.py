guerreiro = 0
gatuno = 5
mago = 3
dicionario = {}

value = f'guerreiro={guerreiro}\ngatuno={gatuno}\nmago={mago}'

z = dict([i.split('=') for i in value.strip().split('\n')])

lista = []
xy = []

for i in z.items():
    x = tuple(i)
    lista.append(x)

print(lista)
for k, j in lista:
    xy.append(j)

xy.sort()
print(xy[-1])