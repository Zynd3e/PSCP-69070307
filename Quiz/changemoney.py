"""changemoney"""


def main():
    """changemoney"""
    money = int(input())

    c10 = money // 10
    money %= 10

    c5 = money // 5
    money %= 5

    c2 = money // 2
    money %= 2

    c1 = money

    print(f"10 = {c10}")
    print(f"5 = {c5}")
    print(f"2 = {c2}")
    print(f"1 = {c1}")


main()
