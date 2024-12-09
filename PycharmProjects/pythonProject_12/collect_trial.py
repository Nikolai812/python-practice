#import pytest
#import  from collections
import collections

from my_file_reader import MyFileReader
import argparse

#1. list
#2. tuple
#3. set
#4. frozenSet
#5. dictionary
#6. defaultDictionary
#7. orderedDictionary
#8. string
#9. namedTuple
def fiddle_named_gtuple():
    Coord = collections.namedtuple("Coord", ["x", "y", "z"])
    cd = Coord(1, 2, 3)
    print(cd)




#10. deque
def fiddle_deque():
    deq = collections.deque([3, 4, 5])
    deq.append(6)
    deq.appendleft(1)
    deq.appendleft(0)
    deq.popleft()
    print(deq)




#11. Counter
def fiddle_counter():
    cnt = collections.Counter(['aa', "b", 'c', 'aa', 'd', "b"])
    print(cnt)




def fiddle_ord_dict():
    ordd = collections.OrderedDict()
    ordd['aa'] = 1
    ordd['bb'] = 2
    ordd['cc'] = 3
    ordd.pop("aa")
    ordd["aa"] = 4
    print(ordd)



def fiddle_default_dict():
    defdic = collections.defaultdict(float)
    defdic["k1"] = 1
    defdic["k2"] += 3
    print(defdic)
    print(defdic["k3"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="mock_server_url",
                        help="Mock Server URL",
                        default="http://stats-qa-03:8888")
    parser.add_argument("-o", "--order_id", dest="order_id",
                        help="Order Id",
                        default="81b0314a-9e90-4657-bed6-b00aa3468007")

    #args = parser.parse_args()

    fiddle_counter()
    fiddle_deque()
    fiddle_ord_dict()
    fiddle_default_dict()
    fiddle_named_tuple()



