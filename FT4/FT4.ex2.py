
def soma(n1,n2):
    res = (n1 + n2)
    return res

def subtracao(n1,n2):
    res = (n1 - n2)
    return res

def divisao(n1,n2):
    res = ( n1/n2 )
    return res


def multi(n1,n2):
    res = ( n1 * n2)
    return res


print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")
print()
operacao = int(input("Introduza o tipo de operação que pretende: "))
num1 = int(input("Introduza o 1º numero: "))
num2 = int(input("Introduza o 2º numero: "))

if operacao == 1 :
    res = soma(num1,num2)
    print(res)
elif operacao == 2 :
    res = subtracao(num1,num2)
    print(res)
elif operacao == 3 :
    res = divisao(num1,num2)
    print(res)
elif operacao == 4 :
    res = multi(num1,num2)
    print(res)
else :
    print("Introduza uma operação possivel.")
