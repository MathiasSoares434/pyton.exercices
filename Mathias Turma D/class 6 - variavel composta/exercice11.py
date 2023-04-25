A = []
soma=0
for i in range(10):
    A.append(int(input('Digite os números no vetor A: ')))
x= int(input('Digite o número que você quer encontrar: '))

for y in range(10):
    if x==A[y]:
        soma+=1
print(soma)