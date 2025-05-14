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
## 🗓️ Dia 10

✅ **Data:** 02/05/2025
📌 **Resumo:**

Hoje eu trabalhei com o loop for e criei uma sequência de números de 1 a 10 de forma automática! 🔄
Simples, mas é incrível ver o código fazendo o trabalho repetitivo pra mim. 😎

Entendi melhor como controlar a repetição e como usar o range() pra definir o intervalo. Cada linha de código é um passo pra mais produtividade! 🚀
```python
for i in range(1, 11):# Cria uma sequência de números
    print(i)
```
---
## 🗓️ Dia 11

✅ **Data:** 03/05/2025
📌 **Resumo:**

Hoje foi dia de fazer uma sequência de números de 1 a 10 novamente, mas dessa vez usando o loop while! 🔄
Diferente do for, o while me deu mais controle, e eu precisei definir as condições direitinho pra não entrar num loop infinito. 😅

Mais uma ferramenta que entendi melhor e que me dá mais flexibilidade no código!
```python
# for i in range(2, 21, 2):
#     print(i)
numero = 2 # Número incial
while numero <= 20:
    print(numero)
    numero += 2 # Somando 2 sobre o valor anterior da variável 'numero'
    break
```
---
## 🗓️ Dia 12

✅ **Data:** 04/05/2025
📌 **Resumo:**

Hoje eu criei um programa em Python que verifica se um número é par ou ímpar! 🔢
O usuário digita o número, e o código faz a mágica — usando o operador % pra identificar se o resto da divisão por 2 é zero (par) ou não (ímpar).

Simples, mas super útil pra treinar lógica e condições! 😎💡
Cada dia, mais domínio do código!
```python
def verificador(valor: int): # Declara a propriedade como um valor inteiro
    if valor % 2 == 0:
        # Testei fazer com um print, porém ele sempre me retornou o resultado e logo abaixo, ele retornou a mensagem "None". Para evitar isso, devemos utilizar um 'return'
        return f"O número {numero} é par!"
    elif valor % 2 == 1:
        return f"O número {numero} é ímpar!"
    else:
        return "Digite um número válido!"
numero = int(input("Digite um número inteiro: "))
resultado = verificador(numero)
print(resultado)
```
---
## 🗓️ Dia 13

✅ **Data:** 05/05/2025
📌 **Resumo:**

Hoje eu desenvolvi um programa em Python que identifica o maior número entre três valores digitados pelo usuário! 🔍📊

Foi uma ótima prática pra reforçar o uso de condições (if, elif, else) e lógica, garantindo que o código sempre encontre o maior valor, não importa a combinação. 💡
```python
def verificarMaiorNumero(n1: int, n2: int, n3: int) -> int:
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o último número: "))
resultado = verificarMaiorNumero(num1, num2, num3)
print(f"O maior número é {resultado}")
```
---
## 🗓️ Dia 14

✅ **Data:** 06/05/2025
📌 **Resumo:**

Hoje eu criei um programa em Python que verifica se um ano é bissexto ou não! 📅🌐

O usuário digita o ano, e o código analisa com base nas regras:
✅ Divisível por 4, mas não por 100 (a menos que seja divisível por 400).
```python
def verificar_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return f"{ano} é um ano bissexto."
    else:
        return f"{ano} não é um ano bissexto."

try:
    ano = int(input("Digite um ano: "))
    print(verificar_ano_bissexto(ano))
except ValueError:
    print("Por favor, insira um valor numérico válido.")
```
---
## 🗓️ Dia 15

✅ **Data:** 07/05/2025
📌 **Resumo:**
Hoje foi dia de criar uma função em Python para calcular o fatorial de um número! 🔢⚡

Foi uma ótima prática pra reforçar o conceito de funções e lógica matemática.
O usuário digita o número e o código retorna o fatorial dele — multiplicando todos os números de 1 até o valor escolhido.
```python
def calcular_fatorial(n):
    if n < 0:
        return "Fatorial não é definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial

try:
    numero = int(input("Digite um número: "))
    print(f"O fatorial de {numero} é: {calcular_fatorial(numero)}")
except ValueError:
    print("Por favor, insira um valor numérico válido.")
```
---
## 🗓️ Dia 16

✅ **Data:** 08/05/2025
📌 **Resumo:**

Hoje eu criei uma função em Python que verifica se uma palavra é um palíndromo! 🔁✨

