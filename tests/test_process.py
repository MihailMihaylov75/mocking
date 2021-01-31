import os
import unittest
from unittest import mock
from unittest.mock import Mock

from examples import DataCollector
from start_some_process import MyProcess
from tests.test_doubles import TestPairs
from stubs import MyProcessStub


class TestDataCollector(unittest.TestCase):

    def setUp(self) -> None:
        self.data_collector = DataCollector()
        self.data_collector.initialize()

    def tearDown(self) -> None:
        del self.data_collector

    def test_initialize(self):
        isinstance(self.data_collector, MyProcess)

    @mock.patch('start_some_process.MyProcess.start_process', return_value={0: 0})
    def test_collect_data(self, _):
        assert self.data_collector.collect_data() == {0: 0}

    def test_collect_data2(self):
        with mock.patch.object(MyProcess, 'start_process', return_value={0: 0}):
            assert self.data_collector.collect_data() == {0: 0}

    @mock.patch('start_some_process.MyProcess.start_process', return_value={0: 0})
    @mock.patch('start_some_process.MyProcess.clear_data', return_value={})
    def test_collect_data_not_clear(self, _, mock_clear):
        self.data_collector.collect_data()
        mock_clear.assert_called()

    @mock.patch('start_some_process.MyProcess.start_process', return_value={0: 0})
    @mock.patch('start_some_process.MyProcess.stop_process')
    def test_stop_process_called(self, _, mock_stop_process):
        self.data_collector.collect_data()
        mock_stop_process.assert_called()
        mock_stop_process.assert_called_once()

    @mock.patch('start_some_process.MyProcess.start_process', return_value={0: 0})
    @mock.patch('start_some_process.MyProcess.stop_process')
    def test_stop_process_called(self, _, mock_stop_process):
        mock_stop_process.assert_not_called()

    def test_process_started(self):
        self.data_collector.collect_data()
        assert self.data_collector.my_driver.is_process_started()

    def test_process_stopped(self):
        self.data_collector.collect_data()
        self.data_collector.stop_the_process()
        assert not self.data_collector.my_driver.is_process_started()


class TestDataCollectorWithStubs(unittest.TestCase):

    def test_mock_getcwd(self):
        mock_getcwd = Mock(return_value='whatever_i_want')
        with TestPairs(module=os, getcwd=mock_getcwd):
            assert os.getcwd() == 'whatever_i_want'

    def test_process_started(self):
        with TestPairs(MyProcess=MyProcessStub):
            self.data_collector = DataCollector()
            self.data_collector.initialize()
            self.data_collector.collect_data()
            assert self.data_collector.my_driver.is_process_started()


class TestDataCollectorWithStubs2(unittest.TestCase):

    def setUp(self) -> None:
        with TestPairs(MyProcess=MyProcessStub):
            self.data_collector = DataCollector()
            self.data_collector.initialize()

    def tearDown(self) -> None:
        del self.data_collector

    def test_process_started(self):
        self.data_collector.collect_data()
        assert self.data_collector.my_driver.is_process_started()


if __name__ == '__main__':
    unittest.main()
