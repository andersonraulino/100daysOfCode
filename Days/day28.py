def inverter_palavras(frase):
    palavras = frase.split()  # separa a frase em palavras
    palavras_invertidas = [palavra[::-1] for palavra in palavras]  # inverte cada palavra
    frase_invertida = ' '.join(palavras_invertidas)  # junta de volta em uma frase
    return frase_invertida


frase = "O rato roeu a roupa do rei de Roma"
print("Frase com palavras invertidas:", inverter_palavras(frase))