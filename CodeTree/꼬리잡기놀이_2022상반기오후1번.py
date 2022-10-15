import sys
def print_map(board):
    for line in board:
        print(line)
    print()
def move_people():
    for g_idx in range(len(people_group_start)):
        group_start = people_group_start[g_idx]
        group_end = people_group_end[g_idx]
        direc = direc_ls[g_idx]

        if direc==0:
            front_map = road_map_front
            back_map = road_map_back
        else:
            front_map = road_map_back
            back_map = road_map_front

        cur_r, cur_c = group_start
        while game_map[cur_r][cur_c] != 4:
            next_r, next_c = front_map[cur_r][cur_c]
            back_r, back_c = back_map[cur_r][cur_c]

            game_map[next_r][next_c] = game_map[cur_r][cur_c]
            game_map[cur_r][cur_c] = 4
            cur_r, cur_c = back_r, back_c

        people_group_start[g_idx] = front_map[group_start[0]][group_start[1]]
        people_group_end[g_idx] = front_map[group_end[0]][group_end[1]]

    return game_map, people_group_start, people_group_end

def shoot_ball(round):

    shoot_direcs = [(0,0,1), (N-1, -1,0), (N-1, 0, -1), (0, 1, 0)] #right, up, left, down
    shoot_direc = (round-1)//N
    shoot_rc = (round-1)%N

    score = 0
    # print(round, shoot_direc, shoot_rc)

    if shoot_direc == 0 : #right
        r = shoot_rc
        for c in range(0, N):
            if game_map[r][c] not in (0,4):
                team = (int)(game_map[r][c][1:])-1

                if direc_ls[team]==0:
                    front_map = road_map_front
                else:
                    front_map = road_map_back

                cnt = 1
                cur_x, cur_y = r, c
                while cur_x!=people_group_start[team][0] or cur_y!=people_group_start[team][1] :
                    cur_x, cur_y = front_map[cur_x][cur_y]
                    cnt+=1

                score = cnt**2
                direc_ls[team] = (direc_ls[team]+1)%2
                temp = people_group_start[team]
                people_group_start[team] = people_group_end[team]
                people_group_end[team] = temp

                break

    elif shoot_direc == 1: #up
        c = shoot_rc
        for r in range(N-1, -1, -1):
            if game_map[r][c] not in (0, 4):
                team = (int)(game_map[r][c][1:]) - 1

                if direc_ls[team] == 0:
                    front_map = road_map_front
                else:
                    front_map = road_map_back

                cnt = 1
                cur_x, cur_y = r, c
                while cur_x != people_group_start[team][0] or cur_y != people_group_start[team][1]:
                    cur_x, cur_y = front_map[cur_x][cur_y]
                    cnt += 1

                score = cnt ** 2
                direc_ls[team] = (direc_ls[team] + 1) % 2
                temp = people_group_start[team]
                people_group_start[team] = people_group_end[team]
                people_group_end[team] = temp

                break

    elif shoot_direc == 2: #left

        r = shoot_rc
        for c in range(N-1, -1, -1):
            if game_map[r][c] not in (0, 4):
                team = (int)(game_map[r][c][1:]) - 1

                if direc_ls[team] == 0:
                    front_map = road_map_front
                else:
                    front_map = road_map_back

                cnt = 1
                cur_x, cur_y = r, c
                while cur_x != people_group_start[team][0] or cur_y != people_group_start[team][1]:
                    cur_x, cur_y = front_map[cur_x][cur_y]
                    cnt += 1

                score = cnt ** 2
                direc_ls[team] = (direc_ls[team] + 1) % 2
                temp = people_group_start[team]
                people_group_start[team] = people_group_end[team]
                people_group_end[team] = temp

                break

    else :

        c = shoot_rc
        for r in range(0, N):
            if game_map[r][c] not in (0, 4):
                team = (int)(game_map[r][c][1:]) - 1

                if direc_ls[team] == 0:
                    front_map = road_map_front
                else:
                    front_map = road_map_back

                cnt = 1
                cur_x, cur_y = r, c
                while cur_x != people_group_start[team][0] or cur_y != people_group_start[team][1]:
                    cur_x, cur_y = front_map[cur_x][cur_y]
                    cnt += 1

                score = cnt ** 2
                direc_ls[team] = (direc_ls[team] + 1) % 2
                temp = people_group_start[team]
                people_group_start[team] = people_group_end[team]
                people_group_end[team] = temp

                break

    return score

if __name__ == "__main__":
    sys.stdin = open("../input.txt", 'r')
    N, M, K = map(int, sys.stdin.readline().split(" "))
    game_map = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    road_map_front = [[(0,0)]*N for _ in range(N)]
    road_map_back = [[(0,0)]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    move = [(1,0), (-1,0), (0,1), (0,-1)] #down, up, right, left
    people_group_start = []
    people_group_end = []
    direc_ls = []

    # Set Map
    for i in range(N):
        for j in range(N):
            if game_map[i][j] == 1:
                start = (i, j)
                end = ()
                r, c = i, j
                direc_ls.append(0)
                while True:
                    if game_map[r][c] in [1,2,3]:
                        game_map[r][c] = f"t{len(direc_ls)}"
                    # print(r, c)
                    find = False
                    for m in move:
                        next_r, next_c = r+m[0],  c+m[1]
                        if next_r>=0 and next_r<N and next_c>=0 and next_c<N:
                            if game_map[next_r][next_c]==4 and visited[next_r][next_c]==0:
                                road_map_front[r][c] = (next_r, next_c)
                                road_map_back[next_r][next_c] = (r, c)
                                r, c = next_r, next_c
                                visited[next_r][next_c] = 1

                                find = True
                                break
                    # 만약 4를 못찾았다면 - 2,3,1 이라도 찾아라
                    if not find:
                        for m in move:
                            next_r, next_c = r + m[0], c + m[1]
                            if next_r >= 0 and next_r < N and next_c >= 0 and next_c < N:
                                if game_map[next_r][next_c]!=0 and visited[next_r][next_c]==0:
                                    # print(i,j, "4못찾았을때", game_map[next_r][next_c], start, end)
                                    road_map_front[r][c] = (next_r, next_c)
                                    road_map_back[next_r][next_c] = (r, c)
                                    r, c = next_r, next_c
                                    visited[next_r][next_c] = 1
                                    if game_map[next_r][next_c]==3:
                                        end = (next_r, next_c)
                                    break
                    if r == i and c==j:
                        break
                people_group_start.append(start)
                people_group_end.append(end)







    # print_map(road_map_front)
    # print_map(road_map_back)
    #
    # print_map(game_map)

    # game_map, start, end = move_people(game_map, road_map_front, road_map_back, (0,0), 1)
    score = 0
    for round in range(1, K+1):

        # print_map(game_map)
        # print(people_group_start, people_group_end)
        game_map, people_group_start, people_group_end = move_people() #game_map, road_map_front, road_map_back, people_group_start, people_group_end, direc_ls
        # print(people_group_start, people_group_end)
        #
        score += shoot_ball(round)
        # print(score)
        # print(score)
        # print_map(game_map)
        # print(people_group_start, people_group_end)
    print(score)