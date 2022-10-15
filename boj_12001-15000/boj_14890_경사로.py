import sys


def is_road(row):
    visited = [0]*N # 0 : 경사로가 없다는 의미, 1: 경사로가 이미 존재한다.
    # print(row)
    for i in range(N-1):
        if row[i]==row[i+1]+1: #경사로를 넣을 수 있는 높이 차이
            put_slope = True
            for j in range(L):
                if i+j+1>=N or row[i+1+j] != row[i]-1:
                    put_slope = False
                    break
            if put_slope :
                for j in range(L):
                    visited[i+j+1] = 1
            else :
                return False

        elif row[i]==row[i+1]-1 : #앞 칸이 현재 칸보다 한칸 더 높을 경우
            put_slope = True
            for j in range(L):
                # print(i-j, visited[i-j])
                if i-j<0 or row[i-j]+1 != row[i+1] or visited[i-j]==1:
                    put_slope=False
                    break
            if put_slope:
                for j in range(L):
                    visited[i-j] = 1
            else :
                return False

        elif row[i]==row[i+1] : # 높이가 같을 경우
            continue

        else : # 높이가 2칸 이상 차이 날 경우
            return False

    return True



if __name__=="__main__":
    sys.stdin = open("../input.txt", "r")

    N, L = map(int, sys.stdin.readline().split())
    road_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        if is_road(road_map[i]):cnt+=1

        column_road = [road_map[j][i] for j in range(N)]
        if is_road(column_road):cnt+=1

    # print(is_road(road_map[5]))
    print(cnt)