'''Promotion'''


def main():
    '''Promotion'''
    Proppl = int(input())
    PromoCount = int(input())
    Price = int(input())
    PplCount = int(input())

    PplSet = PplCount // Proppl
    PplLeft = PplCount % Proppl

    Sum = ((PplSet * PromoCount)*Price) + (PplLeft * Price)

    print(Sum)

main()
