name= input('Digite seu nome: ')
grade_one= float(input('Digite sua primeira nota: '))
grade_two= float(input('Digite sua segunda nota: '))
media= (grade_one+grade_two)/2

if media >= 7: 
    print(f'Parabéns {name} você está aprovado')
else:
    print(f'Desculpe {name} mas seu aproveitamento foi abaixo')