def anagramas(palavra1, palavra2):

    # Remove os espaços e converte para minúsculas
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()

    # Verifica se as duas palavras tem o mesmo número de caracteres e as mesmas letras
    return sorted(palavra1) == sorted(palavra2)

print(anagramas("Amor", "Roma"))
print(anagramas("Cama", "Sala"))