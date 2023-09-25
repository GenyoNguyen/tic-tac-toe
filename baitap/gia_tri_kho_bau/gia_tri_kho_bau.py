v1,w1,v2,w2 = int(input()),int(input()),int(input()),int(input())
maxW = int(input())

val = 0

if (w1+w2) <= maxW:
    val = max(v1+v2,val)
if w1 <= maxW:
    val = max(val,v1)
if w2 <= maxW:
    val = max(val,v2)
print(val)