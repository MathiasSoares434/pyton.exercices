import time
import random


def gerar_numeros():
    code = ""
    for i in range(6):
        code += str(random.randint(0, 9))
    return code
class Client:
    def __init__(self, number, name, kind, balance):
        self.number=number
        self.name=name
        self.kind=kind
        self.balance=balance
        self.active=False

    def ativar_conta(self):
        self.active= True
        verifying_code = gerar_numeros()
        print(f'Seu código de verificação é: {verifying_code}')
        confirm =input('Digite aqui seu código: ')
        if verifying_code == confirm:
            print('Parabéns você agora é nosso cliente')

        else:
            print('Algo deu errado, por favor repita o procedimento')

    def deposit(self, value):
        if
            if value>0:
                self.balance+=value
                print(f'Depósito de valor {value} realizado com sucesso. Saldo atual: {self.balance}')
            else:
                def contador_regressivo(segundos):
                    print('Valor inválido, por favor tente novamente')
                    while segundos > 0:
                        print(segundos)
                        segundos -= 1
                        time.sleep(1)
                    print("Tempo para correção esgotado")

                contador_regressivo(5)


    def take_out(self, value):
        if self.active == True:
            if value > 0 and value<=self.balance:
                self.balance-=value
                print(f'Saque no valor de R${value} realizado com sucesso. Novo saldo: {self.balance}')
            else:
                print('Não é possível realizar. Conta inativa ou sem saldo suficiente para saque.')

    def verifying_count(self):
        print(f'Saldo disponível: {self.balance}')

name= input('Diga-me seu nome: ')
kind= input('Qual o tipo de conta você deseja? ')

if kind == 'Corrente' or kind == 'Poupança':
    print(kind)
else:
    print('Conta inválida')
value= float(input('Digite o valor a ser depositado: '))
value_take_off= float(input('Digite o valor que você quer sacar: '))
client= Client(gerar_numeros(), name, kind, 0)
client.ativar_conta()
client.deposit(value)
client.take_out(value_take_off)
client.verifying_count()

