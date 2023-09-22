import math

can = ['CANH','TAN','NHAM','QUY','GIAP','AT','BINH','DINH','MAU','KY']
giap = ['THAN','DAU','TUAT','HOI','TY\'','SUU','DAN','MEO','THIN','TY.','NGO','MUI']

a = int(input())
if a<0:
    print(can[(11+a)%10],giap[(13+a)%12])
else:
    print(can[a%10],giap[a%12])