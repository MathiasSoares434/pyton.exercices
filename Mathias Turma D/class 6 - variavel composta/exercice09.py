names = []
passwords= []

for x in range(5):
    names.append(input('Digite o seu nome'))
    passwords.append((input('Digite sua senha')))
    print()

login = input('Diga seu usuário')
senha = input('Digite sua senha')
for i in range(1):
    while login==names[i] and  senha==passwords[i] :
        print('Login efetuado com sucesso')
        break
    while login!=names[i] and senha!=passwords[i]:
        print('ERRADO DERROTA')
        break