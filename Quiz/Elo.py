'''Elo'''

def main():
    '''Elo'''
    RA = int(input())
    RB = int(input())
    select_player = str(input()).upper()
    chances = ''


    EA = 1/(1+10**((RB - RA)/400))
    EB = 1/(1+10**((RA - RB)/400))

    if select_player == "A":
        chances = EA
    elif select_player == "B":
        chances = EB
    print(f"{chances:.2f}")

main()
