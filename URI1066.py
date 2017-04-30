positivos, negativos, impares, pares = (0, 0, 0, 0)
for i in range(0, 5):
    num = int(input())
    if (num%2) == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("%d valor(es) par(es)" %pares)
print("%d valor(es) impar(es)" %impares)
print("%d valor(es) positivo(s)" %positivos)
print("%d valor(es) negativo(s)" %negativos)
