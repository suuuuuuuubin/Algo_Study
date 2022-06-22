# 백준 1920 수 찾기
# https://www.acmicpc.net/problem/1920

import sys

if __name__=="__main__":
    # sys.stdin = open('../input.txt','r')
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    nums_ls = [[n, idx, 0] for idx, n in enumerate(nums)]

    A.sort()
    nums_ls.sort()
    a_idx, nums_idx = 0, 0

    while a_idx<N and nums_idx<M:
        # pointer가 가리키는 값이 같을 경우
        if A[a_idx]==nums_ls[nums_idx][0]:
            nums_ls[nums_idx][2] = 1
            nums_idx+=1
        elif A[a_idx]<nums_ls[nums_idx][0]:
            a_idx+=1
        else:
            nums_idx+=1

    nums_ls.sort(key=lambda x:x[1])
    for num in nums_ls:
        print(num[2])
