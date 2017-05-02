def Main(A, B):
    print(A^B)
while True:
    try:
        A, B = [int(x) for x in input().split()]
    except EOFError:
        break
    Main(A, B)
