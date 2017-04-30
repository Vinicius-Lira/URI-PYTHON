hora_inicial, min_inicial, hora_final, min_final = [int(x) for x in input().split()]

def calculaHora(hora_inicial, min_inicial, hora_final, min_final):
    if hora_inicial > hora_final:
        horas = ((24 - hora_inicial) + hora_final)

        if min_inicial > 0:
            min = 60 - min_inicial

        minutos = (min + min_final)
        if (hora_inicial > 0) & (min_inicial > 0):
            horas -= 1

        while (minutos > 60) | (minutos == 60):
            horas += 1
            minutos -= 60

        return (horas, minutos)
    elif hora_inicial < hora_final:
        horas = hora_final - hora_inicial
        if min_inicial > 0:
            horas -= 1
            minutos = (60 - min_inicial) + min_final
            while (minutos > 60) | (minutos == 60):
                horas += 1
                minutos -= 60
        else:
            minutos += min_final
        return (horas, minutos)
    else:
        return (24, 0)

hora, minutos = calculaHora(hora_inicial, min_inicial, hora_final, min_final)
print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hora, minutos))
