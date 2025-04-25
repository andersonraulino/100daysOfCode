name = input("Qual seu nome?")
print(f"Olá, {name}")

age = int(input("Qual sua idade?"))
height = float(input("Qual sua altura?"))

print(f"\nSeus dados:")
print(f"Nome: {name}")
print(f"Idade: {age}")
print(f"Altura: {height}")

print("\nTipos de dados:")
print("Nome: ", type(name))
print("Idade: ", type(age))
print("Altura: ", type(height))

#Colocar um if para mandar uma resposta pro usuário, caso ele digite um valor diferente do tipo dele.
