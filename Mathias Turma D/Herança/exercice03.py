class Form:
    def __init__(self, base, altura):
        self.base= base
        self.altura=altura
class Triangle(Form):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def calculate_perimeter(self):
        perimetro= self.altura+self.base
        print(f'Valor do perímetro é {perimetro}')
    def calculate_area(self):
        area= (self.base * self.altura)/2
        print(f'Valor da área é {area}')
class Retangle(Form):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def calculate_perimeter(self):
        perimetro= self.altura+self.base
        print(f'Valor do perímetro é {perimetro}')

    def calculate_area(self):
        area= 2*(self.base+self.altura)
        print(f'Valor da área é {area}')

triangulo= Triangle(10, 20)
triangulo.calculate_area()
triangulo.calculate_perimeter()
retangulo= Retangle(10,20)
retangulo.calculate_area()
retangulo.calculate_perimeter()