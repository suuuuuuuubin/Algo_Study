# 백준 3055 탈출
# https://www.acmicpc.net/problem/3055

import sys
import copy
from collections import deque

def water_flow(water_map, r, c):
    direc = [(-1,0),(1,0),(0,-1),(0,1)]
    new_water_map = copy.deepcopy(water_map)
    for i in range(r):
        for j in range(c):
            if water_map[i][j]=="*":
                for d in direc:
                    move_r, move_c = i+d[0], j+d[1]
                    if move_r<0 or move_r>=r or move_c<0 or move_c>=c or water_map[move_r][move_c]!='.':
                        continue
                    else:
                        new_water_map[move_r][move_c]='*'
    return new_water_map

def print_map(water_map):
    for line in water_map:
        print(' '.join(line))

if __name__=='__main__':
    sys.stdin = open('../input.txt', 'r')
    R, C = map(int, sys.stdin.readline().split())

    # 문제 조건 - 고슴도치 위치 : S, 비버의 굴 위치 : D
    # 고슴도치는 인접한 네칸 중 하나로 이동
    # 물(*)은 매 분마다 비어있는 칸으로 확장

    # water map init
    water_map = []
    for _ in range(R):
        water_map.append(list(sys.stdin.readline().strip()))
    kak_coord=None
    for i in range(R):
        for j in range(C):
            if (water_map[i][j]=='S'):
                kak_coord = (i,j)
                water_map[i][j]='.'
                break
        if kak_coord:
            break


    # find min time to visit D using bfs -> 최소 시간을 찾는 문제이기 때문에 bfs 활용
    move_queue = deque([(kak_coord,0)])
    min_time = None
    direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    time = -1
    visited = [[0]*C for _ in range(R)]
    visited[kak_coord[0]][kak_coord[1]] = 1
    while move_queue and not min_time:
        cur_coord, cur_time = move_queue.popleft()
        if (cur_time != time): # 시간대가 변했을 때만 물을 이동
            water_map = water_flow(water_map, R, C)
            time = cur_time
        for d in direc :
            move_r, move_c = cur_coord[0] + d[0], cur_coord[1] + d[1]
            if move_r < 0 or move_r >= R or move_c < 0 or move_c >= C or water_map[move_r][move_c] == '*' or water_map[move_r][move_c] == 'X' or visited[move_r][move_c]:
                continue
            elif water_map[move_r][move_c]=='D':
                min_time = cur_time+1
                break
            else :
                move_queue.append(((move_r, move_c), cur_time+1))
                visited[move_r][move_c] = 1

    if min_time:
        print(min_time)
    else:
        print("KAKTUS")

