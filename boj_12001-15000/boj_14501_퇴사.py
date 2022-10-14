import sys

def dfs(i, n, consulting):
    max_result = 0
    if max_consult_day[i]!=-1:
        return max_consult_day[i]
    elif consulting[i][0]+i > n:
        max_consult_day[i] = 0
        return 0
    else:
        consult_p = consulting[i][1]
        j = i+consulting[i][0]
        max_val = 0
        for idx in range(j, n):
            val = dfs(idx, n, consulting)
            if val>max_val : max_val = val

        max_consult_day[i] = max_val + consult_p
        return max_val + consult_p


if __name__ == "__main__":
    # sys.stdin = open('../input.txt','r')
    n = int(sys.stdin.readline())

    consulting = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    max_consult_day = [-1 for _ in range(n)]

    for i in range(n):
        dfs(i, n, consulting)

    print(max(max_consult_day))
