# 백준 1713 후보 추천하기
# https://www.acmicpc.net/problem/1713

import sys

if __name__=="__main__":
    sys.stdin = open('../input.txt','r')

    N = int(sys.stdin.readline()) # N : 사진 틀의 개수
    M = int(sys.stdin.readline()) # M : 총 추천 횟수
    recoms = list(map(int, sys.stdin.readline().split())) # recom : 추천 목록

    pic_ls =  []

    for t, recom in enumerate(recoms):
        flag = False
        # 이미 추천 받은 학생을 또 추천한 경우 추천 받은 횟수만 증가
        for p_idx, pic in enumerate(pic_ls):
            if pic[0] == recom :
                pic[1] += 1
                pic_ls[p_idx] = pic
                flag = True
        if (flag):
            continue

        # 추천 받지 않았고 빈 사진틀도 있을 경우
        if len(pic_ls) < N:
            # 추천받은 학생의 번호, 추천받은 횟수, 추천받아 게시된 시간
            pic_ls.append([recom, 1, t])
            flag = True
        if (flag):
            continue


        # 빈 사진틀이 없을 경우
        # 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고 게시
        # 추천 받은 횟수가 가장 적은 학생이 많을 경우 가장 오래된 사진 삭제
        pic_ls.sort(key=lambda x:x[2], reverse=False)
        pic_ls.sort(key=lambda x:x[1], reverse=False)
        del pic_ls[0]
        pic_ls.append([recom, 1, t])


    final_cand = list(str(pic[0]) for pic in sorted(pic_ls))
    print(' '.join(final_cand))
