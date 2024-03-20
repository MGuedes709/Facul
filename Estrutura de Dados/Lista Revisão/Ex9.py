lista1 = [17,4,39,73,26]
lista2 = [2,99,51,55,23]
def somar_listas(lista1,lista2):
    soma = []
    for i in range(len(lista1)):
        soma.append(lista1[i] +lista2[i])
    return soma
resultado = somar_listas(lista1, lista2)
print(resultado)