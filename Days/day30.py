import time

def classificacao(lista):
    return sorted(lista)

numeros = [14, 25, 2, 13, 10, 1, 5, 100, 210, 59, 78, 18]

while True:
    print("\nMenu")
    print("1. Ver lista")
    print("2. Ordem crescente")
    print("3. Ordem decrescente")
    print("4. Sair")

    menu = int(input("Digite um número de 1 a 4: "))

    if menu == 1:
        print(numeros)
        time.sleep(0.8)
    elif menu == 2:
        print(classificacao(numeros))
        time.sleep(0.8)
    elif menu == 3:
        def classificacao(lista):
            return sorted(lista, reverse=True)
        print(classificacao(numeros))
        time.sleep(0.8)
    elif menu == 4:
        print("Saindo...")
        break
    else:
        print("Por favor, digite um número inteiro de 1 a 4: ")
    

