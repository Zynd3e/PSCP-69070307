'''RabbitFence'''


def main():
    '''Rabbitfence'''
    x, y, z = map(int, input().split())
    price = int(input())

    length = (2 * (x + y)) * z
    total = length * price

    print(length)
    print(total)

main()
