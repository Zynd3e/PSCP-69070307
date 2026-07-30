'''Ink'''
import math


def main():
    '''Ink'''
    S, N = map(int, input().split())
    pi = 3.1416
    for _ in range(N):
        x, y = map(int, input().split())
        t = (pi * (x**2 + y**2)) / S
        print(math.ceil(t))

main()
