'''rabmarket'''


def main():
    '''rabmarket'''
    Carrot, Cabbage, Tomato = map(int, input().split())
    Carrot_price = 10
    Cabbage_price = 25
    Tomato_price = 3

    print(f"{(Carrot * Carrot_price) + (Cabbage * Cabbage_price) + (Tomato * Tomato_price)}")

main()
