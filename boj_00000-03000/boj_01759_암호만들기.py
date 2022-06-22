# 백준 1759 암호 만들기
# https://www.acmicpc.net/problem/1759

import sys
from itertools import combinations

if __name__=="__main__":
    sys.stdin = open('../input.txt','r')
    N, M = map(int, sys.stdin.readline().split())
    char_ls = sys.stdin.readline().split()

    vowel_ls, consonant_ls = [], []

    for char in char_ls:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel_ls.append(char)
        else:
            consonant_ls.append(char)

    passwords = []
    for i in range(N-2):
        v_combi = list(combinations(vowel_ls, i+1))
        c_combi = list(combinations(consonant_ls, N-i-1))
        for v in v_combi:
            for c in c_combi:
                passwords.append(''.join(sorted(list(v+c))))

    passwords.sort()
    print('\n'.join(passwords))
