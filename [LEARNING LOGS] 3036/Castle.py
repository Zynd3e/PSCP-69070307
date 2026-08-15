'''Castle'''
import math

def main():
    '''Castle'''
    N = int(input().strip())

    if N == 1:
        print(0)
        return

    r = math.ceil(math.sqrt(N))
    c = N - (r - 1) ** 2

    if c % 2 == 1:
        ans = 2 * (r - 1)
    else:
        ans = 2 * r - 3

    print(ans)

main()
