# 백준 2580 스도쿠
# https://www.acmicpc.net/problem/2580

import sys

def find_possi(blank, puzzle_board):
    possi_list = [i for i in range(1,10)]
    # print_board(puzzle_board)
    # 가로 체크
    for j in puzzle_board[blank[0]]:
        if j in possi_list:
            possi_list.remove(j)

    # 세로 체크
    for i in range(9):
        if puzzle_board[i][blank[1]] in possi_list:
            possi_list.remove(puzzle_board[i][blank[1]])

    # 사각형 체크
    square_x, square_y = blank[0]//3, blank[1]//3
    for i in range(square_x*3, square_x*3+3):
        for j in range(square_y * 3, square_y * 3 + 3):
            if puzzle_board[i][j] in possi_list:
                possi_list.remove(puzzle_board[i][j])

    if possi_list:
        return possi_list
    else:
        return -1


def dfs(blank, puzzle_board, blank_ls):

    possi_ls = find_possi(blank, puzzle_board)

    if possi_ls==-1:
        return -1

    for possi in possi_ls:
        puzzle_board[blank[0]][blank[1]] = possi
        if len(blank_ls)!=1: #만약에 마지막 blank일 경우
            result = dfs(blank_ls[1], puzzle_board, blank_ls[1:])
            if result!=-1:
                return result
        else:
            return puzzle_board

    puzzle_board[blank[0]][blank[1]]=0

    return -1


def print_board(board):
    for line in board:
        line = list(map(str, line))
        print(' '.join(line))



if __name__=="__main__":
    # sys.stdin = open('../input.txt','r')
    puzzle_board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    blank_ls = []
    for i in range(9):
        for j in range(9):
            if puzzle_board[i][j] == 0:
                blank_ls.append((i,j))

    result = dfs(blank_ls[0], puzzle_board, blank_ls)
    print_board(result)