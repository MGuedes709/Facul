lista = [42,25,67,42,95,2]
def sem_repetir(lista):
    conjunto = set(lista)
    return conjunto
resultado= sem_repetir(lista)
print(resultado)