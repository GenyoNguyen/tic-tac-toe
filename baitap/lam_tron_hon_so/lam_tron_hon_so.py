a,n = input().split()
a = float(a)
n = int(n)
s = n*a
if s-int(s) == 0.5:
    s = int(s) + 1
else:
    s = round(s)
r = s%n

if r!=0:
    print(str(int(s/n)),str(r)+'/'+str(n))
else:
    print(str(int(s/n)))