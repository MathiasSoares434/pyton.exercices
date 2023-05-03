number_one= int(input('Digite o primeiro número: '))
number_two= int(input('Digite o segundo número: '))


while number_one!=number_two:
    if number_one>number_two:
        print(f'{number_one} {number_two}')
        break
    elif number_two>number_one:
        print(f'{number_two} {number_one}')
        break