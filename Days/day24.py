def converterPalavras(palavra):
    return " ".join(palavra)

lista = ["Olá", "Mundo.", "Quebrei", "a", "maldição."]

print(f"Lista sem conversão: {lista}")
print(f"Lista com conversão: {converterPalavras(lista)}")