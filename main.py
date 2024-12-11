import random

game_plain = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

flag_plain = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# this plain is used to see if a value has been changed or not
# (it will be restored after every move)


def block_generator(plain):
    i, j = random.randrange(0, 4), random.randrange(0, 4)
    if plain[i][j] != 0:
        block_generator(plain)
    else:
        plain[i][j] = 2
        return plain


def move_maker(plain, flag):
    move = input(': ')
    not_changed = True

    if move == 'w':
        i = 1
        while i<4:
            j = 0
            while j<4:
                if plain[i][j] != 0:
                    b = i

                    while b>0:
                        if plain[b-1][j] == 0:
                            not_changed = False
                            tmp = plain[b][j]
                            plain[b][j] = 0
                            plain[b-1][j] = tmp
                        elif (plain[b-1][j] == plain[b][j] != 0 and
                              flag[b-1][j] == flag[b][j] == 0):
                            not_changed = False
                            plain[b-1][j] *= 2
                            flag[b-1][j] = 1
                            plain[b][j] = 0
                        b -= 1
                j += 1
            i += 1


    if move == 's':
        i = 2
        while i>-1:
            j = 3
            while j>-1:
                if plain[i][j] != 0:
                    b = i

                    while b<3:
                        if plain[b+1][j] == 0:
                            not_changed = False
                            tmp = plain[b][j]
                            plain[b][j] = 0
                            plain[b+1][j] = tmp
                        elif (plain[b+1][j] == plain[b][j] != 0 and
                              flag[b+1][j] == flag[b][j] == 0):
                            not_changed = False
                            plain[b+1][j] *= 2
                            flag[b+1][j] = 1
                            plain[b][j] = 0
                        b += 1
                j -= 1
            i -= 1


    if move == 'a':
        j = 1
        while j<4:
            i = 0
            while i<4:
                if plain[i][j] != 0:
                    b = j

                    while b>0:
                        if plain[i][b-1] == 0:
                            not_changed = False
                            tmp = plain[i][b]
                            plain[i][b] = 0
                            plain[i][b-1] = tmp
                        elif (plain[i][b-1] == plain[i][b] != 0 and
                              flag[i][b-1] == flag[i][b] == 0):
                            not_changed = False
                            plain[i][b-1] *= 2
                            flag[i][b-1] = 1
                            plain[i][b] = 0
                        b -= 1
                i += 1
            j += 1


    if move == 'd':
        j = 2
        while j>-1:
            i = 3
            while i>-1:
                if plain[i][j] != 0:
                    b = j

                    while b<3:
                        if plain[i][b+1] == 0:
                            not_changed = False
                            tmp = plain[i][b]
                            plain[i][b] = 0
                            plain[i][b+1] = tmp
                        elif (plain[i][b+1] == plain[i][b] != 0 and
                              flag[i][b+1] == flag[i][b] == 0):
                            not_changed = False
                            plain[i][b+1] *= 2
                            flag[i][b+1] = 1
                            plain[i][b] = 0
                        b += 1
                i -= 1
            j -= 1


    if not_changed :
        move_maker(plain, flag)


block_generator(game_plain)
block_generator(game_plain)


def play(plain, flag):

    flag = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    for i1 in range(4):
        print(game_plain[i1])

    move_maker(plain, flag)
    block_generator(plain)
    play(plain, flag)


play(game_plain, flag_plain)