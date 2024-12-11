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