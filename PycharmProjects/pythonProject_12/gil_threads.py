#import pytest
import threading
import time
import datetime

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
    parser.add_argument("-j", "--jobnumber", dest="jnumber",
                        help="HPC sbatch number",
                        default="-1")

    args = parser.parse_args()
    print("job started with number " + args.jnumber)

    th1 = threading.Thread(target=cpu_threading)
    th2 = threading.Thread(target=io_threading)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    now = datetime.datetime.now()
    print()
    print("#########################################")
    print(now)
    print("Both tasks are done")
    print("#########################################")