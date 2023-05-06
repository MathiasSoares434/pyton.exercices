speed= float(input('Qual é a velocidade do carro? '))

if speed>80:
    trafficTicket= (speed-80)*5
    print(f'Você estava à {speed}km/h e por isso tomou uma multa no valor de R${trafficTicket}.')
else:
    print('Nada a relatar')
    