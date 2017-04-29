hora_inicial, hora_final = [int(x) for x in input().split()]

def calculaHoraDia(hora):
    return 24 - hora

def horaIgual():
    return 24

if (hora_inicial > hora_final) | (hora_final > hora_inicial):
    if hora_inicial > hora_final:
        print("O JOGO DUROU %d HORA(S)" %(calculaHoraDia(hora_inicial) + hora_final))
    elif hora_final > hora_inicial:
        print("O JOGO DUROU %d HORA(S)" %(calculaHoraDia(hora_inicial) - calculaHoraDia(hora_final)))
elif hora_final == hora_inicial:
    print("O JOGO DUROU %d HORA(S)" %horaIgual())
