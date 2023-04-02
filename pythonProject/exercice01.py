nome = input("Digite seu nome")
idade = int(input("Digite sua idade"))
peso = float(input("Digite seu peso em KG"))
salario= float(input("Digite seu salário"))
porCent = float(input("Digite a porcentagem de aumento desejada"))
resultPorCent = (salario * porCent) / 100
finalResult = resultPorCent + salario

print(f"{nome} tem {idade} anos, com {peso}kg, recebendo R${salario}, porém gostaria de receber R${finalResult} que corresponde a {porCent}% do seu salário atual")
