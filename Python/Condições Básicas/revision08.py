distance=int(input('Qual é a distância que o senhor(a) irá percorrer? '))

if distance<=200:
    value=(distance*0.5)
    print(f'O valor da sua viagem será R${value}')
elif distance>200:
    value_second=(distance*0.45)
    print(f'O valor da sua viagem será R${value_second}')