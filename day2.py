#Criação de variáveis de diferentes tipos.
name = "Anderson" #String 
age = 20 #Int
height = 1.80 #Float
is_student = True #Boolean
email = None #Null value
siblings = ["Fulano", "Ciclano"]  #Lista
address = {"street": "321 Avenida Central", "city": "São Paulo"} #Rua e Cidade

#print de cada variável.
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is student: {is_student}")
print(f"Email: {email}")
print(f"Siblings:{siblings }")
print(f"Address: {address}")

#Retirando somente um valor da lista.
print(f"\nSiblings:{siblings[0]}") #Utilizando "[]" após a variável, é possivel acessar um valor especifico dentro da variável. Apenas indicando o índice de valor desejado.
