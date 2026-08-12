'''Calc'''


def main():
    '''Calc'''
    n = int(input())

    if n == 1:
        print(1)
        return

    digit_count = 0
    for i in range(1, n + 1):
        digit_count += len(str(i))

    total = digit_count + n
    print(total)


main()
