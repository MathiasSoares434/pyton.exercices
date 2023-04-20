ask = int(input('Quantos alunos tem na turma?'))
lista_alunos = []

for names in range(ask):
    lista_alunos.append(str(input('Digite os nomes desejados')))

for aluno in range(ask):
    print(lista_alunos[aluno], aluno)

