print("Adição: +")
print("Subtração: -")
print("Multiplicação: x")
print("Divisão: /")
operacao = input("Qual a operação que deseja efetuar: ")

num1 = float(input("Introduza o numero 1: "))
num2 = float(input("Introduza o numero 2: "))

if operacao == "+" :
    resultado = (num1 + num2)
if operacao == "-" :
    resultado = (num1 - num2)
if operacao == "x":
    resultado = (num1 * num2)
if operacao == "/":
    resultado = (num1/num2)

print(resultado)