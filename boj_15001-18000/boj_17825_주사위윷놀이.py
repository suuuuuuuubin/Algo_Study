import sys
from collections import deque

def dfs(cur, dice_ls, cur_ls):
    max_result = 0
    # print(cur, cur_ls)
    if cur == len(dice_ls):
        return 0
    else:
        dice = dice_ls[cur]

        for horse in range(4):

            temp = cur_ls[horse]

            if temp == 21:
                continue

            if temp in (5, 10, 15): # take blue line
                move_end = game_map_blue[temp]
            else :
                move_end = game_map_red[temp][1]

            for i in range(dice-1):
                if move_end == 21:
                    break
                move_end = game_map_red[move_end][1]

            if move_end == 21:
                cur_ls[horse] = move_end
                max_result = max(max_result, dfs(cur + 1, dice_ls, cur_ls) + game_map_red[move_end][0])
                cur_ls[horse] = temp
            elif move_end not in cur_ls:
                cur_ls[horse] = move_end
                max_result = max(max_result, dfs(cur + 1, dice_ls, cur_ls) + game_map_red[move_end][0])
                cur_ls[horse] = temp

    return max_result



if __name__ =="__main__":
    sys.stdin = open("../input.txt", "r")
    dice_ls = list(map(int, sys.stdin.readline().split()))

    game_map_red = [(2*i, i+1) for i in range(21)] + [(0, 'end')] + [(13+3*i, 23+i) for i in range(3)] + [(22+2*i, 26+i) for i in range(2)] + [(28-i, 28+i) for i in range(4)] + [(30, 32), (35,21)]
    game_map_red[24] = (19, 30)
    game_map_red[26] = (24, 30)
    game_map_blue = {5: 22, 10: 25, 15:27}  #(red index from, red index to)
    # 0~20 / 21 - end / 22~24 - 중앙왼쪽 blueline / 25~26 - 중앙 하단 blueline / 27~30 - 중앙오른쪽 blueline -> 중앙 25 : 30index / 31~32 - 중앙위쪽
    # print(len(game_map_blue), len(game_map_red))

    print(dfs(0, dice_ls, [0,0,0,0]))
