# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''
def print_map(board):
    for line in board:
        print(line)
# import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# sys.stdin = open("../input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # M , A = map(int, sys.stdin.readline().split(" ")) # M : 총 이동 시간 / A : BC의 개수
    # A_move = list(map(int, sys.stdin.readline().strip().split(" ")))+[0]
    # B_move = list(map(int, sys.stdin.readline().strip().split(" ")))+[0]
    # AP_ls = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(A)]
    # AP : x, y 좌표, C-충전범위, P-처리량

    M, A = map(int, input().split(" "))  # M : 총 이동 시간 / A : BC의 개수
    A_move = list(map(int, input().strip().split(" "))) + [0]
    B_move = list(map(int, input().strip().split(" "))) + [0]
    AP_ls = [list(map(int, input().strip().split(" "))) for _ in range(A)]

    BC_MAP = [[-1]*11 for _ in range(11)]

    for A_idx, AP in enumerate(AP_ls):
        cnt=0
        x, y, c, p = AP
        for i in range(-c, c+1):
            for j in range(-c+abs(i), c-abs(i)+1):
                if x+i>0 and x+i<=10 and y+j>0 and y+j<=10:
                    if BC_MAP[x+i][y+j]==-1:
                        BC_MAP[x+i][y+j] = [(A_idx, p)]
                    else:
                        BC_MAP[x+i][y+j].append((A_idx, p))
    # print_map(BC_MAP)
    A_cur = [1,1]
    B_cur = [10,10]
    # 0 : 이동하지 않음, 1: 위로 이동, 2: 우로 이동, 3: 아래로 이동, 4: 좌로 이동
    Move = [[0,0], [0,-1], [1,0], [0,1], [-1,0]]

    AB_total = 0
    for t in range(M+1):
        # print(t)
        # A
        A_avail = []
        if BC_MAP[A_cur[0]][A_cur[1]] != -1:
            A_avail = BC_MAP[A_cur[0]][A_cur[1]]
        A_avail.sort(key=lambda x: x[1], reverse=True)

        # B
        B_avail = []
        if BC_MAP[B_cur[0]][B_cur[1]] != -1:
            B_avail = BC_MAP[B_cur[0]][B_cur[1]]
        B_avail.sort(key=lambda x: x[1], reverse=True)

        # Get Largest Charge
        if A_avail and B_avail:
            if A_avail[0] == B_avail[0]:
                if len(A_avail)>1 and len(B_avail)>1:
                    AB_total += max(A_avail[0][1] + B_avail[1][1], A_avail[1][1] + B_avail[0][1])
                elif len(A_avail)>1:
                    AB_total += A_avail[1][1] + B_avail[0][1]
                elif len(B_avail)>1:
                    AB_total += A_avail[0][1] + B_avail[1][1]
                else :
                    AB_total += A_avail[0][1]
            else:
                AB_total += A_avail[0][1]
                AB_total += B_avail[0][1]
        elif A_avail :
            AB_total += A_avail[0][1]
        elif B_avail :
            AB_total += B_avail[0][1]

        # Move
        A_cur = [A_cur[0]+Move[A_move[t]][0], A_cur[1]+Move[A_move[t]][1]]
        B_cur = [B_cur[0]+Move[B_move[t]][0], B_cur[1]+Move[B_move[t]][1]]

    print(f"#{test_case} {AB_total}")
    # ///////////////////////////////////////////////////////////////////////////////////
