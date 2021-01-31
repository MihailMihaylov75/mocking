__author__ = 'Mihail Mihaylov'
from random import randint


class DataException(Exception):
    pass


class MyProcess(object):
    _is_started = False
    _my_data = {}

    def is_process_started(self):
        return self._is_started

    def start_process(self):
        if self._my_data:
            raise DataException('You already have the data!')
        self._is_started = True
        return self._collect_data()

    def _collect_data(self):
        collected_data = {i: i * 10 for i in range(randint(5, 20))}
        self._my_data.update(collected_data)
        return self._my_data

    def clear_data(self):
        self._my_data = {}

    def stop_process(self):
        if self._is_started:
            self._is_started = False
        else:
            print('The process is stopped. Nothing to do.')
