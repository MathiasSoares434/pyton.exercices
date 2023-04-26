numbers = []


for number in range(3):
    numbers.append(int(input('Digite 3 números: ')))
print()
maior = numbers[0]
menor = numbers[0]
for valor in range(3):
    if numbers[valor] > maior:
        maior=numbers[valor]
    elif numbers[valor] < menor:
        menor = numbers[valor]
print(f'O maior é:{maior} e o menor é: {menor}')