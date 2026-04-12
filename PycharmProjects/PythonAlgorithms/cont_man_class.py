class MyContextManager:
    def __init__(self, exponent):
        self.exponent = exponent
    def __enter__(self):
        print('entering')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting')
        if(exc_type is not None):
            print('exception type:', exc_type)
            print('exception value', exc_val)
            print('exception traceback', exc_tb)
        return True

    def send_to_exp_power(self, value):
        print('sending value {} to power {}'.format(value, self.exponent))
        return value ** self.exponent

    def send_generator(self, value):
        print('sending value {} to generator {}'.format(value, self.exponent))
        yield value ** self.exponent

    def do_something(self,arg):
        print(f'doing something with {arg}')
        if type(arg) is not int:
            raise TypeError(f'arg must be an integer, but is {arg}')


if __name__ == '__main__':
    print("main started")
    with MyContextManager(3) as mct:
        mct.do_something(5)
        print("do_something done, now method:\n")
        res = mct.send_to_exp_power(2)
        print(res)
        res = mct.send_to_exp_power(3)
        print(res)
        res = mct.send_to_exp_power(4)
        print(res)
        print("generator:\n")
        res = next(mct.send_generator(2))
        print(res)
        res = next(mct.send_generator(3))
        print(res)
        res = next(mct.send_generator(4))
        print(res)

    #with MyContextManager() as mct2:
    #    mct2.do_something((3,4))

    print("main ended")