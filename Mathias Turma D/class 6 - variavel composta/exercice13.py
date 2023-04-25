A =[]
soma=0

for i in range(5):
    A.append(int(input('Digite os números no vetor A: ')))
print()
for value in range(5):
    if A[value]%2==0:
        soma+=1
print(f'tem {soma} números pares')



maior = A[0]
menor = A[0]

for valor in range(5):
    if A[valor]>maior :
        maior=A[valor]

    if A[valor]<menor:
        menor = A[valor]
print(f'O maior é:{maior} e o menor é: {menor}')

for division in range(5):
    soma+=A[division]
mediaAritmetica= soma/5

cont=0
for media in range(5):
    if A[media]>=mediaAritmetica:
        cont+=1
print(f"Tem {cont} valores maiores que a média")
