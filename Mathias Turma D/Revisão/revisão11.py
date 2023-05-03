válidos = []
brancos = []
nulos = []
todos = []

for todo in range(1):
    todos.append(int(input('Quantos votos foram computados? ')))
print()

for valido in range(1):
    válidos.append(int(input('Quantos votos válidos? ')))
print()

for branco in range(1):
    brancos.append(int(input('Quantos votos em branco? ')))
print()
for nulo in range(1):
    nulos.append(int(input('Quantos votos nulos? ')))
print()

while (válidos[valido]+brancos[branco]+nulos[nulo]) == todos[todo]:

    perValido =(válidos[valido]/todos[todo]) * 100
    perBranco = (brancos[branco]/todos[todo]) * 100
    perNulo = (nulos[nulo]/todos[todo]) * 100
    print(f'{todos[todo]} e os percentuais são: {perValido}% pros válidos; {perBranco}% pros brancos e {perNulo}% pros nulos')
    break

while (válidos[valido]+brancos[branco]+nulos[nulo]) != todos[todo]:
    print('Algum procedimento foi feito de maneira equivocada.')
    break