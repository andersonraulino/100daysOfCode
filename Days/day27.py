def palavra_mais_longa(frase):
    palavras = frase.split()  # separa a frase em palavras
    mais_longa = max(palavras, key=len)  # pega a palavra com maior comprimento
    return mais_longa


frase = "O rato roeu a roupa do rei de Roma"
print("A palavra mais longa é:", palavra_mais_longa(frase))