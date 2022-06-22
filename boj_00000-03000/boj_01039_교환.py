# 백준 1039 교환
# https://www.acmicpc.net/problem/1039

import sys

def find_possi(num):
    possi_ls = []
    for i in range(len(str(num))-1):
        for j in range(i+1,len(str(num))):
            num_str = list(str(num))
            temp = num_str[i]
            num_str[i] = num_str[j]
            num_str[j] = temp
            if num_str[0]=='0':
                continue
            else :
                possi_ls.append(int(''.join(num_str)))
    return list(set(possi_ls))

if __name__=="__main__":
    # sys.stdin = open('../input.txt')
    N, K = map(int, sys.stdin.readline().split())

    possi_dict = {}
    exchg_objs = [N]
    for _ in range(K):
        possi_ls = find_possi(N)
        new_exchg_objs = []
        for exchg_obj in exchg_objs:
            if exchg_obj in possi_dict.keys():
                new_exchg_objs.extend(possi_dict[exchg_obj])
            else:
                found = find_possi(exchg_obj)
                new_exchg_objs.extend(found)
                possi_dict[exchg_obj] = found

        exchg_objs = list(set(new_exchg_objs))

    if not exchg_objs:
        print(-1)
    else:
        print(max(exchg_objs))

