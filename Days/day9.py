import random

# Função para gerar um número aleatório (inteiro ou decimal)
def gerador_aleatorio():
    tipo = input("Digite 1 para número inteiro ou 2 para número decimal: ")
    if tipo == "1":
        numero = random.randint(1, 100)  # Número inteiro entre 1 e 100
        print(f"Número inteiro aleatório: {numero}")
    elif tipo == "2":
        numero = random.uniform(1, 100)  # Número decimal entre 1 e 100
        print(f"Número decimal aleatório: {numero:.2f}")
    else:
        print("Opção inválida. Escolha 1 ou 2.")
    
# Função para gerar apenas números inteiros
def gerador_inteiro():
    numero = random.randint(1, 100)  # Gera um número inteiro entre 1 e 100
    print(f"Número inteiro aleatório: {numero}")

print("=== GERADOR DE NÚMEROS ALEATÓRIOS ===")
gerador_aleatorio()

