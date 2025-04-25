# 💻 100 Days of Code Challenge

Bem-vindo ao meu repositório do desafio **#100DaysOfCode**!  
Aqui eu vou registrar meu progresso diário enquanto codifico por pelo menos 1 hora durante 100 dias seguidos.

---

## 🗓️ Dia 1

✅ **Data:** 23/04/2025 
📌 **Resumo:**  
Hoje comecei o desafio com o clássico dos clássicos:  
```python
print("Hello World!")
```
---

E dei uma enriquecida com outras funcionalidades:
```python
from time import sleep #Função para dar um intervalo entre os códigos.

print('Hello World!') #Exibe a mensagem 'Hello World' no console, para quebrar a maldição.
sleep(0.8)#Intervalo de 0.8s.
print("Ebaaaaa!!! Quebrei a maldição!!!")
```
---
## 🗓️ Dia 2

✅ **Data:** 24/04/2025 
📌 **Resumo:**  
Hoje foi dia de mexer com tipos de variáveis:  
```python
#Criação de variáveis de diferentes tipos.
name = "Anderson" #String 
age = 20 #Int
height = 1.80 #Float
is_student = True #Boolean
email = None #Null value
siblings = ["Fulano", "Ciclano"]  #Lista
address = {"street": "321 Avenida Central", "city": "São Paulo"} #Rua e Cidade
``` 
---

Depois chamei cada uma delas usando a função 'print':
```python
#print de cada variável.
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is student: {is_student}")
print(f"Email: {email}")
print(f"Siblings:{siblings }")
print(f"Address: {address}")
```
Logo após, resolvi testar retirar somente um valor da variável:
```python
#Retirando somente um valor da lista.
print(f"\nSiblings:{siblings[0]}") #Utilizando "[]" após a variável, é possivel acessar um valor especifico dentro da variável. Apenas indicando o índice de valor desejado.

```
---
## 🗓️ Dia 3
✅ **Data:** 25/04/2025
📌 **Resumo:**

Hoje foi dia de praticar input e output!
Trabalhei com input() e print() em alguns exercícios simples, mas que me ajudaram a entender melhor como interagir com o usuário e exibir informações de forma clara.

Pode parecer básico, mas cada linha de código é um passo a mais nessa jornada! 👨‍💻🔥

Bora pro próximo!
```python
name = input("Qual seu nome?")
print(f"Olá, {name}") 

age = int(input("Qual sua idade?")) #int converte valor para números inteiros
height = float(input("Qual sua altura?")) #float converte valor para números decimais

print(f"\nSeus dados:")
print(f"Nome: {name}") #Tipo String
print(f"Idade: {age}") #Tipo Inteiro
print(f"Altura: {height}") #Tipo Decimal

print("\nTipos de dados:")
print("Nome: ", type(name))
print("Idade: ", type(age))
print("Altura: ", type(height))
```

