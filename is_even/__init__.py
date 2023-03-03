__version__ = "1.0.4"

def isEven(n, optimized = True):
    res = [True, False]
    while True:
        try:
            return res[n]
        except IndexError:
            if optimized:
                res += res
            else:
                res += [True, False]
