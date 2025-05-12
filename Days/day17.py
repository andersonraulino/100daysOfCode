def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    
    return f"A string contém {contador} vogal(is)."

# Testando a função
entrada = input("Digite uma string: ")
print(contar_vogais(entrada))
