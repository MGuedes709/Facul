def contagem_semelhantes(lista):
    contagem = 0
    for i in lista: 
        if i == 25:
            contagem = contagem + 1
    return contagem        
lista = [25,47,92,50,21,25,34,96,66,25]    
resultado = contagem_semelhantes (lista)
print(f"O número de vezes que o 25 apareceu é :{resultado}")