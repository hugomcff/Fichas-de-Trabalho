num1 = int(input("Introduza o numero 1: "))
num2 = int(input("Introduza o numero 2: "))

if num1 == num2 :
    print("Os numeros sao iguais")
else:
    maior = None
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    print(maior)
  