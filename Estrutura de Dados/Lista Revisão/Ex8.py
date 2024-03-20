lista1 = [17,4,39,73,26,8]
lista2 = [2,99,51,55,23]
def juntar_listas(lista1,lista2):
    for i in lista2:
        lista1.append(i)
    return lista1
resultado = juntar_listas(lista1,lista2)
print(resultado)
