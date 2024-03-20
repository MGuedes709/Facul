def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[j] < lista[i]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

lista = [100,60,30,25,10]
print(lista)
print(ordenar(lista))