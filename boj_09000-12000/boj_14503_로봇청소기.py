import sys

def move_cleaner(x, y, direc, clean_map):
    # print("in", x, y, direc, clean_map)
    count = 1
    # clean cur coord
    clean_map[x][y] = 2 # if clean value is 2

    # direcs = [0, 1, 2, 3] # 왼쪽 방향 회전 : (direc-1)%4 / 북, 동, 남, 서
    move = [[0, -1], [-1, 0], [0, 1], [1, 0]] # 왼쪽 방향 이동 : 북쪽 -> x, y-1 / 동쪽 -> x-1, y / 남쪽 -> x, y+1 / 서쪽 -> x+1, y
    back_move = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    # 북쪽 기준 : left,

    # 1. 왼쪽 방향에 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한칸을 전진하고 1번부터 진행
    while True:
        left = [x+move[direc][0], y+move[direc][1]]
        if clean_map[left[0]][left[1]] == 0:
            direc = (direc-1)%4
            clean_map[left[0]][left[1]] = 2
            x, y, direc, count_add = move_cleaner(left[0], left[1], direc, clean_map)
            count += count_add
        else :
            back_wall = True if clean_map[x+back_move[direc][0]][y+back_move[direc][1]]==1 else False
            all_filled = True
            for m in move:
                if clean_map[x+m[0]][y+m[1]]==0:
                    all_filled = False
                    break
            # print(all_filled, back_wall)
            if all_filled and not back_wall:
                x += back_move[direc][0]
                y += back_move[direc][1]
                continue

            elif all_filled and back_wall:
                break

            else :
                direc = (direc-1)%4
                continue

    return x, y, direc, count


if __name__ == "__main__":
    # n, m = map(int, input().split())
    # r, c, d = map(int, input().split())
    # # direction - 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3: 서쪽
    #
    # clean_map = [list(map(int, input().split())) for _ in range(n)]
    # print(clean_map)

    # sys.stdin = open('../input.txt','r')
    n, m = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    # direction - 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3: 서쪽

    clean_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    print(move_cleaner(r, c, d, clean_map)[3])
