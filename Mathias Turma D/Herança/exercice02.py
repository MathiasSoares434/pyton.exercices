class Ingresso:
    def __init__(self, value):
        self.value=value
    def print_value(self):
        print(f'O valor do ingresso custa R${self.value}')
class Vip(Ingresso):
    def __init__(self, value):
        super().__init__(value)
    def print_vip(self, tax):
        ticket_vip= self.value + (self.value/100)*tax
        print(f'O valor do ingresso vip é R${ticket_vip}')

ingresso= Ingresso(50)
ingresso.print_value()
vip_ingresso= Vip(50)
vip_ingresso.print_vip(10)
