getAlunos = []
listaMedias = []
getAlunos.append(input('Digite seu nome '))

n1 = float(input('Digite a primeira nota: '))
n= 1

while n1<0 or n1>10:
    n1= float(input('NOTA INVÁLIDA BURRÃO, DIGITA DE NOVO'))

n2 = float(input('Digite a segunda nota: '))
while n2<0 or n2>10:
    n2=float(input('NOTA INVÁLIDA BURRÃO, DIGITA DE NOVO'))

media = (n1 + n2)/2
listaMedias.append(media)
print(f'Sua média final foi: {media}')
if media >= 7:
    print('Parabéns, você está aprovado')
elif media<7 and media>=4:
    print('Opa você ficou de recuperação.')
else:
    print('REPROVADO DERROTA')

ask= input('Deseja continuar? ')
while ask == 'sim':

    getAlunos.append(input('Digite seu nome '))

    n1 = float(input('Digite a primeira nota: '))
    n = 1

    while n1 < 0 or n1 > 10:
        n1 = float(input('NOTA INVÁLIDA BURRÃO, DIGITA DE NOVO'))

    n2 = float(input('Digite a segunda nota: '))
    while n2 < 0 or n2 > 10:
        n2 = float(input('NOTA INVÁLIDA BURRÃO, DIGITA DE NOVO'))

    media = (n1 + n2) / 2
    listaMedias.append(media)
    print(f'Sua média final foi: {media}')
    if media >= 7:
        print('Parabéns, você está aprovado')
    elif media < 7 and media >= 4:
        print('Opa você ficou de recuperação.')
    else:
        print('REPROVADO DERROTA')

    ask = input('Deseja continuar? ')
while ask == 'não':
    break
print(listaMedias)
print(getAlunos)