class Atleta:
    def __init__(self, peso):
        self.aposentado= False
        self.aquecendo= False
        self.peso=peso
    def aposentar(self):
        self.aposentado=True
        print('Atleta está aposentado!!!!')
    def aquecer(self):
        if not self.aquecendo and self.peso<=100:
            self.aposentado=True
            print('Atleta está aquecendo!!')
        else:
            print('O atleta já está aquecido!!')
class Corredor(Atleta):
    def __init__(self, peso: float):
        super().__init__(peso)
        self.correndo = False

    def correr(self):
        if not self.aposentado and self.aquecendo and self.peso <= 100:
            print('Atleta está aquecido e pronto para correr!')
        elif self.aposentado==True:
            print('Você está aposentado!!!')
        elif not self.aquecendo and self.peso<=100:
            print('Você precisa aquecer antes de correr!!!!')
        elif self.peso > 100:
            print('Você não pode correr pois está acima do peso permitido')
        else:
            print('OH DERROTA TU JÁ ESTÁ CORRENDO')
    def parar_correr(self):
        if self.correndo:
            self.correndo = False
            print('Pare de correr')
        else:
            print('Você já parou de correr!!!')    

class Nadador(Atleta):
    def __init__(self, peso: float):
        super().__init__(peso)
        self.nadando = False
    
    def nadar(self):
        if not self.aposentado and self.aquecendo and self.peso <= 100:
            self.nadando = True
            print('Atleta está aquecido e pronto para nadar!')
        elif self.aposentado:
            print('Você está aposentado!!!')
        elif not self.aquecendo and self.peso<=100:
            print('Você precisa aquecer antes de nadar!!!!')
        elif self.peso > 100:
            print('Você não pode nadar pois está acima do peso permitido')
        else:
            print('OH DERROTA TU JÁ ESTÁ NADANDO')
    
    def parar_nadar(self):
        if self.nadando:
            self.nadando = False
            print('Pare de nadar')
        else:
            print('Você já parou de nadar!!!')


class Ciclista(Atleta):
    def __init__(self, peso: float):
        super().__init__(peso)
        self.pedalando = False
    
    def pedalar(self):
        if not self.aposentado and self.aquecendo and self.peso <= 100:
            self.pedalando = True
            print('Atleta está aquecido e pronto para pedalar!')
        elif self.aposentado:
            print('Você está aposentado!!!')
        elif not self.aquecendo and self.peso<=100:
            print('Você precisa aquecer antes de pedalar!!!!')
        elif self.peso > 100:
            print('Você não pode pedalar pois está acima do peso permitido')
        else:
            print('OH DERROTA TU JÁ ESTÁ PEDALANDO')
    
    def parar_pedalar(self):
        if self.pedalando:
            self.pedalando=False
            print('Pare de pedalar')
        else:
            print('Você já parou de pedalar')

class Triatleta(Corredor, Ciclista, Nadador):
    def __init__(self, peso: float):
        super().__init__(peso)
        self.triatleta = False    
    def atleta_completo(self):
        if not self.aposentado and self.aquecendo and self.peso <= 85:
            self.triatleta = True
            print('Atleta está aquecido e pronto para pedalar, correr e nadar!')
        elif self.aposentado:            
            print('Você está aposentado!!!')
        elif not self.aquecendo and self.peso<=85:
            print('Você precisa aquecer antes de pedalar, correr e nadar!!!!')
        elif self.peso > 85:
            print('Você não pode ser um triatleta pois está acima do peso permitido')
        else:
            print('OH DERROTA TU JÁ ESTÁ NAS ATIVIDADES')
    def parar_atividades(self):
        if self.triatleta:
            self.triatleta=False
            print('Pare as atividades')
        else:
            print('Você já parou as atividades')
    
corrida= Corredor(80)
nadar= Nadador(120)
pedalar= Ciclista(90)
tri_atleta= Triatleta(90)

corrida.correr()
corrida.parar_correr()
nadar.nadar()
nadar.parar_nadar()
pedalar.pedalar()
pedalar.parar_pedalar()
tri_atleta.atleta_completo()
tri_atleta.parar_atividades()