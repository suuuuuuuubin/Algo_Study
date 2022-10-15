import sys

def spring(search_land_ls, land_map, tree_map):
    # print("search", search_land_ls)
    for i, j in search_land_ls :
        for tree in tree_map[i][j]:
            if land_map[i][j]<tree[0]:
                tree[1] = 0
            else:
                land_map[i][j] -= tree[0]
                tree[0] += 1

    # print_land(land_map)
    return search_land_ls, land_map, tree_map

def summer(search_land_ls, land_map, tree_map):
    # print("search", search_land_ls)
    del_ls = []
    for i,j in search_land_ls :
        tree_map[i][j].sort(reverse=True)
        while len(tree_map[i][j])!=0:
            tree = tree_map[i][j][0]
            if tree[1]==0:
                land_map[i][j] += (tree[0]//2)
                del tree_map[i][j][0]
            else:
                break
        if not tree_map[i][j] :
            del_ls.append([i,j])

        tree_map[i][j].sort()

    for del_land in del_ls:
        search_land_ls.remove(del_land)
    return search_land_ls, land_map, tree_map
    # print_land(land_map)

def autumn(search_land_ls, land_map, tree_map):
    # print("search", search_land_ls)
    new_tree_map = [[[] for _ in range(N)] for _ in range(N)]
    for i, j in search_land_ls:
        for tree in tree_map[i][j]:
            new_tree_map[i][j].append(tree[:])

    # print("new", new_tree_map)
    move = [] # 나무 심을 8개 방향
    for i in [0, -1, 1]:
        for j in [0, -1, 1]:
            move.append([i, j])
    del move[0]

    add_ls = []
    for i, j in search_land_ls :
        for tree in tree_map[i][j]:
            if tree[0] % 5 == 0:
                for m in move:
                    next_i, next_j = i+m[0], j+m[1]
                    if next_i>=0 and next_i<N and next_j>=0 and next_j<N:
                        new_tree_map[next_i][next_j].append([1, 1])
                        if [next_i, next_j] not in add_ls and [next_i, next_j] not in search_land_ls:
                            add_ls.append([next_i, next_j])
        new_tree_map[i][j].sort()

    for add_land in add_ls:
        search_land_ls.append(add_land)

    return search_land_ls, land_map, new_tree_map

def winter(land_map, food_map):
    for i in range(N):
        for j in range(N):
            land_map[i][j] += food_map[i][j]

    # print_land(land_map)
    return land_map


def print_land (land_map):
    for line in land_map:
        print(line)
if __name__=="__main__":
    sys.stdin = open("../input.txt", "r")
    N, M, K = map(int, sys.stdin.readline().split())
    land_map = [[5]*N for _ in range(N)]
    food_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    trees = [list(map(int, sys.stdin.readline().split())) for _ in range(M)] # tree x. y, age
    tree_map = [[[] for _ in range(N)] for _ in range(N)]

    search_land_ls = []
    for tree in trees:
        x, y, age = tree
        tree_map[y-1][x-1].append([age, 1]) # 나이와 나무가 살아 있는지 여부
        if [y-1, x-1] not in search_land_ls:
            search_land_ls.append([y-1, x-1])
    for i,j in search_land_ls:
        tree_map[i][j].sort()

    for _ in range(K):
        # print("start", search_land_ls)
        # print_land(tree_map)
        search_land_ls, land_map, tree_map = spring(search_land_ls, land_map, tree_map)

        # print("spring")
        # print_land(tree_map)
        search_land_ls, land_map, tree_map = summer(search_land_ls, land_map, tree_map)
        # print("summer")
        # print_land(tree_map)

        search_land_ls, land_map, tree_map = autumn(search_land_ls, land_map, tree_map)
        # print("autumn")
        # print_land(tree_map)
        land_map = winter(land_map, food_map)


    cnt = 0
    # print("last")
    # print_land(tree_map)
    for i, j in search_land_ls:
        cnt += len(tree_map[i][j])

    print(cnt)