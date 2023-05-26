class Animal:
    def __init__(self, name, color):
        self.name=name
        self.color=color
    def comer(self):
        print(f'{self.name} foi comer ...')
    def sound(self):
        print(f'A {self.name} emitiu som ...')
class Gato(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)
    def sound(self):
        print(f'O {self.name} foi miando: ')

class Cachorro(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)
    def sound(self):
        print(f'{self.name} começou a latir')
class Vaca(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

gato= Gato("Ermiona", "Green")
cachorro= Cachorro('Apolo', 'Preto e Branco')
vaca= Vaca('Josefa', 'Branca')
gato.comer()
gato.sound()
cachorro.sound()
vaca.comer()