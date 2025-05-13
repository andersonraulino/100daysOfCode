# === Primeiro Método ===
# def reverterLista(lista):

#     listaRevertida = []

#     for elemento in lista: # Percorre a lista e manda os elementos para a posição 0, um por um
#         listaRevertida.insert(0, elemento)
    
#     return listaRevertida


# === Segundo Método ===
def reverterLista(lista):
    lista = lista[::-1] # Utilizando método de fatiamento (slicing)

    return lista

# Testando
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"A lista original é: {numeros}")
print(f"A lista invertida é: {reverterLista(numeros)}")
