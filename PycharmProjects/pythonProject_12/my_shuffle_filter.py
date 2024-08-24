import argparse
import random


def list_shuffle(theList, number=1):
    for iteration in range(number):
        print("shuffle iteration " + str(iteration + 1))
        random.shuffle(theList)
        print(theList)


def are_anagrams(word1, word2):
    return sorted(word1.casefold()) == sorted(word2.casefold())


def omit_anagrams(string_list):
    result = []
    for item in string_list:
        if not any(are_anagrams(item, res_item) for res_item in result):
            result.append(item)
    return result


def get_random_integers(lower, upper):
    while True:
        yield random.randint(lower, upper)


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

    args = parser.parse_args()

    first_list = list(range(21))
    print(first_list)
    list_shuffle(first_list, 3)

    word1 = "melon"
    word2 = "Lemon"
    word3 = "limon"

    b1 = are_anagrams(word1, word2)
    b2 = are_anagrams(word1, word3)

    print(b1, b2)

    word5 = "strap"
    word6 = "Traps"

    initial_list = [word1, word2, word3, word5, word6]
    refined_list = omit_anagrams(initial_list)
    print(refined_list)

    lk = []
    for i in range(40):
        lk.append(next(get_random_integers(10, 30)))

    print(lk)
