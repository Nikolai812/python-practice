#import pytest
from my_file_reader import MyFileReader
import argparse


# Fixture without yield
def list_fiddling(l):
    l2 = l
    l3 = list(l)
    l2.pop()

    print('l=' + str(l))
    print('l2=' + str(l2))
    print('l3=' + str(l3))

    sl3 = sorted(l3)
    print('sl3=' + str(sl3))

    m = l3.sort()
    print('after sort() l3=' + str(l3))
    print('m=' + str(m))

    print('type of l3:' + str(type(l3)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="mock_server_url",
                        help="Mock Server URL",
                        default="http://stats-qa-03:8888")
    parser.add_argument("-o", "--order_id", dest="order_id",
                        help="Order Id",
                        default="81b0314a-9e90-4657-bed6-b00aa3468007")

    #args = parser.parse_args()

    list1 = [3, 2, 6, 8, 5, 14]
    list2 = [1, -1, 4, 13]
    list3 = [77, 75, 70]

    print(list1)
    print(list2)

    zipped3 = zip(list1, list2, list3)
    zipped2 = zip(list1, list2)
    output_list = [value for pair in zipped2 for value in pair]
    output_list2 = [pair for pair in zipped3]

    
    lz3 = list(zipped3)
    l3 = len(lz3)

    lz2 = list(zipped2)
    print(lz2)

    r = range(3)
    lr = len(r)


    print(output_list)
    print(output_list2)
