'''Dist'''
import math


def main():
    '''Dist'''
    x1, y1, z1 = map(int, input().split())
    x2, y2, z2 = map(int, input().split())
    nums = [x1, x2, y1, y2, z1, z2]

    if all(-200000 < i < 200000 for i in nums):
        ans = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))
        print(f"{ans:.2f}")

main()
