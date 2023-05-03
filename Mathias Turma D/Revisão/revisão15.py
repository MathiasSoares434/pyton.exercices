begin= int(input('Digite o horário de início: '))
end= int(input('Digite o horário do final: '))
hoursSpend = end - begin
hoursNegative= (end + 24) - begin
while hoursNegative<24:
    if begin>end:
        print(f'A duração da partida de xadrez foi de {hoursNegative} horas.')
    break
while hoursSpend<24:
    if end > begin:
        print(f'A duração da partida de xadrez foi de {hoursSpend} horas. ')
        break
    elif end == begin:
        print(f'A duração da partida de xadrez foi de {(end - begin) + 24} horas.')
        break

