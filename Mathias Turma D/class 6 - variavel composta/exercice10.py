A = []
B = []
C = []

x =  int(input('Digite quantos números quer somar:'))
for i in range(x):
    A.append(int(input('Digite os números A: ')))
    B.append(int(input('Digite os números B: ')))

for y in range(x):
    C.append(A[y] + B[y])
print(C)