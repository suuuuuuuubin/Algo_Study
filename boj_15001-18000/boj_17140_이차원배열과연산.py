import sys

def sort_arr(arr):
    # print("in sort")
    r_num, c_num = len(arr), len(arr[0])
    new_arr = []
    # R 연산


    if r_num<c_num:
        temp = [[0] * r_num for _ in range(c_num)]
        for i in range(r_num):
            for j in range(c_num):
                temp[j][i] = arr[i][j]
        arr = temp
        # print("switch", arr)

    max_len = 0
    every_line = []
    R, C = len(arr), len(arr[0])
    for i in range(R):
        line = arr[i][:]
        line_dict = {}
        for a in line:
            if a == 0:
                continue
            elif a not in line_dict.keys():
                line_dict[a] = 1
            else:
                line_dict[a] += 1
        ls = list(sorted(line_dict.items(), key=lambda x: (x[1], x[0])))
        if len(ls) > max_len: max_len = len(ls)
        every_line.append(ls)
    # print(every_line)
    for line in every_line:
        num = len(line)
        new_line = []
        for i in range(num):
            new_line.append(line[i][0])
            new_line.append(line[i][1])
        for j in range(num, max_len):
            new_line.append(0)
            new_line.append(0)
        new_arr.append(new_line)

    # print("new", new_arr)

    if r_num<c_num:
        temp = [[0] * len(new_arr) for _ in range(len(new_arr[0]))]
        for i in range(len(new_arr)):
            for j in range(len(new_arr[0])):
                temp[j][i] = new_arr[i][j]
        new_arr = temp

    new_arr = new_arr[:100][:100]

    if len(new_arr)>=100:
        print('no')

    # print(new_arr)
    return new_arr

if __name__=="__main__":

    sys.stdin = open("../input.txt", "r")

    r, c, k = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

    min_t = -1
    for t in range(101):
        # print(arr)
        if r-1 >= len(arr) or c-1>=len(arr[0]):
            # print("in")
            arr = sort_arr(arr)
            continue
        elif arr[r-1][c-1] == k:
            min_t = t
            break
        else:
            arr = sort_arr(arr)


    print(min_t)