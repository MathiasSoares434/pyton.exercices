def contVogais(t):
    cont=0
    for x in t:
        if x in "aeiouAEIOU":
            cont+=1
    print(cont)

texto="O rato roeu a roupa do rei de roma"
contVogais(texto)