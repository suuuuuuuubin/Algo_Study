from collections import deque
import sys


def get_team(drawing):
    team = [[-1] * N for _ in range(N)]
    team_block_count = []
    team_block_value = []

    team_num = -1
    for r in range(N):
        for c in range(N):
            if team[r][c] == -1:
                team_num += 1
                team[r][c] = team_num
                draw_num = drawing[r][c]
                team_block_count.append(0)
                team_block_value.append(draw_num)

                queue = deque([[r, c]])
                while queue:
                    cur_r, cur_c = queue.popleft()
                    team_block_count[team_num] +=1
                    for move in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_r, next_c = cur_r + move[0], cur_c + move[1]
                        if next_r >= 0 and next_r < N and next_c >= 0 and next_c < N and drawing[next_r][next_c]==draw_num and team[next_r][next_c] == -1:
                            team[next_r][next_c] = team_num
                            queue.append([next_r, next_c])
    # print(team)
    return team_num+1, team,  team_block_count, team_block_value

def get_score(team, total_team, team_block_count, team_block_value):
    team_adj = [[0]*total_team for _ in range(total_team)]

    for r in range(N):
        for c in range(N):
            cur_team = team[r][c]
            for move in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_r, next_c = r + move[0], c + move[1]
                if next_r >= 0 and next_r < N and next_c >= 0 and next_c < N :
                    next_team = team[next_r][next_c]
                    # print(cur_team, next_team)
                    team_adj[cur_team][next_team] += 1

    total_score =  0
    for i in range(total_team):
        for j in range(i+1, total_team):
            total_score += (team_block_count[i] + team_block_count[j]) * team_block_value[i] * team_block_value[j] * team_adj[i][j]

    # print("score", total_score)
    return total_score

def rotate_drawing(drawing):

    new_drawing = [[0]*N for _ in range(N)]
    mid = N//2

    # 십자 회전
    center_r, center_c = mid, mid
    for i in range(N):
        r, c = i, mid
        # 반시계 회전
        r1, c1 = -1*(c-center_c)+center_r, (r-center_r)+center_c
        new_drawing[r1][c1] = drawing[r][c]
        r, c = mid, i
        r2, c2 = -1*(c-center_c)+center_r, (r-center_r)+center_c
        new_drawing[r2][c2] = drawing[r][c]


    center_r, center_c = (N-mid)/2-1, (N-mid)/2-1
    # print(center_r, center_c)
    for i in range(mid):
        for j in range(mid):
            new_i, new_j = int((j-center_c)+center_r), int(-1*(i-center_r)+center_c)
            new_drawing[new_i][new_j] = drawing[i][j]

    center_r, center_c = (N - mid) / 2 + mid, (N - mid) / 2 + mid
    # print(center_r, center_c)
    for i in range(mid+1, N):
        for j in range(mid+1, N):
            new_i, new_j = int((j - center_c) + center_r), int(-1 * (i - center_r) + center_c)
            new_drawing[new_i][new_j] = drawing[i][j]

    center_r, center_c = (N - mid) / 2 + mid, (N-mid)/2-1
    for i in range(mid+1, N):
        for j in range(mid):
            new_i, new_j = int((j - center_c) + center_r), int(-1 * (i - center_r) + center_c)
            new_drawing[new_i][new_j] = drawing[i][j]

    center_r, center_c = (N-mid)/2-1, (N - mid) / 2 + mid
    for i in range(mid):
        for j in range(mid+1, N):
            new_i, new_j = int((j - center_c) + center_r), int(-1 * (i - center_r) + center_c)
            new_drawing[new_i][new_j] = drawing[i][j]

    # for center_r in range((N-mid))
    # for center_r, center_c in [()]
    # print(drawing)
    # print(new_drawing)

    # print(-1*(c-center_c)+center_r, (r-center_r)+center_c)
    # print((c-center_c)+center_r, -1*(r-center_r)+center_c)

    return new_drawing


if __name__ == "__main__":
    sys.stdin = open("../input.txt", "r")
    N = int(sys.stdin.readline())
    drawing = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    # N = (int)input()
    # drawing = [list(map(int, input().split(" "))) for _ in range(N)]

    total_score = 0
    for _ in range(4):
        total_team_num, team_map, team_block_count, team_block_value = get_team(drawing)
        total_score+=get_score(team_map, total_team_num, team_block_count, team_block_value)
        drawing = rotate_drawing(drawing)

    print(total_score)