N = int(input())
for i in range(1, N + 1):
    num = int(input())
    if num == 0:
        print("NULL")
    elif (num%2) == 0:
        if num > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        if num > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
