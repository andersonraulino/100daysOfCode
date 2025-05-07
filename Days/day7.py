import time
import sys

# Lista 
categoria = ["filme", "série", "desenho", "documentário", "anime"]

while True:
    print("\nMenu")
    print("1. Ver generos")
    print("2. Adicionar elemento")
    print("3. Remover elemento")
    print("4. Dividir lista")
    print("5. Sair")

    menu = int(input("Digite um número de 1 a 5: "))
    time.sleep(1.2)

    if menu == 1:
        print(categoria)
        time.sleep(1.2)
    elif menu == 2:
        add = input("Digite o que deseja adicionar: ")
        categoria.append(add)
        def loading(mensagem="Adicionando", repeticoes=3, delay=0.5):
            for _ in range(1):  # repete o ciclo algumas vezes
                for i in range(repeticoes + 1):
                    pontos = '.' * i
                    print(f'\r{mensagem}{pontos}{" " * (repeticoes - i)}', end='')
                    sys.stdout.flush()
                    time.sleep(delay)
            print(f"\n{add} adicionado!")
        loading()
        time.sleep(1.2)
    elif menu == 3:
        delete = input("Digite o que deseja remover: ")
        categoria.remove(delete)
        def loading(mensagem="Removendo", repeticoes=3, delay=0.5):
            for _ in range(2):  # repete o ciclo algumas vezes
                for i in range(repeticoes + 1):
                    pontos = '.' * i
                    print(f'\r{mensagem}{pontos}{" " * (repeticoes - i)}', end='')
                    sys.stdout.flush()
                    time.sleep(delay)
            print(f"\n{delete} removido!")
        loading()
        time.sleep(1.2)
    elif menu == 4:
        divisao = len(categoria) // 2
        primeiroLado = categoria[:divisao]
        segundoLado = categoria[divisao:]

        escolha = int(input("Digite 1 para o primeiro lado ou 2 para o segundo: "))
        
        if escolha == 1:
            print("Primeiro lado:", primeiroLado)
        elif escolha == 2:
            print("Segundo Lado:", segundoLado)
        else:
            print("Escolha o número 1 ou 2: ")
        time.sleep(1.2)
    elif menu == 5:
        def loading(mensagem="Saindo", repeticoes=3, delay=0.5):
            for _ in range(2):  # repete o ciclo algumas vezes
                for i in range(repeticoes + 1):
                    pontos = '.' * i
                    print(f'\r{mensagem}{pontos}{" " * (repeticoes - i)}', end='')
                    sys.stdout.flush()
                    time.sleep(delay)
            print('\nPronto!')
        loading()
        break
    
    else:
        print("POR FAVOR, DIGITE UM NÚMERO INTEIRO DE 1 A 5")
        time.sleep(1)

# Teste para dividir lista numérica
# lista = [1, 2, 3, 4, 5, 6]
# print(lista)

# divisao = int(len(lista) / 2)

# primeiroLado = lista[:divisao]
# segundoLado = lista[divisao:]

# escolha = int(input("Digite 1 para o primeiro lado ou 2 para o segundo: "))

# if escolha == 1:
#     print(f"Primeiro Lado: {primeiroLado}")
# elif escolha == 2:
#     print(f"Segundo Lado: {segundoLado}")
# else:
#     print("Digite 1 ou 2: ")

# Tuplas
tupla = ("Anderson", "Gabriela", "Henrique", "Denis")
tupla2 = ("19", "26", "25", "24")
print(tupla)
print(tupla[1])
tuplaList = list(tupla) # Convertendo para uma lista
print(tupla)

# Utilizanndo operadores
print(len(tupla)) # Identificando quantos elementos possui
print(tupla + tupla2) # Juntando as tuplas
print(tupla *2) # Repetindo a tupla