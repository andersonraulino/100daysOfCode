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