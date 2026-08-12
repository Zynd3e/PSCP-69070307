'''passgen'''


def main():
    '''passgen'''
    Name = str(input())
    Surname = str(input())
    Age = str(input())

    if len(Name) >= 5 and len(Surname) >= 5:
        print(f"{Name[:2]}{Surname[-1]}{Age[-1]}")
    else:
        print(f"{Name[:1]}{Age}{Surname[-1]}")


main()
