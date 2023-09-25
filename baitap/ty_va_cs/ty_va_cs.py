x = input().split()
for i in range(len(x)):
    x[i] = bool(int(x[i]))

if(x[0] and not x[1]) or (x[1] and not x[2]) or (not x[1] and x[2] and not x[3]):
    print(0)
else:
    print(1)