A, B = (1, 1)

def decimail_binario(numero):
    valor = list(range(32))
    for i in range(0,32):
        valor[i] = 0
    i = 0
    if numero > 1:
        while(numero > 1):
            valor[i] = 0
            if (numero%2) == 0:
                valor[i] = 0
            else:
                valor[i] = 1
            numero = int(numero/2)
            i += 1
            if numero == 0:
                valor[i] = 0
            else:
                valor[i] = 1
    else:
        valor[i] = numero

    return valor

def somaBinario(lista1, lista2):
    lista = list(range(32))

    for i in range(0, 32):
        lista[i] = 0
        if ((lista1[i] == 0) & (lista2[i] == 0)):
            lista[i] = 0
        elif ((lista1[i] == 0) & (lista2[i] == 1)) | ((lista1[i] == 1) & (lista2[i] == 0)):
            lista[i] = 1
        elif ((lista1[i] == 1) & (lista2[i] == 1)):
            lista[i] = 0
    return lista

def binario_Decimal(lista):
    soma = 0
    for i in range(31,-1,-1):
        if lista[i] == 1:
            soma += (2**i)
    return soma

while True:
    try:
        A, B = [int(x) for x in input().split()]
        lista = list(range(32))
        lista = somaBinario(decimail_binario(A), decimail_binario(B))
        print(binario_Decimal(lista))
    except EOFError:
        break
