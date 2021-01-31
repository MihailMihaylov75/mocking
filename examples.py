__author__ = 'Mihail Mihaylov'


import os

from start_some_process import MyProcess, DataException


def read_input():
    my_input = input()
    return my_input


def print_input(my_input):
    print(my_input)


def get_current_dir():
    return os.getcwd()


class DataCollector(object):

    def __init__(self):
        self.my_driver = None
        self.my_data = []

    def initialize(self):
        self.my_driver = MyProcess()

    def collect_data(self):
        if self.my_driver.is_process_started():
            self.my_driver.stop_process()
            self.my_driver.clear_data()
        try:
            self.my_data = self.my_driver.start_process()
        except DataException:
            self.my_driver.clear_data()
            self.my_data = self.my_driver.start_process()
        return self.my_data

    def stop_the_process(self):
        self.my_driver.stop_process()


a = DataCollector()
a.initialize()
the_data = a.collect_data()
the_data = a.collect_data()
