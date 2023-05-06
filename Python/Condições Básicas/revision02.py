age= int(input('Digite sua idade: '))
year= 2023 - age
if age>=16:
    print(f'Você nasceu no de {year} portanto está autorizado(a) a votar')
else:
    print(f'Sinto muito mas você nasceu no ano de {year} e não está autorizado a votar.')
