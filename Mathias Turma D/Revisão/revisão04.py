number = float(input('Digite um número diferente de zero: '))
while number == 0:
    number = float(input('Digite um número diferente de zero DESGRAÇA: '))
    break

while number!=0:
    if number<0:
        print(f'{number} é um número negativo')
        break
    elif number>0:
        print(f'{number} é um número positivo')
        break

ask = input('Deseja continuar?')

while ask == 'sim':
    number = float(input('Digite seu número: '))
    while number != 0:
        if number < 0:
            print(f'{number} é um número negativo')
            break
        elif number > 0:
            print(f'{number} é um núemro positivo')
            break
    while number == 0:
        break
    ask = input('Deseja continuar?')
while ask == 'não':
    print('VOLTE QUANDO QUISER')
    break