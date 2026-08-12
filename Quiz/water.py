'''water'''


def main():
    '''water'''
    temp = int(input())
    unit = input().lower()

    if (0 < temp < 100 and unit == "c") or (32 < temp < 212 and unit == "f"):
        print("liquid")
    elif(temp <= 0 and unit == "c") or (temp <= 32 and unit == "f"):
        print("solid")
    else:
        print("gas")

main()