O usuário digita uma palavra, e o código verifica se ela é igual quando lida de trás pra frente.
Um ótimo exercício pra entender melhor manipulação de strings e lógica de comparação! 😎

Exemplos:
✅ "arara" é um palíndromo.
❌ "python" não é.
```python
def verificar_palindromo(texto):
    # Remove espaços e transforma em minúsculas
    texto = texto.replace(" ", "").lower()
    
    # Verifica se a string é igual ao seu reverso
    if texto == texto[::-1]:
        return "A palavra é um palíndromo."
    else:
        return "A palavra não é um palíndromo."

# Testando a função
entrada = input("Digite uma palavra: ")
print(verificar_palindromo(entrada))

```
---
## 🗓️ Dia 17

✅ **Data:** 09/05/2025
📌 **Resumo:**

Hoje eu criei uma função em Python que conta as vogais em uma palavra! 🔡✨

O usuário digita a palavra, e o código percorre cada letra, verificando se é uma vogal (a, e, i, o, u).
Um ótimo exercício pra treinar loops, condições e manipulação de strings! 😎

Exemplo:
✅ "python" tem 1 vogal.
✅ "desenvolvimento" tem 6 vogais.
```python
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    
    return f"A string contém {contador} vogal(is)."

# Testando a função
entrada = input("Digite uma string: ")
print(contar_vogais(entrada))

```
---
## 🗓️ Dia 18

✅ **Data:** 10/05/2025
📌 **Resumo:**

Hoje eu criei uma função em Python que calcula a soma de todos os elementos em uma lista! ➕📋

O código percorre cada item somando tudo.
Exemplo:
✅ Para a lista [1, 2, 3, 4, 5], a soma é 15.
```python
def somar_elementos(lista):
    return sum(lista)

numeros = [1, 2, 3, 4, 5]

# Testando a função
print(f"A soma dos elementos da lista {numeros} é: {somar_elementos(numeros)}")
```
---
## 🗓️ Dia 19

✅ **Data:** 11/05/2025
📌 **Resumo:**

Hoje eu criei uma função em Python que encontra o elemento máximo em uma lista! 🔝📋

O código percorre todos os itens, retornando o maior valor.
Foi uma boa prática pra aprimorar a lógica e entender mais sobre manipulação de listas! 😎

Exemplo:
✅ Para a lista [3, 1, 9, 7, 2], o maior número é 9.
```python
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

```
---
## 🗓️ Dia 20

✅ **Data:** 12/05/2025
📌 **Resumo:**

Hoje eu criei uma função em Python que gera a sequência de Fibonacci até um certo limite! 🔢✨

O usuário escolhe o limite, e o código vai somando os dois últimos números pra formar o próximo da sequência.
Foi uma ótima prática pra entender melhor loops e lógica matemática! 😎

Exemplo:
✅ Para o limite 20, a sequência é: 0, 1, 1, 2, 3, 5, 8, 13.
```python
def fibonacci_ate_limite(limite):
    sequencia = [0, 1]
    
    while True:
        proximo = sequencia[-1] + sequencia[-2]
        if proximo > limite:
            break
        sequencia.append(proximo)
    
    return sequencia

# Testando a função
limite = int(input("Digite o limite para a sequência de Fibonacci: "))
print(f"A sequência de Fibonacci até {limite} é: {fibonacci_ate_limite(limite)}")
```
---
# 🗓️ Dia 21

✅ **Data:** 13/05/2025
📌 **Resumo:**

Hoje criei uma função para inverter uma lista de elementos!

O usuário fornece a lista e para reverter ela, eu ultilizei doi métodos.

O primeiro utilizei um insert dentro de um loop, para percorrer todos os elementos e mandar cada um para a posição '0'. Assim, faria com que o último elemento se tornasse o primeiro.

No segundo utilizei o método [:: -1] de fatiamento (slicing). Para em caso de ter uma lista com diversos elementos, esse método é mais recomendado, por conta da sua rapidez. 😎
```python
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
```
---
# 🗓️ Dia 22

✅ **Data:** 14/05/2025
📌 **Resumo:**

Criei uma função para remover todos os elementos duplicados, utilizando a função 'set'. Assim pude criar uma lista somente com elementos únicos.

```python
def removerDuplicadas(lista):
    return list(set(lista)) # set é uma coleção não ordenada de elementos únicos, o que o torna ideal para remover duplicatas

numeros = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8]
print(f"Lista com duplicadas: {numeros}")
print(f"Lista sem duplicadas: {removerDuplicadas(numeros)}")
```