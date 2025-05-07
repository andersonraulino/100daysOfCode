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
print(f"Nome: {name}") 
print(f"Idade: {age}") 
print(f"Altura: {height}") 

print("\nTipos de dados:")
print("Nome: ", type(name)) #Tipo String
print("Idade: ", type(age)) #Tipo Inteiro
print("Altura: ", type(height)) #Tipo Decimal
```
---

## 🗓️ Dia 4

✅ **Data:** 26/04/2025
📌 **Resumo:**

Hoje foi dia de botar a mão na massa com expressões e operadores básicos!
Treinei operações matemáticas, uso de +, -, *, /, % e até um pouco de precedência entre eles.
Além disso, trabalhei com os operadores lógicos, como, AND, OR e NOT.
Coisa simples, mas essencial pra construir qualquer lógica mais pra frente! 🧠💻

Bora pro próximo!
```python
from time import sleep

#Expressões e operadores básicos
num1 = 5
num2= 8
#Operadores aritméticos
print("\nOperadores Aritméticos")
print(f"A soma de {num1} e {num2} é igual: ", num1 + num2)
print(f"A subtração de {num1} e {num2} é igual: ", num1 - num2)
print(f"A multiplicação de {num1} e {num2} é igual: ", num1 * num2)
print(f"A divisão de {num1} e {num2} é igual: ", num1 / num2)
print(f"A divisão inteira de {num1} e {num2} é igual: ", num1 // num2)#Divisão que resulta em um número inteiro;
print(f"O modulus de {num1} e {num2} é igual: ", num1 % num2)#Resto da conta;
print(f"A exponenciação de {num1} com o exponente {num2} é igual: ", num1 ** num2)

#Operadores Relacionais
sleep(1.2)
print("\nOperadores Relacionais")
print(f"{num1} é igual a {num2}? ",num1 == num2)
print(f"{num1} é diferente de {num2}? ", num1 != num2)
print(f"{num1} é maior que {num2}? ", num1 > num2)
print(f"{num1} é menor que {num2}? ", num1 < num2)
print(f"{num1} é maior ou igual a {num2}? ", num1 >= num2)
print(f"{num1} é menor ou igual a {num2}? ", num1 <= num2)

#Operadores lógicos

value_true = True
value_false = False
sleep(1.2)
print("\nOperadores Lógicos")
print("AND")#AND significa que se os dois valores forem verdadeiros, então o resultado será True;
print("True AND False: ", value_true and value_false)
print("False AND True: ", value_false and value_true)
print("True AND True: ", value_true and value_true)
print("False AND False: ", value_false and value_false)
sleep(1.2)
print("OR")#OR significa que se ao menos tiver um valor verdadeiro, então o resultado será True;
print("True OR False: ", value_true or value_false)
print("False OR True: ", value_false or value_true)
print("True OR True: ", value_true or value_true)
print("False OR False: ", value_false or value_false)
sleep(1.2)
print("NOT")#NOT inverte o valor;
print("NOT True: ", not value_true)
print("NOT False: ", not value_false)
```
---
## 🗓️ Dia 5

✅ **Data:** 27/04/2025
📌 **Resumo:**

Hoje mergulhei em condições e repetições em Python!
Aprendi a usar if, else, elif e também dei meus primeiros passos com os laços while e for.
Foi tipo dar superpoderes pro código — agora ele toma decisões e repete ações sozinho! 🦾⚙️

Cada dia mais animado com o que tô construindo! Vamos firme! 💻🔥
```python
# #Programa para determinar se o número é ímpar ou par;
number = int(input("Digite um número: "))
if number % 2 == 0:
    print("O número", number, "é um número par")
else:
    print("O número", number, "é um número ímpar")

# #Programa para determinar se você é uma criança, jovem, adulto ou idoso;
age = int(input("Qual sua idade? "))
if age <= 12:
    print("Você uma criança")
elif age <= 18:
    print("Você é um jovem")
elif age <= 60:
    print("Você é um adulto")
else:
    print("Você é um idoso")

#Programa para determinar o maior valor;
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 >= num2:
    if num1 >= num3:
        print("O maior número é", num1)
    else:
        print("O maior número é", num3)
else:
    if num2 >= num3:
        print("O maior número é", num2)
    else:
        print("O maior número é", num3)

#Programa para calcular a soma de todos os números;
number = int(input("\nDigite um número positivo para calcular a soma até esse número; "))
sum = 0 
for n in range(1, number + 1):
    sum += n
print(f"\nA soma dos números de 1 a {number} é igual a {sum}.")

#Programa para saber o resultado um um número fatorial;
number = int(input("\nDigite o número para saber seu fatorial: "))
fatorial = 1
while number > 1:
    fatorial *= number
    number -= 1
print(f"O fatorial de {number} é igual a {fatorial}")
```
---
## 🗓️ Dia 6

✅ **Data:** 28/04/2025
📌 **Resumo:**

Hoje foi dia de aprender sobre funções e como elas ajudam a reutilizar código!
Agora meu código tá mais organizado, limpo e fácil de entender — nada de repetir blocos iguais mil vezes. Só chamo a função e pronto! 📦✨

Curti demais a ideia de dividir tudo em pedacinhos que fazem tarefas específicas.
Programar tá começando a parecer mágica (organizada)! 🧙‍♂️💻
```python
#Função Simples;
def greet_user(nome):
    print(f"Olá {nome}")

#greet_user("Anderson")
greet_user("Convidado") # Atualizando função 'greet_user'
print() # Chamando a função

#Calculo da área do retângulo;
def calculo(comprimento, largura):
    return comprimento * largura # Declarando o calculo

resultado = calculo(5, 4) # Declarando valores das props
print("O valor da área é", resultado)
print() # Chamando a função

#Escopo da Variável;
global_var = 10 # Valor incial da variável
print(f"O valor atual da variável é: {global_var}")

def modify_var():
    global_var = 20 # Atualizando a variável
    print(f"Atualizando valor dentro de uma função: {global_var}")

modify_var() # Chamando a função
print(f"O valor depois de chamar a função é: {global_var}") # Verificando valor da variável

def modify_global_var():
    global global_var # Declara que queremos usar a variável
    global_var = 20 # Atualizando valor de 'global_var'
    print(f"Atualizando valor dentro de uma função: {global_var}") # Alterando valor

modify_global_var() # Chamando a função
print(f"Valor atualizado depois de chamar a função: {global_var}")
```
---
## 🗓️ Dia 7

✅ **Data:** 29/04/2025
📌 **Resumo:**

Hoje foi dia de conhecer as listas e tuplas em Python!
Aprendi a guardar vários valores numa mesma variável e a manipular esses dados de várias formas: adicionar, acessar, remover… tudo na base da praticidade! 📚🛠️

As tuplas me surpreenderam por serem imutáveis — ótimas pra quando os dados não devem mudar.
Mais uma ferramenta na caixa! 🔧💻
```python
import time
import sys

# Lista 
list = ["filme", "série", "desenho", "documentário", "anime"]

while True:
    print("\nMenu")
    print("1. Ver generos")
    print("2. Adicionar elemento")
    print("3. Remover elemento")
    # print("4. Dividir lista")
    print("5. Sair")

    menu = int(input("Digite um número de 1 a 5: "))
    time.sleep(1.2)

    if menu == 1:
        print(list)
        time.sleep(1.2)
    elif menu == 2:
        add = input("Digite o que deseja adicionar: ")
        list.append(add)
        def loading(mensagem="Adicionando", repeticoes=3, delay=0.5):
            for _ in range(1):  # repete o ciclo algumas vezes
                for i in range(repeticoes + 1):
                    pontos = '.' * i
                    print(f'\r{mensagem}{pontos}{" " * (repeticoes - i)}', end='')
                    sys.stdout.flush()
                    time.sleep(delay)
            print(f"\n{add} adicionado!")
        loading()
        time.sleep(1.2)
    elif menu == 3:
        delete = input("Digite o que deseja remover: ")
        list.remove(delete)
        def loading(mensagem="Removendo", repeticoes=3, delay=0.5):
            for _ in range(2):  # repete o ciclo algumas vezes
                for i in range(repeticoes + 1):
                    pontos = '.' * i
                    print(f'\r{mensagem}{pontos}{" " * (repeticoes - i)}', end='')
                    sys.stdout.flush()
                    time.sleep(delay)
            print(f"\n{delete} removido!")
        loading()
        time.sleep(1.2)
    # elif menu == 4:
    #     print("Primeiro lado")  
    #     print("Segundo lado")
    #     n = "desenho"
    #     primeiroLado = menu[:n]
    #     segundoLado = menu[n:]
                                        #DIVIDIR A LISTA NO MEIO
    #     if n == 1:
    #         print(primeiroLado)
    #     elif n == 2:
    #         print(segundoLado)
    #     else:
    #         print("Escolha o número 1 ou 2: ")
    #     time.sleep(1.2)
    elif menu == 5:
        def loading(mensagem="Saindo", repeticoes=3, delay=0.5):
            for _ in range(2):  # repete o ciclo algumas vezes
                for i in range(repeticoes + 1):
                    pontos = '.' * i
                    print(f'\r{mensagem}{pontos}{" " * (repeticoes - i)}', end='')
                    sys.stdout.flush()
                    time.sleep(delay)
            print('\nPronto!')
        loading()
        break
    
    else:
        print("POR FAVOR, DIGITE UM NÚMERO INTEIRO DE 1 A 5")
        time.sleep(1)

# Tuplas
tupla = ("Anderson", "Gabriela", "Henrique", "Denis")
tupla2 = ("19", "26", "25", "24")
print(tupla)
print(tupla[1])
tuplaList = list(tupla) # Convertendo para uma lista
print(tupla)

# Utilizanndo operadores
print(len(tupla)) # Identificando quantos elementos possui
print(tupla + tupla2) # Juntando as tuplas
print(tupla *2) # Repetindo a tupla
```
---
## 🗓️ Dia 8

✅ **Data:** 30/04/2025
📌 **Resumo:**

Hoje o aprendizado foi sobre conjuntos e dicionários em Python!
Os conjuntos me mostraram como trabalhar com dados únicos, sem repetições — tipo uma limpeza automática nos valores duplicados.
Já os dicionários foram como criar mini bancos de dados, com chaves e valores pra organizar melhor as informações. 🔑📦
Cada estrutura nova abre um monte de possibilidades. Bora pro próximo!

```python
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
conjuntoUniao = meuConjunto.union(novoConjunto)
print(conjuntoUniao)

conjunto1 = {"banana", "maça", "kiwi"}
conjunto2 = {"pera", "goiaba", "banana"}

print("\nOperação intersection:")
inter = conjunto1.intersection(conjunto2)
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
```
---
## 🗓️ Dia 09

✅ **Data:** 01/05/2025
📌 **Resumo:**

Hoje eu criei um gerador de números aleatórios em Python! 🎲
Com ele, posso gerar tanto números inteiros quanto decimais de 1 a 100, tudo na base da escolha do usuário. Simples, mas super divertido de fazer! 😎

Foi uma ótima prática pra entender mais sobre bibliotecas como o random e também pra melhorar minhas habilidades de lógica e condições.
```python
import random

# Função para gerar um número aleatório (inteiro ou decimal)
def gerador_aleatorio():
    tipo = input("Digite 1 para número inteiro ou 2 para número decimal: ")
    if tipo == "1":
        numero = random.randint(1, 100)  # Número inteiro entre 1 e 100
        print(f"Número inteiro aleatório: {numero}")
    elif tipo == "2":
        numero = random.uniform(1, 100)  # Número decimal entre 1 e 100
        print(f"Número decimal aleatório: {numero:.2f}")
    else:
        print("Opção inválida. Escolha 1 ou 2.")
    
# Função para gerar apenas números inteiros
def gerador_inteiro():
    numero = random.randint(1, 100)  # Gera um número inteiro entre 1 e 100
    print(f"Número inteiro aleatório: {numero}")

print("=== GERADOR DE NÚMEROS ALEATÓRIOS ===")
gerador_aleatorio()

```
---
## 🗓️ Dia 13

✅ **Data:** 05/05/2025
📌 **Resumo:**

## 🗓️ Dia 14

✅ **Data:** 06/05/2025
📌 **Resumo:**