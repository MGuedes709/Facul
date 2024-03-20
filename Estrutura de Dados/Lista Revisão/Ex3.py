def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[j] > lista[i]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

lista = [1,2,3,4,5]
print(lista)
print(ordenar(lista))