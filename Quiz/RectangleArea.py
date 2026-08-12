'''Area'''


def main():
    '''Area'''
    x1, y1, w1, h1 = map(int, input().split())
    x2, y2, w2, h2 = map(int, input().split())

    Left = max(x1,x2)
    Right = min(x1 + w1,x2 + w2)
    woverlap = Right - Left
    Bottom = max(y1,y2)
    Top = min(y1 + h1,y2 + h2)
    hoverlap = Top - Bottom

    Area = woverlap * hoverlap

    if woverlap <= 0 or hoverlap <= 0:
        print("no overlapping")
    else:
        print(Area)

main()
