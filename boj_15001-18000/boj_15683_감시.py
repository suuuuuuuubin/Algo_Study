import sys

def combination(i, n, cur, cctv_ls):
    if i == n:
        total_combi.append(cur)
        return

    cctv_direc_dict = {
        # 0 : left, 1: right, 2: down, 3: up
        1: [[0], [1], [2], [3]],
        2: [[0,1], [2,3]],
        3: [[3, 1], [1, 2], [2, 0], [0, 3]],
        4: [[0, 1, 2], [0,1, 3], [0, 2, 3],  [1,2,3]],
        5 : [[0,1,2,3]]
    }

    for direc in cctv_direc_dict[cctv_ls[i][0]]:
        cctv_info = cctv_ls[i][:] + [direc]
        combination(i+1, n, cur+[cctv_info], cctv_ls)

    return


def cal_square(cctv_ls):
    new_map = [room[i][:] for i in range(n)]
    direction = [[0,-1],[0, 1],[1,0],[-1,0]] # 0:left, 1: right, 2: down, 3: up
    for cctv in cctv_ls :
        for direc in cctv[3]:
            cur_x, cur_y = cctv[1]+direction[direc][0], cctv[2]+direction[direc][1]

            while cur_x>-1 and cur_x<n and cur_y>-1 and cur_y<m and new_map[cur_x][cur_y] != 6 :
                # print(cur_x, cur_y)
                if new_map[cur_x][cur_y] == 0:
                    new_map[cur_x][cur_y] = '#'
                cur_x, cur_y = cur_x+direction[direc][0], cur_y+direction[direc][1]
                # print("out", cur_x, cur_y)
    # print(new_map)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_map[i][j] == 0:
                cnt += 1

    return cnt


if __name__ == "__main__":
    sys.stdin = open('../input.txt','r')

    n, m = map(int, sys.stdin.readline().split())
    room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    cctv_ls = []

    for i in range(n):
        for j in range(m):
            if room[i][j] > 0 and room[i][j] < 6:
                cctv_ls.append([room[i][j],i,j])
    total_combi = []
    combination(0, len(cctv_ls), [], cctv_ls)
    cal_square(total_combi[0])
    min_cnt = float("inf")
    for cctv in total_combi:
        cnt = cal_square(cctv)
        if cnt<min_cnt : min_cnt = cnt

    print(min_cnt)