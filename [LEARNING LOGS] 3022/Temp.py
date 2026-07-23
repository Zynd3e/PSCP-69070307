'''temp'''


def main():
    '''temp'''
    n = float(input())
    before = input().upper()
    after = input().upper()

    match before:
        case "C":
            k = n + 273.15
        case "F":
            k = (n - 32) * (5 / 9) + 273.15
        case "K":
            k = n
        case "R":
            k = n * (5 / 9)

    match after:
        case "C":
            k = k - 273.15
        case "F":
            k = ((9 / 5) * k) - 459.67
        case "K":
            pass
        case "R":
            k = k * (9 / 5)

    print(f"{k:.2f}")


main()
