import sys

def spring(search_land_ls, land_map):
    # print("search", search_land_ls)
    for land in search_land_ls :
        i, j = land[0], land[1]
        if land_map[i][j][1]:
            for tree in land_map[i][j][1]:
                if land_map[i][j][0]<tree[0]:
                    tree[1] = 0
                else:
                    land_map[i][j][0] -= tree[0]
                    tree[0] += 1

    # print_land(land_map)
    return search_land_ls, land_map

def summer(search_land_ls, land_map):
    # print("search", search_land_ls)
    del_ls = []
    for land in search_land_ls :
        i, j = land[0], land[1]
        if land_map[i][j][1]:
            land_map[i][j][1].sort(reverse=True)
            while land_map[i][j][1]:
                tree = land_map[i][j][1][0]
                if tree[1]==0:
                    land_map[i][j][0] += (tree[0]//2)
                    del land_map[i][j][1][0]
                else:
                    break
            if not land_map[i][j][1] :
                del_ls.append(land)
            land_map[i][j][1].sort()

    for del_land in del_ls:
        search_land_ls.remove(del_land)
    return search_land_ls, land_map
    # print_land(land_map)

def autumn(search_land_ls, land_map):
    # print("search", search_land_ls)
    new_land_map = []
    for i in range(N):
        new_land_map.append([])
        for j in range(N):
            land = []
            land.append(land_map[i][j][0])
            land.append([])
            for tree in land_map[i][j][1]:
                land[1].append(tree[:])
            new_land_map[i].append(land)
    # print("new")
    # print_land(new_land_map)
    move = [] # 나무 심을 8개 방향
    for i in [0, -1, 1]:
        for j in [0, -1, 1]:
            move.append([i, j])
    del move[0]
    add_ls = []
    for land in search_land_ls :
        i, j = land[0], land[1]
        if land_map[i][j][1]:
            for tree in land_map[i][j][1]:
                if tree[0] % 5 == 0:
                    for m in move:
                        next_i, next_j = i+m[0], j+m[1]
                        if next_i>=0 and next_i<N and next_j>=0 and next_j<N:
                            new_land_map[next_i][next_j][1].append([1, 1])
                            if [next_i, next_j] not in add_ls and [next_i, next_j] not in search_land_ls:
                                add_ls.append([next_i, next_j])
            land_map[i][j][1].sort()

    for add_land in add_ls:
        search_land_ls.append(add_land)
    land_map = new_land_map
    return search_land_ls, new_land_map

def winter(land_map, food_map):
    for i in range(N):
        for j in range(N):
            land_map[i][j][0] += food_map[i][j]

    # print_land(land_map)
    return land_map


def print_land (land_map):
    for line in land_map:
        print(line)
if __name__=="__main__":
    sys.stdin = open("../input.txt", "r")
    N, M, K = map(int, sys.stdin.readline().split())
    land_map = [[[5, []] for _ in range(N)] for _ in range(N)]
    food_map = [[val for val in list(map(int, sys.stdin.readline().split()))] for _ in range(N)]

    trees = [list(map(int, sys.stdin.readline().split())) for _ in range(M)] # tree x. y, age
    search_land_ls = []
    for tree in trees:
        x, y, age = tree
        land_map[y-1][x-1][1].append([age, 1]) # 나이와 나무가 살아 있는지 여부
        land_map[y-1][x-1][1].sort()
        if [y-1, x-1] not in search_land_ls:
            search_land_ls.append([y-1, x-1])

    for _ in range(K):
        # print("start", search_land_ls)
        # print_land(land_map)
        search_land_ls, land_map = spring(search_land_ls, land_map)
        search_land_ls, land_map = summer(search_land_ls, land_map)
        search_land_ls, land_map = autumn(search_land_ls, land_map)
        land_map = winter(land_map, food_map)


    cnt = 0
    # print_land(land_map)
    for i, j in search_land_ls:
        cnt += len(land_map[i][j][1])

    print(cnt)