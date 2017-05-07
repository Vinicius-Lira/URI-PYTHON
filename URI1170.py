N = int(input())
for i in range(0, N):
    C = float(input())
    dias = 0
    while True:
        dias += 1
        C /= 2
        if C <= 1:
            break
    print("%d dias" %dias)
