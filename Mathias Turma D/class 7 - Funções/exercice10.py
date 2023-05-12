def number(num):
    if num <=1:
        print(f'{num} não é primo')
    elif num == 2 and num == 3:
        print(f'{num} é primo')
    elif num%2!=0 and num%3!=0:
        print(f'{num} é primo')
    else:
        print('Não é um número primo')

number(10)

