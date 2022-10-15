import sys

def get_combi(N):
    # x, y 시작점, d1, d2
    combi_ls = []
    for x in range(N): # 열
        for y in range(N): # 행
            # print(x, y, min(N-x, y))
            for d1 in range(1,min(N-x-1, y)+1):
                for d2 in range(1, min(N-x-1, N-y-1)+1):
                    if x+d1+d2<N :
                        combi_ls.append([x, y, d1, d2])
    # print(combi_ls)
    return combi_ls

def get_gap(combi, city_people):





    # print(combi)
    total = [0]*5
    x, y, d1, d2 = combi
    city_map = [[0]*N for _ in range(N)]

    # 5구역 list 구하기
    ls_5 = []
    # print(combi)
    for i in range(d1+1):
        for j in range(d2+1):
            ls_5.append([x+i+j, y-i+j])
            city_map[x+i+j][y-i+j] = 1
    for i in range(d1):
        for j in range(d2):
            ls_5.append([x+i+j+1, y-i+j])
            city_map[x+i+j+1][y-i+j] = 1

    # print(ls_5)



    for r in range(N):
        for c in range(N):
            if city_map[r][c] == 1:
                total[4] += city_people[r][c]
            else :
                # 1구역
                if r<x+d1 and c<=y:
                    # print(r, c, "in 1")
                    total[0] += city_people[r][c]
                elif r<=x+d2 and c>y:
                    # print(r, c, "in 2")
                    total[1] += city_people[r][c]
                elif r>=x+d1 and c<y-d1+d2:
                    # print(r, c, "in 3")
                    total[2] += city_people[r][c]
                else:
                    # print(r, c, "in 4")
                    total[3] += city_people[r][c]

    # print(total)
    # print(max(total)-min(total))

    return max(total)-min(total)




if __name__=="__main__":
    sys.stdin = open("../input.txt", "r")

    N = (int)(sys.stdin.readline())
    city_people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    combi_ls = get_combi(N)

    min_gap = float("inf")
    # print(len(combi_ls))
    for combi in combi_ls:
        gap =get_gap(combi, city_people)
        if min_gap > gap:
            min_gap = gap

    print(min_gap)

