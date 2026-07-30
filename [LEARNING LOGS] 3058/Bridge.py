'''Bridge'''


def main():
    '''Bridge'''
    Small = int(input())
    Big = int(input())
    length = int(input())

    bigneed = length // 5
    used = min(bigneed, Big)
    lengthleft = length - (used * 5)

    if Small > lengthleft:
        print(lengthleft)
    else:
        print(-1)

main()
