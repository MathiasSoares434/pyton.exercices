contador = 0

for c in range(10):
    numero = int(input("Digite seu número"))
    if numero%2 != 0:
        contador+=numero
print(contador)

