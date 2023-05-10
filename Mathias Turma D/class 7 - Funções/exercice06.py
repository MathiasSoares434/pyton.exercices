numero= int(input('Digite um número: '))
def units(numero):
    if numero>0:
        return "P"
    elif numero<0:
        return "N"
    else:
        return "Z"

resultado= units(numero)
print(resultado)
