num = int(input())
count = 0
aux = num + 1
while(count < 6):
    if (aux%2) != 0:
        count += 1
        print(aux)
    aux += 1
