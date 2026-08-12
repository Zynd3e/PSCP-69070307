'''min'''


def main():
    '''min'''
    n = int(input())
    lowest = None

    for _ in range(n):
        N = int(input())
        if lowest is None or N < lowest:
            lowest = N

    print(lowest)

main()
