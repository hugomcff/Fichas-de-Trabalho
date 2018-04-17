

def lerinteiro(min, max) :
    n = min-1
    while n < min or n > max : 
        n = int(input("Introduza um numero: "))
    return n
def valor() :
    n = lerinteiro(0,10)
    print("-" * n)

valor()



