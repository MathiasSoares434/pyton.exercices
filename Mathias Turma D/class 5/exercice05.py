password= '123'
n = 1
acesso=input('Digite sua senha')


while password!=acesso:
    n+=1
    print("Senha incorreta, digite novamente")
    senha= input('Digite novamente')

    print(n)

    if n == 3 and senha!=password:
        print('BARRADO')

        break
else:
    liberado = input('Acesso liberado')
    print(liberado)



