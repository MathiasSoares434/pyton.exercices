import time
import random
from datetime import datetime
from datetime import date


def gerar_numeros():
    code = ""
    for i in range(6):
        code += str(random.randint(0, 9))
    return code
class Client:
    def __init__(self, number, cpf, name, kind, balance):
        self.number=number
        self.cpf=cpf
        self.name=name        
        self.kind=kind
        self.balance=balance
        self.active = False

    def ativar_conta(self):        
        verifying_code = gerar_numeros()
        print(f'Seu código de autenticação é: {verifying_code}')
        confirm =input('Digite aqui seu código: ')
        if verifying_code == confirm:
            print('Parabéns você agora é nosso cliente')
            self.active = True
        else:
            print('Algo deu errado, por favor repita o procedimento')
            cadastrar_cliente()
    def verifying_cpf(self):
        if self.active:
            self.cpf= ''.join(filter(str.isdigit, self.cpf))

            if len(self.cpf)!=11:
                return False
            if self.cpf == self.cpf * 11:
                return False

            addiction= sum(int(self.cpf[i]) * (10 - i) for i in range(9))       
            rest= (addiction * 10)%11
            if rest==10:
                rest=0
            if rest!= int(self.cpf[9]):
                return False
            
            addiction=sum(int(self.cpf[i]) * (11-i) for i in range(10))
            rest= (addiction * 10) % 11
            if rest == 10:
                rest=0
            if rest != int(self.cpf[10]):
                return False 
            return True
    def deposit(self, value):
        if self.active:
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
        else:
            print('Conta não ativada. Não foi possível realizar o depósito.')


    def take_out(self, value):
        if self.active:
            if value > 0 and value<=self.balance:
                self.balance-=value
                print(f'Saque no valor de R${value} realizado com sucesso. Novo saldo: {self.balance}')
            elif value == 0:
                print(f'Você não realizou saque. Seu saldo continua: {self.balance}')
            else:
                print('Não é possível realizar saque. Conta inativa ou sem saldo suficiente para saque.')
        else:
            print('Conta não ativada. Não é possível realizar o saque.')
    def verifying_count(self):
        if self.active:
            print(f'Saldo disponível: {self.balance}')
        else:
            print('Conta não ativada')


usuarios= []
dados_pessoais=[]
def cadastrar_cliente():

   
    while True:
        nome_usuario = input("Digite o nome de usuário ou 'sair' para encerrar: ")
        if nome_usuario.lower() == "sair":
            break
        senha = input("Digite a senha (6 números): ")
        while len(senha) != 6 or not senha.isdigit():
            print('Senha inválida. A senha deve conter 6 números.')
            senha = input('Digite a senha (6 números): ')
        
        dados_usuarios = {
            "usuario": nome_usuario,
            "senha": senha,
        }

        usuarios.append(dados_usuarios)   
       
        
        name = input('Diga-me seu nome completo: ')
        cpf= input('Digite seu CPF: ')
        kind = input('Qual o tipo de conta você deseja? ')

        while kind.lower() not in ["corrente", "poupança"]:
            print(f'Conta {kind} inválida. Por favor, digite "Corrente" ou "Poupança"')
            kind = input('Qual o tipo de conta você deseja? ')

        dado_pessoal= {
            "Nome Completo": name,
            "CPF": cpf,
            "Tipo de conta": kind,
        }

        dados_pessoais.append(dado_pessoal)
        print(f'Seus dados são: {dados_pessoais}')
        pergunta= input('Tem certeza que os dados acima são seus? ')

        client = Client(gerar_numeros(), cpf, name, kind, 0)
        if pergunta.lower()!="sim":
            print('Por favor repita o processo novamente.')
            cadastrar_cliente()
        else:
            client.ativar_conta()
            if client.active:
                value = float(input('Digite o valor a ser depositado(minímo R$10): '))
                
                if value>=10:
                    value_take_off = float(input('Digite o valor caso queira sacar(se não ponha 0): '))
                    client.deposit(value)
                    client.take_out(value_take_off)
                    client.verifying_count()
                else:
                    print('Valor insuficiente ou cliente não quis realizar nenhum depósito')                
                    resposta = input("Responda sim caso queira realizar novamente esse procedimento ou acrescentar mais algum cadastro; caso não queira é só responder não. ")
                    if resposta.lower() != "sim":
                        break
                    else:
                        cadastrar_cliente()


        resposta = input('Deseja realizar novamente esse procedimento ou gostaria de sair do sitema? ')
        if resposta.lower() != "sim":
            agora = datetime.now()
            hora_atual = agora.strftime("%H:%M:%S")
            date_today = date.today()
            day_of_week = date_today.weekday()
            days_of_week = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
            print(f'Agradecemos o acesso no horário das {hora_atual}, tenha um(a) ótimo(a) {days_of_week[day_of_week]} neste dia {date_today.strftime("%d/%m/%Y")}')
            print(f'Estes foram os dados pessoais cadastrados no sistema: {dados_pessoais}')
            print(f'Estes foram os dados de usuário cadastrados no sistema: {usuarios}')
            break
        else:
            cadastrar_cliente()

cadastrar_cliente()

   
