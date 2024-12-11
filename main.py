import random

game_plain = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# game_plain[3][3] = 5


def block_generator(plain):
    i, j = random.randrange(0, 4), random.randrange(0, 4)
    if plain[i][j] != 0:
        block_generator(plain)
    else:
        plain[i][j] = 2
        return plain


def move_maker(plain):
    move = input(': ')
    if move == 'w':
        i = 1
        while i<4:
            j = 0
            while j<4:
                if plain[i][j] != 0:
                    b = i

                    while b>0:
                        if plain[b-1][j] == 0:
                            tmp = plain[b][j]
                            plain[b][j] = 0
                            plain[b-1][j] = tmp
                        elif plain[b-1][j] == plain[b][j] != 0:
                            plain[b-1][j] *= 2
                            plain[b][j] = 0
                        b -= 1
                j += 1
            i += 1


block_generator(game_plain)
block_generator(game_plain)


def play(plain):

    for i1 in range(4):
        print(game_plain[i1])

    move_maker(plain)
    block_generator(plain)

    play(plain)


play(game_plain)