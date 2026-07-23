'''Colors'''


def main():
    '''Colors'''
    First = str(input()).upper()
    Second = str(input()).upper()
    Sorting = sorted([First,Second])
    Sum = ''

    match Sorting:
        case ["RED","YELLOW"]:
            Sum = "Orange"
        case ["BLUE","RED"]:
            Sum = "Violet"
        case ["BLUE","YELLOW"]:
            Sum = "Green"
        case ["BLUE","BLUE"]:
            Sum = "Blue"
        case ["YELLOW","YELLOW"]:
            Sum = "Yellow"
        case ["RED","RED"]:
            Sum = "Red"
        case _:
            Sum = "Error"

    print(Sum)

main()
