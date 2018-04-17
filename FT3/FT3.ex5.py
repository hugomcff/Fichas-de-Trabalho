

##Variaveis
res = 0
contar = 0
soma = 0

##Ciclo
while True:
    num=int(input("Introduza um numero: "))
    if num == -1: break
    contar = contar + 1
    soma = soma + num
if contar != 0:
    res = soma/contar
print(res)
