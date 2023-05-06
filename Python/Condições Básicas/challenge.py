first_size=float(input('Digite o valor da primeira reta: ')) 
second_size=float(input('Digite o valor da segunda reta: ')) 
third_size=float(input('Digite o valor da terceira reta: ')) 

if first_size<(second_size+third_size) and second_size<(first_size+third_size) and third_size<(first_size+second_size):
    print('É possível ser um triângulo')
else:
    print('É IMPOSSÍVEL ser um triângulo')
