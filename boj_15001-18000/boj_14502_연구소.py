import sys

def combination(cur, num, beginwith, coord_list):
    total_ls = []
    if len(cur) == num:
        total_ls = [coord for coord in cur]
        return [total_ls]

    else :
        for i in range(beginwith, len(coord_list)):
            cur.append(coord_list[i])
            total_ls.extend(combination(cur, num, i+1, coord_list))
            del cur[-1]

    return total_ls


def get_safe_place(lab_map, wall_add, virus_list, safe_num):

    safe = safe_num-3 # remove added wall count
    lab_map_copy = [lab_map[i][:] for i in range(n)]

    for w in wall_add :
        lab_map_copy[w[0]][w[1]] = 1

    while True:
        # print(safe, lab_map_copy)
        del_safe = 0
        # print(virus_list)
        new_virus_list= virus_list[:]
        for v in virus_list:

            #left
            if v[1]-1>=0 and lab_map_copy[v[0]][v[1]-1]==0:
                # print(v, "left")
                lab_map_copy[v[0]][v[1]-1] = 2
                new_virus_list.append((v[0], v[1]-1))
                del_safe +=1
            # right
            if v[1] + 1 < m and lab_map_copy[v[0]][v[1] + 1] == 0:
                # print(v, "right")
                lab_map_copy[v[0]][v[1] + 1] = 2
                new_virus_list.append((v[0], v[1] + 1))
                del_safe += 1
            # down
            if v[0] + 1 < n and lab_map_copy[v[0]+1][v[1]] == 0:
                # print(v, "down")
                lab_map_copy[v[0] + 1][v[1]] = 2
                new_virus_list.append((v[0] + 1, v[1]))
                del_safe += 1
            # up
            if v[0] - 1  >= 0 and lab_map_copy[v[0]-1][v[1]] == 0:
                # print(v,"up")
                lab_map_copy[v[0]-1][v[1]] = 2
                new_virus_list.append((v[0]-1, v[1]))
                del_safe += 1

        if del_safe > 0 :
            safe -= del_safe
            virus_list=new_virus_list
        else:
            break

    return safe


if __name__=="__main__":
    # sys.stdin = open('../input.txt','r')
    n, m = map(int, sys.stdin.readline().split())
    lab_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # n, m = map(int, input().split())
    # lab_map = [list(map(int, input().split())) for _ in range(n)]
    coord_list = []
    virus_list = []
    safe_num = 0
    for i in range(n):
        for j in range(m):
            if lab_map[i][j] == 0 :
                safe_num+=1
                coord_list.append((i,j))
            elif lab_map[i][j] == 2 :
                virus_list.append((i,j))

    wall_combi_list = combination([], 3, 0, coord_list)
    # print(len(combination([], 3, 0, coord_list)))
    # print(wall_combi_list)
    max_safe = 0
    max_wall = []
    # print("before", lab_map)
    # print(get_safe_place(lab_map, [(0, 0), (1, 3), (3, 3)], virus_list, len(coord_list)))
    # print("after", lab_map)
    for wall_add in wall_combi_list:
        safe_num = get_safe_place(lab_map, wall_add, virus_list, len(coord_list))
        if safe_num>max_safe:
            max_safe = safe_num
            max_wall = wall_add

    # print(max_safe, max_wall)
    print(max_safe)