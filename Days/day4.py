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