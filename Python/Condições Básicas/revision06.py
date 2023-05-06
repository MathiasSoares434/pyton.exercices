year= int(input('Digite o seu ano de nascimento: '))
age= 2023 - year

if age<18:
    years_coming= 18-age
    print(f'Faltam {years_coming} anos pra você fazer o alistamento')
elif age>18:
    years_gone= age-18
    print(f'Se passaram {years_gone} anos que você deveria ter se alistado')