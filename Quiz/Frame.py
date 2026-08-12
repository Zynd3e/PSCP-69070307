'''Frame'''


def main():
    '''Frame'''
    string = str(input())
    length = len(string)
    boarder = length + 2

    print(boarder * "*")
    print(f"*{string}*")
    print(boarder * "*")

main()
