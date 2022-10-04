'''Дан многомерный список в котором находится результат игры в крестики нолики,
выяснить какой игрок победил (x или o),
если никто не победил вывести "Ничья".
Необходимо учитывать то,
что есть разные выигрышные варианты
и программа должна их распознавать. '''


a = [['X', 'X', 'O'],
     ['O', 'O', 'X'],
     ['X', 'O', 'X']]

win = 0
for i in range(len(a)):
    for j in range(len(a[i])):

        if a[0][0] == 'X' and a[1][0] == 'X' and a[2][0] == 'X':
            win = 1
        elif a[0][1] == 'X' and a[1][1] == 'X' and a[2][1] == 'X':
            win = 1

        elif a[0][2] == 'X' and a[1][2] == 'X' and a[2][2] == 'X':
            win = 1

        elif a[0][0] == 'X' and a[0][1] == 'X' and a[0][2] == 'X':
            win = 1

        elif a[1][0] == 'X' and a[1][1] == 'X' and a[1][2] == 'X':
            win = 1

        elif a[2][0] == 'X' and a[2][1] == 'X' and a[2][2] == 'X':
            win = 1

        elif a[0][0] == 'X' and a[1][1] == 'X' and a[2][2] == 'X':
            win = 1

        elif a[0][2] == 'X' and a[1][1] == 'X' and a[2][0] == 'X':
            win = 1

        elif a[0][0] == 'O' and a[1][0] == 'O' and a[2][0] == 'O':
            win = -1

        elif a[0][1] == 'O' and a[1][1] == 'O' and a[2][1] == 'O':
            win = -1

        elif a[0][2] == 'O' and a[1][2] == 'O' and a[2][2] == 'O':
            win = -1

        elif a[0][0] == 'O' and a[0][1] == 'O' and a[0][2] == 'O':
            win = -1

        elif a[1][0] == 'O' and a[1][1] == 'O' and a[1][2] == 'O':
            win = -1

        elif a[2][0] == 'O' and a[2][1] == 'O' and a[2][2] == 'O':
            win = -1

        elif a[0][0] == 'O' and a[1][1] == 'O' and a[2][2] == 'O':
            win = -1

        elif a[0][2] == 'O' and a[1][1] == 'O' and a[2][0] == 'O':
            win = -1

    if win == 1:
        print("Победа игрока 'X'")
    elif win == -1:
        print("Победа игрока 'O'")
    else:
        print('Ничья')
