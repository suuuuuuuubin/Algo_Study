# 백준 2003 수들의 합 2
# https://www.acmicpc.net/problem/2003

import sys

if __name__=="__main__":
    #sys.stdin = open('../input.txt','r')
    N, M = map(int,sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    cnt, i, j, sum, flag =0, 0, 0, 0, 2
    while i<N and j<N:
        if flag==1:
            sum-=nums[i-1]
        else:
            sum+=nums[j]

        flag=1
        if sum<M:
            j+=1
            flag = 2
        elif sum==M:
            i+=1
            cnt+=1
        else:
            i+=1

    print(cnt)
