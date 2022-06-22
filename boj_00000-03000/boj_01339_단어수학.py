# 백준 1339 단어 수학
# https://www.acmicpc.net/problem/1339

import sys

if __name__=="__main__":
    sys.stdin = open('../input.txt','r')
    N = int(sys.stdin.readline())

    # word list init
    word_ls = []
    char_ls = []
    for _ in range(N):
        word_ls.append(list(sys.stdin.readline().strip()))
        char_ls.extend(word_ls[-1])
    char_ls = list(set(char_ls))

    # STEP1: 자릿수를 고려해서 한 문자가 차지하는 값을 구한다.
    # ex) ABBA의 경우 1001*A + 110*B이다.
    word_num = {char:0 for char in char_ls}
    for word in word_ls:
        for c_idx, char in enumerate(word):
            word_num[char]+=10**(len(word)-c_idx-1)

    # STEP2: 문자에 해당하는 값이 클수록 더 큰 수를 배당해준다.
    char_posi = sorted(word_num.items(), key = lambda x:x[1], reverse=True)

    # STEP3: 값을 계산한다.
    result = 0
    for i, char in enumerate(char_posi):
        result += (9-i)*char[1]
    print(result)