def fibonacci(nro):
    a, b = 0, 1
    
    if nro == 0 or nro == 1:
        return True
    
    while b < nro:
        a, b = b, a + b
    
    return b == nro

nro_informado = int(input("Informe um número: "))

if fibonacci(nro_informado):
    print(f"O número {nro_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {nro_informado} NÃO pertence à sequência de Fibonacci.")
