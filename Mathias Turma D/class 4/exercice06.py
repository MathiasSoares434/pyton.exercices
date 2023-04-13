alunos = int(input('Digite a quantidade de alunos existentes.'))
contador= 0
for c in range(alunos):
    notas = float(input('Digite as notas de cada um '))
    contador+=notas
    media = contador/alunos


print(media)
