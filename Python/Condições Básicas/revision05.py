year= int(input('Digite o ano desejado: '))

if year%4 == 0:
    print(f'{year} é bissexto')
else:
    print(f'{year} não é bissexto')