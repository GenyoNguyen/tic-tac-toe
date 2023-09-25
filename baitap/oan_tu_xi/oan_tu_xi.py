choices = ['BAO','KEO','BUA']
a = choices.index(input())
b = choices.index(input())

if a==b:
    print('DRAW')
elif (a-b == 1) or (a==0 and b==2):
    print('A WON')
else:
    print('B WON')