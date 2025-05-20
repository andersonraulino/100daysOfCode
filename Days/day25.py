# Função para fazer a contagem de palavras dentro de uma frase
def contagemLista(lista):
    return print(f"A frase possui: {len(lista)} palavras")


frase = "Bem-vindo novamento, espero que esteja bem!" 
frase = frase.split(" ")

contagemLista(frase)