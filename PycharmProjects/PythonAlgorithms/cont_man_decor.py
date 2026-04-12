from contextlib import contextmanager

@contextmanager
def power_gen(exponent):
    print("Powering on with exponent {}".format(exponent))
    def get_power(i):
        return i ** exponent
    yield get_power
    print("Powering off with exponent {}".format(exponent))


if __name__ == '__main__':
    print("main started")

    with power_gen(3) as gen:
        print("Inside gen")
        res = gen(2)
        print(res)
        res= gen(3)
        print(res)
        res = gen(4)
        print(res)


    print("main ended")