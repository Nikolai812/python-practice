#import pytest
import threading
import time

from my_file_reader import MyFileReader
import argparse


class A:
    def show(self):
        print("This is A")


class B(A):
    def show(self):
        print("This is B")


class C(A):
    def show(self):
        print("This is C")


class D(B, C):
    def show2(self):
        print("This is D")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="mock_server_url",
                        help="Mock Server URL",
                        default="http://stats-qa-03:8888")
    parser.add_argument("-o", "--order_id", dest="order_id",
                        help="Order Id",
                        default="81b0314a-9e90-4657-bed6-b00aa3468007")

    #args = parser.parse_args()

    d = D()
    d.show()

    print(D.mro())


