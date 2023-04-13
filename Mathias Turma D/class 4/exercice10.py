inside= 0
outside = 0
for num in range(10):
    valores = int(input('Digite os valores'))
    if valores >= 10 and valores<=20:
        inside+=1
    else:
        outside+=1

print(inside, outside)


