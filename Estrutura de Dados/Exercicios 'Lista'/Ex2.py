numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
def filtrar_pares(lista):
    for i in numeros:
        if i % 2!=0:
            numeros.remove(i)
    return

pares = filtrar_pares(numeros)
print("Números pares:", numeros)