'''Saitama'''


def main():
    '''Saitama'''
    reqpushup = int(input())
    reqsitup = int(input())
    reqsquat = int(input())
    reqrun = int(input())
    pushperday = int(input())
    sitperday = int(input())
    runperday = int(input())
    squatperday = int(input())

    count1 = 0
    while reqpushup > 0:
        count1 += 1
        reqpushup -= pushperday
    count2 = 0
    while reqsitup > 0:
        count2 += 1
        reqsitup -= sitperday
    count3 = 0
    while reqsquat > 0:
        count3 += 1
        reqsquat -= squatperday
    count4 = 0
    while reqrun > 0:
        count4 += 1
        reqrun -= runperday

    print(max(count1,count2,count3,count4))


main()
