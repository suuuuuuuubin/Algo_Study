# 백준 1065 한수
# https://www.acmicpc.net/problem/1065

import sys

def HAN(num):
    num_str = list(map(int,list(str(num))))
    if len(num_str)==1 or len(num_str)==2:
        return True
    else:
        gap = num_str[1]-num_str[0]
        for idx in range(len(num_str)-1):
            if (num_str[idx+1]-num_str[idx])!=gap:
                return False
        return True


if __name__=="__main__":
    N = int(sys.stdin.readline())
    cnt = 0
    for num in range(1,N+1):
        if (HAN(num)):
            cnt+=1
    print(cnt)
