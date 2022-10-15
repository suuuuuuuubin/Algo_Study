import sys


def get_combi(i, avail, line_n, cur):

    if len(cur)==line_n:
        return [cur]

    else :
        return_val = []
        for k in range(i, len(avail)):
            add = True
            for line in cur+h_line_ls:
                if avail[k][0] == line[0] and abs(avail[k][1]-line[1])==1:
                    add = False
                    break
            if add:
                result = get_combi(k+1, avail, line_n, cur+[avail[k]])
                return_val.extend(result)

        return return_val

def get_combination (N, H, h_line_ls, line_n, avail):
    combi_ls = get_combi(0, avail, line_n, [])
    # print("combi", line_n)
    return combi_ls

def is_True(h_line_ls) :
    # print(h_line_ls, len(h_line_ls))
    h_line_dict = {k:[] for k in range(1, H+1)}
    for line in h_line_ls:
        h_line_dict[line[0]].append(line)

    for i in range(1, N+1):
        cur_i = i
        for j in range(1, H+1):
            for line in h_line_dict[j]:
                if (line[1]==cur_i and line[0]==j):
                    cur_i += 1
                elif (line[1]+1==cur_i and line[0]==j):
                    cur_i -= 1

        # print(cur_i, i)
        if cur_i != i:
            return False

    return True



if __name__ =="__main__":

    sys.stdin = open("../input.txt", "r")
    N, M, H = map(int, sys.stdin.readline().split())
    h_line_ls = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    # print(h_line_ls)
    # get_combination(N, H, h_line_ls, 2)

    avail = []
    for i in range(1, N):
        for j in range(1, H + 1):
            make = True
            for line in h_line_ls:
                if line[0] == j and line[1] == i:
                    make = False
                    break
            if make:
                avail.append([j, i])
    avail.sort()
    # print("avail", avail)


    Success = False
    line = -1
    for line_n in range(4):
        if line_n > len(avail):
            break
        combi_ls = get_combination(N, H, h_line_ls, line_n, avail)
        # print(len(combi_ls))
        for combi in combi_ls:
            s = is_True(h_line_ls+combi)
            if s :
                Success = True
                line = line_n
                break

        if Success:
            break

    print(line)