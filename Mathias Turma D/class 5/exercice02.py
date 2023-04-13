n = 1
soma = 0

while n<=10:
    valor = int(input('Digite um número'))
    soma+=valor
    n+=1
    media= soma/10

print(f'Sua média foi: {media}')