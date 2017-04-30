positivo = 0
media = 0
for i in range(0,6):
    numero = float(input())
    if numero > 0:
        positivo += 1
        media += numero

print("%d valores positivos" %positivo )
print("%0.1f" %(media/positivo))
