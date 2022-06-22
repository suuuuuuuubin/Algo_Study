# 백준 0000 문제 이름
# https://www.acmicpc.net/problem/0000

import sys
import copy

# def remove_position(chess_board, cur, N):
#
#     new_chess_board = copy.deepcopy(chess_board)
#     #가로, 세로 제거
#     for i in range(N):
#         new_chess_board[cur[0]][i] = 1
#         new_chess_board[i][cur[1]] = 1
#
#     #대각선 - 좌상단 제거
#     coord = [cur[0], cur[1]]
#     while coord[0]>=0 and coord[1]>=0:
#         new_chess_board[coord[0]][coord[1]] = 1
#         coord[0], coord[1] = coord[0]-1, coord[1]-1
#     #대각선 - 우상단 제거
#     coord = [cur[0], cur[1]]
#     while coord[0] >= 0 and coord[1] < N:
#         new_chess_board[coord[0]][coord[1]] = 1
#         coord[0], coord[1] = coord[0] - 1, coord[1] + 1
#     #대각선 - 좌하단 제거
#     coord = [cur[0], cur[1]]
#     while coord[0] < N and coord[1] >= 0:
#         new_chess_board[coord[0]][coord[1]] = 1
#         coord[0], coord[1] = coord[0] + 1, coord[1] - 1
#     #대각선 - 우하단 제거
#     coord = [cur[0], cur[1]]
#     while coord[0] < N and coord[1] < N:
#         new_chess_board[coord[0]][coord[1]] = 1
#         coord[0], coord[1] = coord[0] + 1, coord[1] + 1
#
#
#     return new_chess_board


def remove_position(chess_board, cur, N):
    new_chess_board = copy.deepcopy(chess_board)
    # 가로, 세로 제거
    new_chess_board[cur[0]] = []
    for i in range(N):
        cnt = new_chess_board[i].count(cur[1])
        if cnt!=0:
            new_chess_board[i].remove(cur[1])

    # print("가로, 세로 제거")
    # print_board(new_chess_board)

    # 대각선 - 좌상단 제거
    coord = [cur[0], cur[1]]
    while coord[0] >= 0 and coord[1] >= 0:
        cnt = new_chess_board[coord[0]].count(coord[1])
        if cnt != 0:
            new_chess_board[coord[0]].remove(coord[1])
        coord[0], coord[1] = coord[0] - 1, coord[1] - 1

    # print("좌상단 제거")
    # print_board(new_chess_board)

    # 대각선 - 우상단 제거
    coord = [cur[0], cur[1]]
    while coord[0] >= 0 and coord[1] < N:
        cnt = new_chess_board[coord[0]].count(coord[1])
        if cnt != 0:
            new_chess_board[coord[0]].remove(coord[1])
        coord[0], coord[1] = coord[0] - 1, coord[1] + 1

    # print("우상단 제거")
    # print_board(new_chess_board)

    # 대각선 - 좌하단 제거
    coord = [cur[0], cur[1]]
    while coord[0] < N and coord[1] >= 0:
        cnt = new_chess_board[coord[0]].count(coord[1])
        if cnt != 0:
            new_chess_board[coord[0]].remove(coord[1])
        coord[0], coord[1] = coord[0] + 1, coord[1] - 1

    # print("좌하단 제거")
    # print_board(new_chess_board)

    # 대각선 - 우하단 제거
    coord = [cur[0], cur[1]]
    while coord[0] < N and coord[1] < N:
        cnt = new_chess_board[coord[0]].count(coord[1])
        if cnt != 0:
            new_chess_board[coord[0]].remove(coord[1])
        coord[0], coord[1] = coord[0] + 1, coord[1] + 1
    
    # print("우하단 제거")
    # print_board(new_chess_board)

    return new_chess_board


# def print_board(board):
#     for line in board:
#         line = list(map(str, line))
#         print(' '.join(line))

def print_board(board):
    N = len(board.keys())
    board_img = [[1]*N for _ in range(N)]
    for x in board.keys():
        for y in board[x]:
            board_img[x][y] = 0
    for line in board_img:
        line = list(map(str, line))
        print(' '.join(line))



# def dfs(chess_board, x, N):
#     cnt = 0
#     for y in range(N):
#         if chess_board[x][y] == 0 :
#             new_chess_board = remove_position(chess_board, (x,y), N)
#             if x==(N-1):
#                 cnt += 1
#             else:
#                 cnt += dfs(new_chess_board, x+1, N)
#     return cnt


def dfs(chess_board, x, N):
    cnt = 0
    for y in chess_board[x]:
        if x==(N-1):
            cnt += 1
        else:
            new_chess_board = remove_position(chess_board, (x, y), N)
            cnt += dfs(new_chess_board, x+1, N)

    return cnt



if __name__=="__main__":
    sys.stdin = open('../input.txt','r')
    N = int(sys.stdin.readline())

    # chess_board = [[0]*N for _ in range(N)]

    chess_board = {idx:[j for j in range(N)] for idx in range(N)}

    print(dfs(chess_board, 0, N))



