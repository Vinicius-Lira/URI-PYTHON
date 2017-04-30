renda = float(input())

def impostorenda(renda):
    valorImposto = 0
    if renda <= 2000:
        print("Isento")

    if ((renda > 2000) & (renda <= 3000)):
        valor = renda - 2000
        taxa = 8
        valorImposto += ((valor * taxa)/100)

    if ((renda > 3000) & (renda <= 4500)):
        valor = renda - 3000
        taxa = 18
        valorImposto += ((1000 * 8)/100)
        if valor > 1000:
            valorImposto += ((1000 * taxa)/100)
            valor -= 1000
        valorImposto += ((valor * taxa)/100)

    if renda > 4500:
        valor = renda - 4500
        valorImposto += ((1000 * 8)/100)
        valorImposto += ((1000 * 18)/100)
        valorImposto += ((500 * 18)/100)

        while(valor > 0):
            taxa = 28
            if valor >= 1000:
                valorImposto += ((1000 * taxa)/100)
                valor -= 1000
            elif valor < 1000:
                valorImposto += ((valor * taxa)/100)
                valor -= valor
    if renda > 2000:
        print("R$ %0.2f" %valorImposto)

impostorenda(renda)
