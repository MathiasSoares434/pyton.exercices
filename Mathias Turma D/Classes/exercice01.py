class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False, fala= False, andar=False, dormir=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo = comendo
        self.fala= fala
        self.andar=andar
        self.dormir=dormir
    def Comendo(self, comida):
        if self.comendo==True:
            print(f'{self.nome} JÁ ESTÁ COMENDO {comida}')
            self.comendo=False
        else:
            print(f'{self.nome} VAI COMER {comida} DERROTA')
    def Stop_Eat(self):
        if self.comendo==True:
            print(f'{self.nome} Você ainda não terminou de comer')
        else:
            print(f'{self.nome} não estava comendo')

    def Fala(self):
        if self.fala==True:
            print(f'Não se fala comendo {self.nome}')
            self.comendo=False
        else:
            print(f'{self.nome} fala comigo')

    def Andar(self):
        if self.andar==True:
            print(f'E aí meu {self.nome} vamos pra onde?')
            self.comendo=True
        else:
            print(f'Ei meu amigo vamos andando.')
    def Dormindo(self):
        if self.dormir==True:
            print(f'Não se come dormindo {self.nome}')
            self.comendo=False
        else:
            print(f'Você está acordado {self.nome}, pode comer')


pessoa= Pessoa('Mathias', 80, 30)

print(f'{pessoa.nome} tem {pessoa.peso}kg e {pessoa.idade} anos.')
pessoa.Comendo('miojo')
pessoa.Stop_Eat()
pessoa.Fala()
pessoa.Andar()
pessoa.Dormindo()
print(vars(pessoa))