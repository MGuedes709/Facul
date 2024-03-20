numeros = [10, 20, 30, 40, 50]
def calcular_media(lista):
    soma = 0
    print(numeros)
    for i in numeros:
        soma = soma + i
    media = soma/len(numeros)
    return media

resultado = calcular_media (numeros)
print(f"A média dos números é:{resultado}")