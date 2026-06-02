from itertools import count, islice

gen_finite = (x*x for x in range(10))
gen_infinite = (x*x for x in count())

def finite_power_expression(n, limit):
    return (x**n for x in range(limit))

def infinite_power_expression(n):
    return (x**n for x in count())

def power_gen(n):
    for i in count(1):
        yield i**5


if __name__ == "__main__":
    z=5

    stream = power_gen(5)
    filtered = filter(lambda x: x % 2 != 0, stream)
    slised = islice(filtered, 10)
    for x in slised:
        print("===")
        print(x)

    # for x in gen_finite:
    #     print(x)
    #
    #
    # for x in range(8):
    #     print(next(gen_infinite))


    # for y in finite_power_expression(3, 5):
    #     print(y)
    #
    # a3 = infinite_power_expression(3)
    # for y in range(6):
    #     print(next(a3))