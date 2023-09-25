def isInMiddle(p,p1,p2):
  return True if p1<=p<=p2 else False

def eliminateDuplicates(li):
  newLi = []
  for i1 in range(len(li)):
    b = False
    for i2 in range(i1+1,len(li)):
      if li[i1]==li[i2]:
        b = True
        break
    if not b:
      newLi.append(li[i1])
  return newLi

def hasSamePos(pList):
  result = 0
  for i1 in range(len(pList)):
    for i2 in range(i1+1,len(pList)):
        if pList[i1]==pList[i2]:
            result+=1
  return result

# Data
x = input().split()
for i in range(len(x)):
  x[i] = int(x[i])

s1 = (x[2]-x[0])*(x[3]-x[1])
s2 = (x[7]-x[5])*(x[6]-x[4])
p = []
for i in range(2):
  p.append([x[2*i],x[1]])
  p.append([x[2*i],x[3]])
for i in range(2):
  p.append([x[2*i+4],x[5]])
  p.append([x[2*i+4],x[7]])

untrimmedTarget = []
indices = []
for i in range(4):
  if isInMiddle(p[i][0],x[4],x[6]) and isInMiddle(p[i][1],x[5],x[7]):
    untrimmedTarget.append(p[i])
    indices.append(i)
for i in range(4, 8):
  if isInMiddle(p[i][0],x[0],x[2]) and isInMiddle(p[i][1],x[1],x[3]):
    untrimmedTarget.append(p[i])
    indices.append(i)

samePos = hasSamePos(untrimmedTarget)

target = eliminateDuplicates(untrimmedTarget)


sameRect = False
if indices==[0,1,2,3] or indices==[4,5,6,7]:
  sameRect = True
      
#Algo
r = 0

#Case 1: Target=2
if len(untrimmedTarget)==2:
  #Case 1.1: No duplicates
  if not samePos:
    #Case 1.1.1: Has same posX or posY
    if(target[0][1]==target[1][1]):
      temp = target[1][0]-target[0][0]
      if((p.index(target[0])==1 and p.index(target[1])==3) or (p.index(target[0])==4 and p.index(target[1])==6)):
        r = temp*(x[3]-x[5])
      else:
        r = temp*(x[7]-x[1])
    elif(target[0][0]==target[1][0]):
      temp = target[1][1]-target[0][1]
      if((p.index(target[0])==2 and p.index(target[1])==3) or (p.index(target[0])==4 and p.index(target[1])==5)):
        r = temp*(x[2]-x[4])
      else:
        r = temp*(x[6]-x[0])
    #Case 1.1.2: 2 diagonal points
    else:
      r = abs((target[0][0]-target[1][0])*(target[0][1]-target[1][1]))
  #Case 1.2: Has duplicates: r=0
#Case 3: Target>=3
elif not ((len(untrimmedTarget)==3 and samePos==1) or (len(untrimmedTarget)==4 and samePos==2)) and len(untrimmedTarget)!=0:
  r = max(abs(target[0][0]-target[1][0]),abs(target[1][0]-target[2][0]))*max(abs(target[0][1]-target[1][1]),abs(target[1][1]-target[2][1]))

print(s1+s2-r)