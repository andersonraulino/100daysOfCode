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