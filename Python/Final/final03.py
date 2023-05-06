grades= []

for students in range(10):
    grade=float(input('Digite sua nota: '))
    grades.append(grade)

media= sum(grades)/len(grades)
print(f'A média da turma foi {media}')

upper_of_media= 0

for grade in grades:
    if grade>media:
        upper_of_media+=1
print(f'{upper_of_media} alunos ficaram acima da média geral da turma')

maior= grades[0]
menor= grades[0]
for valor in range(10):
    if grades[valor]>maior:
        maior=grades[valor]
print(f'A maior nota da turma foi {maior}')
