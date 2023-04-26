idade = int(input('Digite sua idade: '))

ano = 2023 - idade

print(f'Seu ano de nascimento é {ano}')

ask= input('Deseja continuar? ')

while ask == 'sim' or ask == 'Sim' or ask == 'SIM':
    idade = int(input('Digite sua idade: '))

    ano = 2023 - idade

    print(f'Seu ano de nascimento é {ano}')

    ask = input('Deseja continuar? ')

while ask == 'não' or ask == 'Não' or ask == 'NÃO':
    print('Volte sempre otario!!')
    break