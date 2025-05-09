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