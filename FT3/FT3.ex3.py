

##Ciclo
fim = int(input("Introduza o numero onde acaba: "))
salto = int(input("Introduza o numero de salto: "))
if fim > 0 and salto > 0:
    for num in range(0, fim+1, salto):
        print(num)