n1 = int(input('Digite primeiro número'))
n2 = int(input('Digite segundo número'))
contador=1
print('[1]somar '
      '[2]subtração '
      '[3]multiplicação '
      '[4]divisão '
      '[5]para digitar novamente '
      '[6]para sair ')
opção = int(input('Qual é a opção?'))
while opção>=6 and contador==1:
      print('Volte sempre')
      contador+=1
while opção==1 and contador==1:
      soma=n1+n2
      print(soma)
      contador += 1
while opção==2 and contador==1:
      subtração= n1 - n2
      print(subtração)
      contador += 1
while opção==3 and contador==1:
      multiplicação = n1*n2
      print(multiplicação)
      contador += 1
while opção==4 and contador==1:
      divisão = n1/n2
      print(divisão)
      contador += 1
while opção==5 and contador==1:
      print('[1]somar '
            '[2]subtração '
            '[3]multiplicação '
            '[4]divisão '
            '[5]para digitar novamente '
            '[6]para sair ')
      opção = int(input('Digite novamente'))
      while opção >= 6 and contador == 1:
            print('Volte sempre')
            contador += 1
      while opção == 1 and contador == 1:
            soma = n1 + n2
            print(soma)
            contador += 1
      while opção == 2 and contador == 1:
            subtração = n1 - n2
            print(subtração)
            contador += 1
      while opção == 3 and contador == 1:
            multiplicação = n1 * n2
            print(multiplicação)
            contador += 1
      while opção == 4 and contador == 1:
            divisão = n1 / n2
            print(divisão)
            contador += 1




