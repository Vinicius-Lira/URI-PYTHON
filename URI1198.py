while True:
    try:
        H, O = [int(x) for x in input().split()]
    except EOFError:
        break
    diferenca = H - O
    if diferenca < 0:
        diferenca *= -1
    print(diferenca)
