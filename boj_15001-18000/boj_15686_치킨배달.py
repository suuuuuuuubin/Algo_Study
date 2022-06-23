# 백준 15686 치킨 배달
# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

def cal_nearset_dist(house_ls, chicken_ls):

    total = 0
    for house in house_ls:
        nearest_dist = float('inf')
        for chicken in chicken_ls:
            dist = abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])
            if dist < nearest_dist:
                nearest_dist = dist
        total+=nearest_dist

    return total

if __name__=="__main__":
    # sys.stdin = open('../input.txt','r')
    N, M = map(int,sys.stdin.readline().split())
    house_ls,chicken_ls =[], []
    for i in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            if line[j] == 1:
                house_ls.append((i,j))
            elif line[j] == 2:
                chicken_ls.append((i,j))

    min_dist = float('inf')
    for i in range(1, M+1):
        chicken_combis = list(combinations(chicken_ls, i))
        for chicken_combi in chicken_combis:
            dist = cal_nearset_dist(house_ls, chicken_combi)
            min_dist = min(dist, min_dist)

    print(min_dist)
