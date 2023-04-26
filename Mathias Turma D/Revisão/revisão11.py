válidos = []
brancos = []
nulos = []

for valido in range(1):
    válidos.append(int(input('Quantos votos válidos?')))
print()

for branco in range(1):
    brancos.append(int(input('Quantos votos em branco?')))
print()
for nulo in range(1):
    nulos.append(int(input('Quantos votos nulos?')))
print()

total = válidos[valido] + brancos[branco] + nulos[nulo]
perValido =(válidos[valido]/total) * 100
perBranco = (brancos[branco]/total) * 100
perNulo = (nulos[nulo]/total) * 100
print(f'{total} e os percentuais são: {perValido}% pros válidos; {perBranco}% pros brancos e {perNulo}% pros nulos')
