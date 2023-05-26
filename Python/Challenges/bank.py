import time
class Client:
    def __init__(self, number, balance, name, kind, status, limit):
        self.number=number
        self.balance=balance
        self.name=name
        self.kind=kind
        self.status=status
        self.limit=limit
    def deposit(self, value):
        if value>0:
            self.balance+=value
            print(f'Depósito de valor {value} realizado com sucesso. Saldo atual: {self.balance}')
        else:
            def contador_regressivo(segundos):
                print('Valor inválido, por favor tente novamente')
                while segundos > 0:
                    print(segundos)
                    segundos -= 1
                    time.sleep(1)  # Aguarda 1 segundo
                print("Tempo para correção esgotado")

            contador_regressivo(5)

    def take_out(self, value):
        if self.status == 'Ativa':
            if value > 0 and value<=self.balance:
                self.balance-=value
                print(f'Saque no valor de R${value} realizado com sucesso. Novo saldo: {self.balance}')
            else:
                print('Não é possível realizar. Conta inativa ou sem saldo suficiente para saque.')
    def active_count(self):
        if self.status=="Inativa":
            self.status="Ativa"
        else:
            print('A conta já está ativa')
    def verifying_count(self):
        print(f'Saldo disponível: {self.balance}')

client= Client(17546678, 0, "Mathias", "Corrente", "Inativa", 2.000)
client.deposit(1000)
client.take_out(100)
client.active_count()
client.verifying_count()