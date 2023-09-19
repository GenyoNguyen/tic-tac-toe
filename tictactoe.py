import os
os.system('cls')

board = ['*','*','*','*','*','*','*','*','*']

for i in range(9):
    os.system('cls')
    for j in range(3):
        print(board[3*j],board[3*j+1],board[3*j+2])
    
    while True:
        if i%2==0:
            print("Player 1's turn!")
            print("Which square would you like to choose: ")
            x = int(input())
            if x>9 or x<0 or board[x-1]!='*':
                print("Error! Press any key to choose again")
                input()
                continue
            board[x-1] = 'X'
            break
        else:
            print("Player 2's turn!")
            print("Which square would you like to choose: ")
            x = int(input())
            if x>9 or x<0 or board[x-1]!='*':
                print("Error! Press any key to choose again")
                input()
                continue
            board[x-1] = 'O'
            break
    winner = '*'
    for i in range(3):
        if(board[3*i]!='*' and board[3*i]==board[3*i+1]==board[3*i+2]):
            winner = board[3*i]
            break
        if(board[i]!='*' and board[i]==board[i+3]==board[i+6]):
            winner = board[i]
            break
    if board[4]!='*' and (board[0]==board[4]==board[8] or board[2]==board[4]==board[6]):
        winner = board[4]
    if winner == 'X':
        os.system('cls')
        for j in range(3):
            print(board[3*j],board[3*j+1],board[3*j+2])
        print('Player 1 wins!')
        break
    elif winner == 'O':
        os.system('cls')
        for j in range(3):
            print(board[3*j],board[3*j+1],board[3*j+2])
        print('Player 2 wins!')
        break

if winner == '*':
    os.system('cls')
    for j in range(3):
        print(board[3*j],board[3*j+1],board[3*j+2])
    print('Draw!')