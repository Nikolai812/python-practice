import csv
from abc import abstractmethod, ABC
class MyFileReader:

    def read_csv(self, csv_name):
        with open(csv_name, 'r', newline='') as csv_file:
            # Creating csv reader object
            csvreader = csv.reader(csv_file)

            #iterate over object
            for row in csvreader:
                print(row)
