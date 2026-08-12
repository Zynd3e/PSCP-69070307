'''Milk'''


def main():
    '''Milk'''
    bottleprice = int(input())
    cappro = int(input())
    probottle = int(input())
    money = int(input())

    totalbot = money // bottleprice
    cap = totalbot
    count = 0

    if not cappro:
        print(totalbot)
        return

    while cap >= cappro:
        count += 1
        cap -= cappro
        cap += probottle

    print((count * probottle) + totalbot)

main()
