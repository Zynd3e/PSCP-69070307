'''Wrapping'''


def main():
    '''Wrapping'''
    r, h, l = map(float, input().split())
    pi = 3.14

    width = (2 * pi * r) + l
    length = h + (2 * r)

    print(f"{length:.2f} {width:.2f}")


main()
