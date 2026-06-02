from contextlib import contextmanager

@contextmanager
def power_manager(exponent):
    print("Powering on with exponent {}".format(exponent))
    def get_power(i):
        return i ** exponent
    yield get_power
    print("Powering off with exponent {}".format(exponent))


if __name__ == '__main__':
    print("main started")

    with power_manager(3) as cube:
        print("Inside gen")
        res = cube(2)
        print(res)
        res= cube(3)
        print(res)
        res = cube(4)
        print(res)


    print("main ended")