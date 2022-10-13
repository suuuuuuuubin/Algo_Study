import sys

def print_map(coord_map):
    for line in coord_map:
        print(line)

    print()
if __name__ == "__main__":
    sys.stdin = open('../input.txt','r')

    n = int(sys.stdin.readline())
    dragon_ls = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # print(dragon_ls)
    k = 101
    coord_map = [[0]*k for _ in range(k)]
    move_amount = [(1,0),(0,-1),(-1,0), (0,1)] # 0 : right, 1: up, 2: left, 3: down
    for idx, dragon in enumerate(dragon_ls):
        x, y, d, g = dragon
        move = [d]
        for i in range(g):
            new_move = move[:]
            for m_idx in range(len(move)-1, -1, -1):
                m = move[m_idx]
                new_move.append((m+1)%4)
            move = new_move

        cur_x, cur_y = x, y
        for m in move:
            coord_map[cur_y][cur_x] = 1
            cur_x, cur_y = cur_x+move_amount[m][0], cur_y+move_amount[m][1]
        coord_map[cur_y][cur_x] = 1
        # print_map(coord_map)



    # print(coord_map)
    cnt = 0
    for i in range(k-1):
        for j in range(k-1):
            if coord_map[i][j]==1 and coord_map[i+1][j]==1 and coord_map[i][j+1]==1 and coord_map[i+1][j+1]==1:
                cnt+=1

    print(cnt)

    # print()