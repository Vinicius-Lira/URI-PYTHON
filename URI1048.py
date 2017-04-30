salario = float(input())

def salarionovo(salario):
    if salario <= 400:
        percentual = 15
        reajuste = ((salario * percentual)/100)
        novosalario = salario + reajuste
        return (novosalario, reajuste, percentual)
    elif (salario > 400) & (salario <= 800):
        percentual = 12
        reajuste = ((salario * percentual)/100)
        novosalario = salario + reajuste
        return (novosalario, reajuste, percentual)
    elif (salario > 800) & (salario <= 1200):
        percentual = 10
        reajuste = ((salario * percentual)/100)
        novosalario = salario + reajuste
        return (novosalario, reajuste, percentual)
    elif (salario > 1200) & (salario <= 2000):
        percentual = 7
        reajuste = ((salario * percentual)/100)
        novosalario = salario + reajuste
        return (novosalario, reajuste, percentual)
    elif salario > 2000:
        percentual = 4
        reajuste = ((salario * percentual)/100)
        novosalario = salario + reajuste
        return (novosalario, reajuste, percentual)

novosalario, reajuste, percentual = salarionovo(salario)
print("Novo salario: %0.2f" %novosalario)
print("Reajuste ganho: %0.2f" %reajuste)
print("Em percentual: %d %%" %percentual)
