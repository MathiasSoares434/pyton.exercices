notas = list()
soma = 1
acumulador = 0

for notasAlunos in range(5):
    notas.append(int(input('Digite as notas dos alunos?')))

for media in notas:
    acumulador += media
    soma+=1
print()
media = acumulador/5
soma=1
for resolution in notas:
    print(f'A {soma}° nota foi acima da média da turma' if resolution>= media else f'A {soma}° nota foi abaixo da média da turma')
    soma+=1







