def fatorial(num):
    fatorial = 1
    for i in range(1,num + 1):
        fatorial = fatorial * i
    return fatorial

while True:
    try:
        M, N = [int(x) for x in input().split()]
    except EOFError:
        break
    print(fatorial(M) + fatorial(N))
