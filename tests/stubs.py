__author__ = 'Mihail Mihaylov'


class MyProcessStub(object):
    _is_started = False

    def start_process(self):
        self._is_started = True
        return {0: 0}

    def stop_process(self):
        self._is_started = False

    def is_process_started(self):
        return self._is_started


class CarStub(object):

    def get_make(self):
        return 'Mock car'

    @property
    def wheels(self):
        return 666
