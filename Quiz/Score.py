'''Score'''


def main():
    '''Score'''
    num = int(input())
    highest = 0
    highestcount = 0
    for _ in range(num):
        Score = int(input())
        if Score > highest:
            highest = Score
            highestcount = 1
        elif Score == highest:
            highestcount +=1

    print(highest)
    print(highestcount)

main()
