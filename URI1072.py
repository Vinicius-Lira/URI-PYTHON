N = int(input())
in_ , out = (0 ,0)
for i in range(0, N):
    num = int(input())
    if (num >= 10) & (num <= 20):
        in_ += 1
    else:
        out += 1
print("%d in" %in_)
print("%d out" %out)
