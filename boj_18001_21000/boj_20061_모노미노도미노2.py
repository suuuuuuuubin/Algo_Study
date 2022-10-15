import sys


def move_right(block):

    # t=1, 1x1 block / t=2, 1x2 block : 가로 block / t=3, 세로 2x1 block
    # x는 행, y는 열을 의미

    t, x, y = block
    if t==1:
        cur_x, cur_y = x, y
        for i in range(10-y):
            if board_map[cur_x][cur_y] == 1 :
                # cur_y -=1
                break
            else :
                cur_y+=1

        board_map[cur_x][cur_y-1] = 1

    elif t==2: #가로 block
        cur_x, cur_y = x, y  # y+1 을 고려해야함
        for i in range(9 - y):
            if board_map[cur_x][cur_y + 1] == 1:
                break
            else:
                cur_y += 1

        board_map[cur_x][cur_y - 1] = 1
        board_map[cur_x][cur_y] = 1

    else : #세로 block
        cur_x, cur_y = x, y  # x, x+1까지 고려해야함
        for i in range(10 - y):
            if board_map[cur_x][cur_y] == 1 or board_map[cur_x + 1][cur_y] == 1:
                break
            else:
                cur_y += 1

        board_map[cur_x][cur_y - 1] = 1
        board_map[cur_x + 1][cur_y - 1] = 1


def move_down (block):
    # t=1, 1x1 block / t=2, 1x2 block : 가로 block / t=3, 2x1 block
    # x는 행, y는 열을 의미

    t, x, y = block
    if t == 1:
        cur_x, cur_y = x, y
        for i in range(10 - x):
            if board_map[cur_x][cur_y] == 1:
                break
            else:
                cur_x += 1
        board_map[cur_x-1][cur_y] = 1

    elif t == 2:  # 가로 block
        cur_x, cur_y = x, y  # y, y+1까지 고려해야함
        for i in range(10 - x):
            if board_map[cur_x][cur_y] == 1 or board_map[cur_x][cur_y + 1] == 1:
                break
            else:
                cur_x += 1

        board_map[cur_x - 1][cur_y] = 1
        board_map[cur_x - 1][cur_y + 1] = 1

    else:
        cur_x, cur_y = x, y  # x+1 을 고려해야함
        for i in range(9 - x):
            if board_map[cur_x + 1][cur_y] == 1:
                break
            else:
                cur_x += 1

        board_map[cur_x - 1][cur_y] = 1
        board_map[cur_x][cur_y] = 1
def get_score ():
    score=0
    c=9
    while c>=4:
        line = [val[c] for val in board_map[0:4]]
        if sum(line) == 4:
            score +=1
            for i in range(4):
                for j in range(c-1, 3, -1):
                    board_map[i][j+1] = board_map[i][j]
                board_map[i][4] = 0
        else:
            c -= 1

    r = 9
    while r>=4:
        line = [board_map[r][i] for i in range(4)]
        if sum(line) == 4:
            score += 1
            for i in range(r-1, 3, -1):
                for j in range(4):
                    board_map[i+1][j] = board_map[i][j]
            board_map[4] = [0]*10
        else:
            r-=1

    return score

def push():

    push = False
    for c in (4,5):
        line = [val[c] for val in board_map[0:4]]
        if sum(line) > 0:
            push = True
            break
    if push :
        gap = 6-c
        for i in range(4):
            for j in range(9-gap, 3, -1):
                board_map[i][j+gap] = board_map[i][j]
            for j in range(gap):
                board_map[i][5-j] = 0

    push = False
    for r in (4, 5):
        line = [board_map[r][i] for i in range(4)]
        if sum(line) > 0:
            push = True
            break
    # print(push)
    if push:
        gap = 6 - r
        for i in range(9 - gap, 3, -1):
            for j in range(4):
                board_map[i + gap][j] = board_map[i][j]
        # print(push)
        # print_board(board_map)
        # print(push)
        # board_map[5] = [0] * 10
        # board_map[4] = [0] * 10
        for i in range(gap):
            board_map[5-i] = [0] * 10
        # print_board(board_map)
        # print(push)


def print_board(board):
    for line in board:
        print(line)

if __name__ =="__main__":

    sys.stdin = open("../input.txt")
    N = int(sys.stdin.readline())
    tile_ls = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # print(tile_ls)
    board_map = [[0]*10 for i in range(10)]

    score = 0
    for tile in tile_ls:
        move_right(tile)
        move_down(tile)
        # print("moveboard")
        # print_board(board_map)
        score+=get_score()
        push()
        print()
        print_board(board_map)


    print(score)
    total = 0
    for line in board_map:
        total += sum(line)
    # print(sum(board_map))
    print(total)