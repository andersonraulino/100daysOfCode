def converterPalavras(palavra):
    return " ".join(palavra)

lista = ["Olá", "Mundo.", "Quebrei", "a", "maldição."]

print(f"Lista sem conversão: {lista}")
print(f"Lista com conversão: {converterPalavras(lista)}")


# Separando novamento as palavras, utilizando um split() dentro de uma nova função
def inverterConversão(nova):
    x = nova.split(" ")
    return x

print(f"Separação da frase: {inverterConversão(converterPalavras(lista))}")