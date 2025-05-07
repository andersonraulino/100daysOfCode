# Conjuntos
print("Conjunto inicial:")
meuConjunto = {1, 2, 3, 4, 5, 5, 6}
print(meuConjunto)
print("\nConjunto após adição:")
meuConjunto.add(7)
print(meuConjunto)
print("\nConjunto após remoção:")
meuConjunto.remove(1)
print(meuConjunto)

novoConjunto = {8, 9, 10, 11, 12}

print("\nOperação union:")
conjuntoUniao = meuConjunto.union(novoConjunto) # Union serve para unir os conjuntos
print(conjuntoUniao)

conjunto1 = {"banana", "maça", "kiwi"}
conjunto2 = {"pera", "goiaba", "banana"}

print("\nOperação intersection:")
inter = conjunto1.intersection(conjunto2) # Intersection serve para ver os elementos de relação dos conjuntos
print(inter)

print("\nOperação difference:")
diff = conjunto1.difference(conjunto2) # Mostrando a diferença entre conjunto1 em relação ao conjunto2
print(diff) # Chamando a var "diff"
conjunto1.add("uva") # Adicionando elemento "uva" dentro do conjunto
print(conjunto1)

while True:
    print("\nMenu")
    print("0. Ver conjunto")
    print("1. Adicionar")
    print("2. Remover")
    print("3. Union") 
    print("4. Intersection")
    print("5. Difference")
    print("6. Sair")

    menu = int(input("Digite um número inteiro de 0 a 6: "))
    if menu == 0:
        print(f"Conjunto 1: {conjunto1} \nConjunto 2: {conjunto2}")
    elif menu == 1:
        conj = int(input("Qual conjunto deseja?"))
        if conj == 1:
            addconj1 = input("Digite o que irá adicionar: ")
            conjunto1.add(addconj1)
            print(conjunto1)
        elif conj == 2:
            addconj2 = input("Digite o que irá adicionar: ")
            conjunto2.add(addconj2)
            print(conjunto2)
        else:
            print("Digite o número do conjunto desejado: ")
    elif menu == 2:
        conj = int(input("Qual conjunto deseja?"))
        if conj == 1:
            addconj1 = input("Digite o que irá remover: ")
            conjunto1.remove(addconj1)
            print(conjunto1)
        elif conj == 2:
            addconj2 = input("Digite o que irá remover: ")
            conjunto2.remove(addconj2)
            print(conjunto2)
        else:
            print("Digite o número do conjunto desejado: ")
    elif menu == 3:
        conjUni = conjunto1.union(conjunto2)
        print(conjUni)
    elif menu == 4:
        conjInter = conjunto1.intersection(conjunto2)
        print(conjInter)
    elif menu == 5:
        conjdiff = conjunto1.difference(conjunto2)
        print(conjdiff)
    elif menu == 6:
        print("Saindo...")
        break

# Dicionários
dic = {"Nome": "Anderson", "Idade": 19, "Ocupação": "Estudante"}
print(dic["Nome"])
print(dic.get("Idade")) # Chamando valor de Idade
print(dic.pop("Nome")) # Retirando elemento Nome, dentro da tupla
print(dic.values()) # Pegando apenas os valores

# Iterando chaves
for chave in dic.keys():
    print(chave)

# Iterando valores
for valor in dic.values():
    print(valor)

# Iterando chaves e valores
for chave, valor in dic.items():
    print(f"{chave}: {valor}")