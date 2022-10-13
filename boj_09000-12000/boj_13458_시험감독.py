if __name__ == "__main__":

    N = map(int, input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    count = 0
    for a in A:
        a -= B
        if a<=0:
            count += 1
        else:
            c = a//C if a%C ==0 else a//C+1
            count += 1+c

        # print(count)

    print(count)