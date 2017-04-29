hora_inicial, min_inicial, hora_final, min_final = [int(x) for x in input().split()]

horaMinIni = hora_inicial * 60
horaMinFin = hora_final * 60

def calculaHora(horaMinIni, horaMinFin):
    if horaMinIni > horaMinFin:
        return (horaMinIni - horaMinFin)/60
    elif horaMinFin > horaMinIni:
        return (horaMinFin - horaMinIni)/60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(calculaHora(hora_inicial, hora_final), calculaMinutos(min_inicial, min_final)))
