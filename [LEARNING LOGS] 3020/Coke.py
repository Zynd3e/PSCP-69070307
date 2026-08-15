'''Coke'''


def main():
    '''Coke'''
    normprice = int(input())
    cappro = int(input())
    proprice = int(input())
    want = int(input())

    if not want :
        print(0)
    elif cappro > 0:
        cokeset = want // cappro
        left = want % cappro
        if not left:
            cokeset -= 1

        normpricecount = want - cokeset
        sum1 = (normprice * normpricecount) + (proprice * cokeset)
        print(sum1)
    else:
        sum1 = normprice * want
        print(sum1)


main()
