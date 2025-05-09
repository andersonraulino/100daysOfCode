def verificador(valor: int): # Declara a propriedade como um valor inteiro
    if valor % 2 == 0:
        # Testei fazer com um print, porém ele sempre me retornou o resultado e logo abaixo, ele retornou a mensagem "None". Para evitar isso, devemos utilizar um 'return'
        # print(f"O número {numero} é par!")
        return f"O número {numero} é par!"
    elif valor % 2 == 1:
        # print(f"O número {numero} é ímpar!")
        return f"O número {numero} é ímpar!"
    else:
        # print("Digite um número válido!")
        return "Digite um número válido!"
numero = int(input("Digite um número inteiro: "))
resultado = verificador(numero)
print(resultado)