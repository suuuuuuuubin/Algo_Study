# 백준 1103 게임
# https://www.acmicpc.net/problem/1103

import sys
sys.setrecursionlimit(100000) #recursion error 때문에 추가

def dfs(game_map, visited, cur, n, m, dp_map):
    direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    move_num = int(game_map[cur[0]][cur[1]])
    max_time = 0

    if dp_map[cur[0]][cur[1]] != 0:
        return dp_map[cur[0]][cur[1]]

    for d in direc:
        move_x, move_y = cur[0]+d[0]*move_num, cur[1]+d[1]*move_num
        if move_x<0 or move_x>=n or move_y<0 or move_y>=m or game_map[move_x][move_y]=='H':
            continue
        elif visited[move_x][move_y] :
            return -1
        else:
            visited[move_x][move_y] = 1
            time = dfs(game_map, visited, (move_x, move_y), n, m, dp_map)
            if time == -1:
                return -1
            else:
                max_time = max(max_time, time)
            visited[move_x][move_y] = 0

        dp_map[cur[0]][cur[1]]=max_time+1 #런타임 줄이려고 dp 추가

    return max_time+1

if __name__=="__main__":
    # sys.stdin = open('../input.txt', 'r')

    # init game map
    N, M = map(int, sys.stdin.readline().split())
    game_map = [list(sys.stdin.readline().strip()) for _ in range(N) ]
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    dp_map = [[0] * M for _ in range(N)]

    # dfs로 접근
    print(dfs(game_map, visited, (0,0), N, M, dp_map))

