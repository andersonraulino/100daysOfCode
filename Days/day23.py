def intersectionList(lista1, lista2):
    inter = lista1.intersection(lista2)

    return inter

primeiraLista = {2, 4, 6, 8}
segundaLista = {2, 3, 4, 5, 6}
print(f"Primeira lista: {primeiraLista}")
print(f"Segunda lista: {segundaLista}")

print(f"Intersection das listas: {intersectionList(primeiraLista, segundaLista)}")