amount= int(input('Diga quanta maçãs que você vai querer: '))
if amount<12:
    discountLittle= amount*1.3
    print(f'R${discountLittle} a quantidade')
else:
    discountBig= amount*1
    print(f'R${discountBig} a quantidade')