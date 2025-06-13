texto = "gato cachorro rato gato pássaro cachorro gato"

# Quebra o texto em palavras
palavras = texto.split()

# Cria o dicionário de frequências
frequencias = {}

for palavra in palavras:
    if palavra in frequencias:
        frequencias[palavra] += 1
    else:
        frequencias[palavra] = 1

# Mostra o resultado
print(frequencias)
