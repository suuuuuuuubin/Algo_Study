def rotate_dice (rotate, dice):
    new_dice = [0]*6

    for idx, r in enumerate(rotate) :
        new_dice[idx] = dice[r]

    return new_dice

if __name__ =="__main__":

    n, m, x, y, k = map(int, input().split())
    dice_map = [list(map(int, input().split())) for _ in range(n)]

    operation = list(map(int, input().split()))


    move = [[], [0, 1], [0, -1], [-1,0], [1,0]] # 동, 서, 북, 남
    dice_rotate = [[],
                   [2, 1, 5, 0, 4, 3],
                   [3, 1, 0, 5, 4, 2],
                   [4, 0, 2, 3, 5, 1],
                   [1, 5, 2, 3, 0, 4]] # 동, 서, 북, 남
    dice = [0] * 6
    for o in operation:
        next_x, next_y = x+move[o][0], y+move[o][1]
        if next_x <0 or next_x>=n or next_y<0 or next_y>=m:
            # print(dice[0])
            continue
        else:
            x, y = next_x, next_y
            dice = rotate_dice(dice_rotate[o], dice)
            # 0 : 윗면, 5 : 바닥면
            if dice_map[x][y] == 0:
                dice_map[x][y] = dice[5]
                # dice[5] = 0
                print(dice[0])
            else:
                dice[5] = dice_map[x][y]
                dice_map[x][y] = 0
                print(dice[0])

