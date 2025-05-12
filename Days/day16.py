def verificar_palindromo(texto):
    # Remove espaços e transforma em minúsculas
    texto = texto.replace(" ", "").lower()
    
    # Verifica se a string é igual ao seu reverso
    if texto == texto[::-1]:
        return "A palavra é um palíndromo."
    else:
        return "A palavra não é um palíndromo."

# Testando a função
entrada = input("Digite uma palavra: ")
print(verificar_palindromo(entrada))
