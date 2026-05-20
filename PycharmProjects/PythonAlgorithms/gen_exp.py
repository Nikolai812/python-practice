from itertools import count

gen_finite = (x*x for x in range(10))
gen_infinite = (x*x for x in count())

def finite_power(n, limit):
    return (x**n for x in range(limit))

def infinite_power(n):
    return (x**n for x in count())


if __name__ == "__main__":
    # for x in gen_finite:
    #     print(x)
    #
    #
    # for x in range(8):
    #     print(next(gen_infinite))
    for y in finite_power(3,5):
        print(y)

    a3 = infinite_power(3)
    for y in range(6):
        print(next(a3))