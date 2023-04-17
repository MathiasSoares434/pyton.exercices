firstGrade = float(input('Digite sua primeira nota'))
n = 1

while firstGrade<0 or firstGrade>10:
  firstGrade= float(input('Nota inválida, digite novamente'))

secondGrade = float(input('Digite sua segunda nota'))
while secondGrade<0 or secondGrade>10:
    secondGrade = float(input('Nota inválida, digite novamente'))

media = (firstGrade + secondGrade)/2
print(f'Sua média final foi {media}')

ask= input('Deseja continuar?')

while ask == 'sim':
    firstGrade = float(input('Digite sua primeira nota'))
    n = 1

    while firstGrade < 0 or firstGrade > 10:
        firstGrade = float(input('Nota inválida, digite novamente'))

    secondGrade = float(input('Digite sua segunda nota'))
    while secondGrade < 0 or secondGrade > 10:
        secondGrade = float(input('Nota inválida, digite novamente'))

    media = (firstGrade + secondGrade) / 2
    print(f'Sua média final foi {media}')
    ask = input('Deseja continuar?')

while ask == 'não':
    break

