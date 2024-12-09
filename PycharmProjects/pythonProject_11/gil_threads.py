#import pytest
import threading
import time

from my_file_reader import MyFileReader
import argparse


# Fixture without yield
def cpu_threading():
    count = 0
    print("cpu_threading started, count: ", count)
    for i in range(10**8):
        count += 1

    print("cpu_threading ended, count: ", count)


def io_threading():
    print("io_threading started")
    time.sleep(2)
    print("io_threading task ended")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="mock_server_url",
                        help="Mock Server URL",
                        default="http://stats-qa-03:8888")
    parser.add_argument("-o", "--order_id", dest="order_id",
                        help="Order Id",
                        default="81b0314a-9e90-4657-bed6-b00aa3468007")

    #args = parser.parse_args()

    th1 = threading.Thread(target=cpu_threading)
    th2 = threading.Thread(target=io_threading)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print("Both tasks are done")