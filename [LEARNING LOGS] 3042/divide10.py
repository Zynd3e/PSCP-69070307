'''divide10'''


def main():
    '''divide10'''
    num = int(input())

    count = num // 10

    while count >=0:
        print(10 * count,end=" ")
        count -=1
        
main()
