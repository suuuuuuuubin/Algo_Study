import sys

def move_people():
    visited = [[0]*N for _ in range(N)]

    combine = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                total_people = 0
                total_nation = 0
                total_nation_coord = []
                queue = [[i,j]]
                while queue:
                    cur = queue[0]
                    total_nation_coord.append(cur)
                    del queue[0]
                    total_nation += 1
                    total_people += nations[cur[0]][cur[1]]

                    visited[i][j] = 1
                    for move in [(-1,0), (1,0), (0,-1), (0,1)]:
                        next_x, next_y = cur[0]+move[0], cur[1]+move[1]

                        if next_x>=0 and next_x<N and next_y>=0 and next_y<N and visited[next_x][next_y]==0:
                            gap = abs(nations[cur[0]][cur[1]] - nations[next_x][next_y])
                            if gap >= L and gap<=R:
                                combine = True
                                visited[next_x][next_y] = 1
                                queue.append([next_x, next_y])

                average_people = (int)(total_people/total_nation)
                for c in total_nation_coord:
                    nations[c[0]][c[1]] = average_people


    return combine

if __name__ == "__main__":
    sys.stdin = open("../input.txt", 'r')

    N, L, R = map(int, sys.stdin.readline().split())
    nations = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    last = 0
    cnt = 0
    while True:
        combine_result = move_people()
        if combine_result : cnt+=1
        else: break
        # cnt += 1
        # if last !=
    # move_people()
    # print(nations)

    print(cnt)