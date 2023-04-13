alunos = int(input('Quantos alunos tem essa saula?'))
n = 1
contador = 0

while n<= alunos:
    notas = float(input('Digite a nota dos alunos'))
    contador+=notas
    n+=1
    media=(contador/alunos)

print(media)
