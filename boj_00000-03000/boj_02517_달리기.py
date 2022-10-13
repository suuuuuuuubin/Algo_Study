# 백준 2517 달리기
# https://www.acmicpc.net/problem/2517

import sys

def find_position(player_ls, player):

    cur_score = len(player_ls)

    left, right = 0, len(player_ls)-1
    while left<=right:
        mid = (left+right)//2
        if player_ls[mid]>player:
            left=mid+1
        else:
            right=mid-1

    if right<0:
        best_score=0
    else:
        best_score = (left+right)//2+1
    player_ls.insert(best_score, player)
    return player_ls, min(cur_score+1, best_score+1)




if __name__=="__main__":
    # sys.stdin = open('../input.txt','r')
    N = int(sys.stdin.readline())

    players_ls = []
    for idx in range(1,N+1):
        player = int(sys.stdin.readline())
        players_ls, score = find_position(players_ls, player)
        print(score)
