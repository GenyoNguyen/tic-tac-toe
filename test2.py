x = []
while len(x) < 3:
    try:
        temp = input().split()
        for i in temp:
            x.append(float(i))
    except (ValueError, EOFError):
        continue
print(int(x[0]+(x[0]*x[2]/100)/12*x[1]))