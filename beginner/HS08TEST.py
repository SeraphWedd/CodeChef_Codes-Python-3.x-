
def compute(w, c):
    if w%5 == 0:
        if w < c - 0.5:
            print("{0:.2f}".format(c - w - 0.5))
        else:
            print("{0:.2f}".format(c))
    else:
        print("{0:.2f}".format(c))

withraw, cash = [float(x) for x in input().strip(' ').split(' ')]

if (withraw > 0 and withraw <= 2000) and (cash >= 0 and cash <= 2000):
    compute(withraw, cash)
