import sys
def rotate_flip_tet(tet, case=2):
    # 유형 1 : 네모형 -> 회전, 대칭 필요 없음
    if case == 0 :
        return [tet]
    # 유형 2 : 1자형 -> 한번만 회전하면 됨
    elif case == 1:
        return [tet, rotate[tet]]
    # 유형 3 : flip도 해야하고 rotate도 해야함.
    else :
        flip_tet = flip(tet)
        return_ls = []
        for i in range(4):
            tet = rotate(tet)
            flip_tet = rotate(flip_tet)
            return_ls.append(tet)
            return_ls.append(flip_tet)
        return return_ls

def rotate(tet):
    n, m = len(tet), len(tet[0])
    new_tet = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_i = j
            new_j = (n-1) - i
            new_tet[new_i][new_j] = tet[i][j]

    return new_tet

def flip(tet):
    n, m = len(tet), len(tet[0])
    new_tet = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):

            new_i = i
            new_j = m-1 - j
            new_tet[new_i][new_j] = tet[i][j]

    return new_tet

if __name__=="__main__":
    # sys.stdin = open('../input.txt','r')
    n, m = map(int, sys.stdin.readline().split())
    num_map = [list(map(int,  sys.stdin.readline().split())) for _ in range(n)]

    # n, m = map(int, input().split())
    # num_map = [list(map(int, input().split())) for _ in range(n)]
    tetromino = [[[1,1,1,1]],
                 [[1,1],[1,1]],
                 [[0,0,1], [1,1,1]],
                 [[0,1,1], [1,1,0]],
                 [[1,1,1], [0,1,0]]]
    max_val = 0
    for tet in tetromino:
        avail_tet = rotate_flip_tet(tet)
        for avail in avail_tet:
            # print(avail)
            h, w = len(avail), len(avail[0])
            for i in range(n-h+1):
                for j in range(m-w+1):
                    val = 0
                    for x in range(h):
                        for y in range(w):
                            val += avail[x][y]*num_map[x+i][y+j]

                    if val>max_val:
                        max_val = val


    print(max_val)
