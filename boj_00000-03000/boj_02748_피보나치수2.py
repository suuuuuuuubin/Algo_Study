# 백준 2748 피보나치 수2
# https://www.acmicpc.net/problem/2748

import sys

if __name__=="__main__":
    sys.stdin = open('../input.txt','r')
    N = int(sys.stdin.readline())

    f1 = 0
    f2 = 1
    for _ in range(N-1):
        temp = f1+f2
        f1 = f2
        f2 = temp

    print(f2)