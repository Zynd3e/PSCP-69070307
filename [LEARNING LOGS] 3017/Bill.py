'''Bill'''


def main():
    '''Bill'''
    presum = float(input())

    charge = presum * (10/100)

    if charge < 50:
        prevat = presum + 50
    elif charge > 1000:
        prevat = presum + 1000
    else:
        prevat = presum + charge

    vat = prevat * (7/100)
    Sum = prevat + vat

    print(f"{Sum:.2f}")

main()
