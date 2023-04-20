names = []
passwords = []

for x in range(5):
    names.append(input('Digite o seu nome'))
    passwords.append((input('Digite sua senha')))
print()

for x in range(5):
    print(f'{names[x]} tem senha: {passwords[x]}')