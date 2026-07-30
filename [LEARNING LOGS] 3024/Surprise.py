'''Vote'''


def main():
    '''Vote'''
    sumvote = float(input())
    high = float(input())

    leftvote = sumvote - high

    minvote = max(0, leftvote - high)

    if (high - minvote) > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
