from random import randrange

dice = [(2, True),
        (3, False), (3, False),
        (4, False), (4, True), (4, False),
        (5, False), (5, False), (5, False), (5, False),
        (6, False), (6, False), (6, True), (6, False), (6, False),
        (7, False), (7, False), (7, False), (7, False), (7, False), (7, False),
        (8, False), (8, False), (8, True), (8, False), (8, False),
        (9, False), (9, False), (9, False), (9, False),
        (10, False), (10, True), (10, False),
        (11, False), (11, False),
        (12, True)]

# list of player states, [location, in_jail?, rolls in jail count]
player = [[0, False, 0] for x in range(4)]

# location count
loc_count = [[0 for x in range(40)] for y in range(1000000)]

def move(player, roll):
    player[0] = (player[0] + roll[0]) % 40
    if(player[0] == 30):
        player[0] = 10
        player[1] = True
        player[2] = 0

for i in range(len(loc_count)):
    for l in range(50):
        for j in range(len(player)):
            if player[j][1]:
                #if player is in jail
                k = dice[randrange(len(dice))]
                if k[1] or player[j][2] >= 2:
                    player[j][2] = 0
                    player[j][1] = False
                    move(player[j], k)
                    loc_count[i][player[j][0]] = loc_count[i][player[j][0]] + 1
                    if k[1] and not(player[j][1]):
                        k = dice[randrange(len(dice))]
                        move(player[j], k)
                        loc_count[i][player[j][0]] = loc_count[i][player[j][0]] + 1
                        if k[1] and not(player[j][1]):
                            k = dice[randrange(len(dice))]
                            if k[1] and not(player[j][1]):
                                player[j][0] = 10
                                player[j][1] = True
                                loc_count[i][player[j][0]] = loc_count[i][player[j][0]] + 1
                            else:
                                move(player[j], k)
                                loc_count[i][player[j][0]] = loc_count[i][player[j][0]] + 1
                else:
                    player[j][2] = player[j][2] + 1
                    loc_count[i][10] = loc_count[i][10] + 1
            else:
                #if player is not in jail
                k = dice[randrange(len(dice))]
                move(player[j], k)
                loc_count[i][player[j][0]] = loc_count[i][player[j][0]] + 1
                if k[1] and not(player[j][1]):
                    k = dice[randrange(len(dice))]
                    move(player[j], k)
                    loc_count[i][player[j][0]] = loc_count[i][player[j][0]] + 1
                    if k[1] and not(player[j][1]):
                        k = dice[randrange(len(dice))]
                        if k[1] and not(player[j][1]):
                            player[j][0] = 10
                            player[j][1] = True
                            loc_count[i][player[j][0]] = loc_count[i][player[j][0]] + 1
                        else:
                            move(player[j], k)
                            loc_count[i][player[j][0]] = loc_count[i][player[j][0]] + 1
    #reset players for next game
    player = [[0, False, 0] for x in range(4)]

##for i in range(40):
##    print("{:2d}: ".format(i), end = '\t')
##    for j in range(100):
##        print("{:2d}".format(loc_count[j][i]), end = ' ')
##    print()
##print()
count = [0 for x in range(40)]
for i in range(40):
    for j in range(len(loc_count)):
        count[i] = count[i] + loc_count[j][i]

##for i in range(40):
##    print("{:2d}: {}".format(i, count[i]))
##print()
sc = [(x, count[x]) for x in range(40)]

sc.sort(key = lambda x: -x[1])

for x in range(len(sc)):
    print("{:2d}: {}".format(sc[x][0], sc[x][1]))
          

