import time
import sys

# Lista 
list = ["filme", "série", "desenho", "documentário", "anime"]

while True:
    print("\nMenu")
    print("1. Ver generos")
    print("2. Adicionar elemento")
    print("3. Remover elemento")
    # print("4. Dividir lista")
    print("5. Sair")

    menu = int(input("Digite um número de 1 a 5: "))
    time.sleep(1.2)

    if menu == 1:
        print(list)
        time.sleep(1.2)
    elif menu == 2:
        add = input("Digite o que deseja adicionar: ")
        list.append(add)
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
        list.remove(delete)
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
    # elif menu == 4:
    #     print("Primeiro lado")  
    #     print("Segundo lado")
    #     n = "desenho"
    #     primeiroLado = menu[:n]
    #     segundoLado = menu[n:]
                                        #DIVIDIR A LISTA NO MEIO
    #     if n == 1:
    #         print(primeiroLado)
    #     elif n == 2:
    #         print(segundoLado)
    #     else:
    #         print("Escolha o número 1 ou 2: ")
    #     time.sleep(1.2)
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

# Tuplas
