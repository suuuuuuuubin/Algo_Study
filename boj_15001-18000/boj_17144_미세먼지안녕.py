import sys

def diffuse(room_map):
    # new_room_map = room_map[:][:]
    new_room_map = [line[:] for line in room_map]
    # new_room_map = [room_map[i][:] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if room_map[i][j] > 0:
                diffuse_amount = room_map[i][j]//5
                for move in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                    new_i, new_j = i+move[0], j+move[1]
                    if new_i>-1 and new_i<R and new_j>-1 and new_j<C and room_map[new_i][new_j]!= -1:
                        new_room_map[new_i][new_j] += diffuse_amount
                        new_room_map[i][j] -= diffuse_amount
    # print_room(room_map)
    # print_room(new_room_map)
    room_map = new_room_map
    return new_room_map

def wind(purifier, room_map):
    new_room_map = [line[:] for line in room_map]

    # print("in")
    # print_room(new_room_map)

    top_puri, down_puri = purifier[0], purifier[1]

    move_direc = [(0,1), (-1,0), (0,-1), (1,0)] #반시계 기준 이동 방향 : right->up->left->down
    cur_x, cur_y = top_puri[0], top_puri[1]
    cur_direc = 0
    while True:
        val = room_map[cur_x][cur_y]
        new_x, new_y = cur_x+move_direc[cur_direc][0],cur_y+move_direc[cur_direc][1]
        # print(new_x, new_y)
        if new_x<0 or new_x>=R or new_y<0 or new_y>=C:
            cur_direc = (cur_direc+1)%4
        else:
            if room_map[new_x][new_y] == -1:
                break
            else:
                if val<=0:
                    new_room_map[new_x][new_y] = 0
                else:
                    new_room_map[new_x][new_y] = val
                cur_x, cur_y =new_x, new_y
                # print_room(new_room_map)
                # print_room(room_map)


    cur_x, cur_y = down_puri[0], down_puri[1]
    cur_direc = 0
    while True:
        val = room_map[cur_x][cur_y]
        new_x, new_y = cur_x + move_direc[cur_direc][0], cur_y + move_direc[cur_direc][1]

        if new_x < 0 or new_x >= R or new_y < 0 or new_y >= C:
            cur_direc = (cur_direc - 1) % 4
        else:
            if room_map[new_x][new_y] == -1:
                break
            else:
                if val <= 0:
                    new_room_map[new_x][new_y] = 0
                else:
                    new_room_map[new_x][new_y] = val
                cur_x, cur_y = new_x, new_y
                # print_room(new_room_map)
                # print_room(room_map)

    return new_room_map

def cal_fine (room_map):
    cnt = 0
    for i in range(R):
        for j in range(C):
           if room_map[i][j] != -1:
               cnt+=room_map[i][j]

    return cnt

def print_room(room_map):
    for line in room_map:
        print(line)


if __name__ =="__main__":
    sys.stdin = open("../input.txt")

    R, C, T = map(int, sys.stdin.readline().split())
    room_map = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

    purifier = []
    for i in range(R):
        for j in range(C):
            if room_map[i][j] == -1:
                purifier.append([i,j])

    for _ in range(T):
        room_map = diffuse(room_map)
        room_map = wind(purifier, room_map)

    print(cal_fine(room_map))
