Na = [0,0,0,0]
Ng = [0,0,0,0]

Na[0],Na[1],Na[2],Na[3] = input().split()
Ng[0],Ng[1],Ng[2],Ng[3] = input().split()

for i in range(4):
    Na[i] = int(Na[i])
    Ng[i] = int(Ng[i])

pt_Na, pt_Ng = 0,0

min_Na = Na[0]+Na[2]
max_Na = Na[1]+Na[3]
min_Ng = Ng[0]+Ng[2]
max_Ng = Ng[1]+Ng[3]

if max(min_Na,min_Ng) == min_Na:
    pt_Na += min_Na - min_Ng
else:
    pt_Ng += min_Ng - min_Na

if max(max_Na,max_Ng) == max_Na:
    pt_Na += max_Na - max_Ng
else:
    pt_Ng += max_Ng - max_Na

if pt_Na > pt_Ng:
    print('Nam')
elif pt_Na < pt_Ng:
    print('Nga')
else:
    print('Tie')