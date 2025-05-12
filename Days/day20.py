def fibonacci_ate_limite(limite):
    sequencia = [0, 1]
    
    while True:
        proximo = sequencia[-1] + sequencia[-2]
        if proximo > limite:
            break
        sequencia.append(proximo)
    
    return sequencia

# Testando a função
limite = int(input("Digite o limite para a sequência de Fibonacci: "))
print(f"A sequência de Fibonacci até {limite} é: {fibonacci_ate_limite(limite)}")
