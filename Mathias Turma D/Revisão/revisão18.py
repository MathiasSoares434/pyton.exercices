cont= 0
a=[]
cont_impar=0

while True:
    if cont%2!=0:
        a.append(cont)
        cont_impar+=1
    if cont_impar>=10:
        break
    cont+=1
print(a)





