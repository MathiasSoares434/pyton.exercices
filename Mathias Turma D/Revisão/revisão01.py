n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2

if media >= 7:
    print('Parabéns, você está aprovado')
elif media<7 and media>=4:
    print('Opa você ficou de recuperação.')
else:
    print('REPROVADO DERROTA')