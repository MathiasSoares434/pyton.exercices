grade_one = float(input('Escreva a sua primeira nota: '))
grade_two= float(input('Escreva a sua segunda nota: '))
media= (grade_one+grade_two)/2

if media>=7:
    print('Parabéns, você foi aprovado')
elif media<7 and media>=4:
    print('Opa você ficou em recuperação')
else:
    print('REPROVADO')