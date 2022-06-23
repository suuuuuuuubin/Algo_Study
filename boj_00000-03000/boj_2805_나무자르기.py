# 백준 2805 나무 자르기
# https://www.acmicpc.net/problem/2805

import sys
import math

if __name__=="__main__":
    sys.stdin = open('../input.txt','r')
    N, M = map(int, sys.stdin.readline().split())
    trees = list(map(int, sys.stdin.readline().split()))
    trees.sort(reverse=True)
    trees.append(0)
    tree_cut = [0]

    # 나무를 sorting한 후 큰 나무부터 그 나무 높이만큼 잘랐을 때 얻을 수 있는 총 나무의 길이를 계산한다.
    # 위의 값들을 M과 비교하면서 절단기 높이의 범위를 알아낸다. (ex) 세번째로 큰 나무 높이 ~ 두번째로 큰 나무 높이)
    tree_cut_idx = 0
    for t_idx in range(1, len(trees)):
        tree_cut_cal = tree_cut[-1]+(trees[t_idx-1]-trees[t_idx])*t_idx
        if (tree_cut[-1]-M)*(tree_cut_cal-M)<=0:
            tree_cut_idx=t_idx-1
            break
        tree_cut.append(tree_cut_cal)


    height = trees[tree_cut_idx]-math.ceil((M-tree_cut[-1])/(tree_cut_idx+1))
    print(height)