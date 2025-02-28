import pandas as pd

# def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def test():
    # x = input('enter in a setence: ')
    x = 'hello there my name is'

    df = pd.read_csv('test.csv')

    y = list(x.split(" "))

    p1, p2 = 0, len(y)-1

    new = []

    while p1 < p2:
        # the .values check in the whole csv file(s)
        if y[p1] in df.values:
            p1 += 1

        else:
            # return 'f', prRed(f'{y[p1]}')
            # return f'{y[p1]}'
            new.append(y[p1])

    return f'{new}'


# invoke
h = test()
print(h)


# have it input the words use .split() and
# see if any of those words are in the dictionary if not return that word
