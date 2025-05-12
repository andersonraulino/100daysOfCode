def encontrar_maximo(lista):
    if len(lista) == 0:
        return "A lista está vazia."
    maximo = lista[0]
    for elemento in lista[1:]:
        if elemento > maximo:
            maximo = elemento
    return f"O maior elemento da lista é: {maximo}"

# Testando a função
numeros = [10, 22, 5, 78, 33]
print(encontrar_maximo(numeros))
