def removerDuplicadas(lista):
    return list(set(lista)) # set é uma coleção não ordenada de elementos únicos, o que o torna ideal para remover duplicatas

numeros = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8]
print(f"Lista com duplicadas: {numeros}")
print(f"Lista sem duplicadas: {removerDuplicadas(numeros)}")