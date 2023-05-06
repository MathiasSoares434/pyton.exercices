amountDay= int(input('Quantos cigarros o senhor(a) fuma por dia? '))
amountYears= int(input('Há quantos anos o senhor(a) fuma? '))
amountTotal= amountDay*(amountYears*365)
minutesLife= amountTotal*10
dayLife= minutesLife/1440

print(f'O(A) senhor(a) perdeu {dayLife} dias da sua vida por causa do cigarro')