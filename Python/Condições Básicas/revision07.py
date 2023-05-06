name= input('Digite seu nome: ')
gender= input('Qual o seu sexo biológico? ')
value= float(input('Digite quanto deu suas compras: '))

if gender == 'feminino' or gender == 'F':
    discount_female= value - (value*0.13)
    print(f'O valor das suas compras {name} deu R${discount_female}')
elif gender == 'masculino' or gender == 'M':
    discount_male= value-(value*0.05)
    print(f'O valor das suas compras {name} deu R${discount_male}')
else:
    print(f'O valor das suas compras {name} deu R${value}')