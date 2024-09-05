def fibonacci(numero):
    # Inicializando os dois primeiros números da sequência
    a, b = 0, 1
    
    # Se o número informado for 0 ou 1, pertence à sequência
    if numero == 0 or numero == 1:
        return True
    
    # Loop para calcular a sequência de Fibonacci até encontrar ou ultrapassar o número informado
    while b < numero:
        a, b = b, a + b
    
    # Verifica se o número informado é igual ao último valor da sequência calculada
    return b == numero

# Número a ser verificado (pode ser substituído por uma entrada do usuário)
numero_informado = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} NÃO pertence à sequência de Fibonacci.")
