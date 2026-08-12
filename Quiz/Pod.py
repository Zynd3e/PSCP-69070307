'''Pod'''


def main():
    '''Pod'''
    N, K = map(int, input().split())
    count = [0] * K

    for _ in range(N):
        row = int(input())
        count[row - 1] += 1

    trip = min(count)

    remain = N - (trip * K)
    print(remain)


main()
