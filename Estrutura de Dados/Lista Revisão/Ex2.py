def definir_maior(lista):
    maior = 0
    for i in lista:    
        if i > maior:
            maior = i
    return maior
lista = [10,12,14,16,23,13,7]
resultado = definir_maior(lista)
print(f"O maior número foi o : {resultado}")
