def soma(n1, n2):
        resultado= n1+n2
        print(resultado)
def sub(n1, n2):
        resultado= n1-n2
        print(resultado)
def mult(n1, n2):
        resultado= n1*n2
        print(resultado)
def div(n1, n2):
        resultado= n1/n2
        print(resultado)
while True:
    resp=int(input('1-Soma 2-Subtração 3-Multiplicação 4-Divisão 5-Sair: '))
    if resp==1:
        n1=float(input('Digite o primeiro número: '))
        n2=float(input('Digite o segundo número: '))
        soma(n1,n2)
    elif resp==2:
        n1=float(input('Digite o primeiro número: '))
        n2=float(input('Digite o segundo número: '))
        sub(n1,n2)
    elif resp==3:
        n1=float(input('Digite o primeiro número: '))
        n2=float(input('Digite o segundo número: '))
        mult(n1,n2)
    elif resp==4:
        n1=float(input('Digite o primeiro número: '))
        n2=float(input('Digite o segundo número: '))
        div(n1,n2)
    elif resp==5:
        print('VALEU FALOU')
        break
    else:
        print('Numeração inválida')
