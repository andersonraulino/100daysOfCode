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
