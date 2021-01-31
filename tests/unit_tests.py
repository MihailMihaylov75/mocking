import os
import unittest
from unittest import mock
from unittest.mock import MagicMock
import tempfile
import shutil

from examples import print_input, get_current_dir, read_input


class TestInput(unittest.TestCase):

    def test_input1(self):
        with mock.patch('builtins.input', return_value='test'):
            assert read_input() == 'test'

    @mock.patch('builtins.input', lambda *args: 'test')
    def test_input2(self):
        assert read_input() == 'test'

    @mock.patch('builtins.input', return_value='test')
    def test_input3(self, mock_input):
        assert read_input() == 'test'
        assert mock_input.call_count == 1
        assert mock_input.called
        # mock_input.return_value = 'something else'

    def test_input4(self):
        mock_input = MagicMock(return_value='test')
        with mock.patch('builtins.input', mock_input):
            assert read_input() == 'test'

    def test_input5(self):
        with mock.patch('builtins.input') as mock_input:
            mock_input.return_value = 'test'
            assert read_input() == 'test'


class TestPrint(unittest.TestCase):

    # Example with assert_called_with
    def test_print1(self):
        with mock.patch('builtins.print') as mock_print:
            print_input('Hello World!')
            mock_print.assert_called_with("Hello World!")

    # Example with assert_called_with and mock at test case level
    @mock.patch('builtins.print')
    def test_print2(self, mock_print):
        print_input('Hello World!')
        mock_print.assert_called_with("Hello World!")

    def test_print3(self):
        mock_print = MagicMock()
        with mock.patch('builtins.print', mock_print):
            print_input("Hello World!")
            # assert function is called
            mock_print.assert_called()
            # assert function is called only once
            mock_print.assert_called_once()
            # assert function is called with specific value
            mock_print.assert_called_with("Hello World!")


class TestDirectory(unittest.TestCase):

    def setUp(self) -> None:
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        if os.path.isdir(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_get_current_dir1(self):
        with mock.patch('os.getcwd', return_value=self.temp_dir):
            assert get_current_dir() == self.temp_dir

    def test_get_current_dir2(self):
        with mock.patch.object(os, 'getcwd', return_value=self.temp_dir):
            assert get_current_dir() == self.temp_dir

    def test_get_current_dir3(self):
        with mock.patch('os.getcwd') as mocked_path:
            mocked_path.return_value = self.temp_dir
            assert get_current_dir() == self.temp_dir

    @mock.patch('os.getcwd')
    def test_get_current_dir4(self, mock_getcwd):
        mock_getcwd.return_value = self.temp_dir
        assert get_current_dir() == self.temp_dir

    def test_get_current_dir5(self):
        mock_getcwd = MagicMock()
        mock_getcwd.return_value = self.temp_dir
        with mock.patch('os.getcwd', mock_getcwd):
            assert get_current_dir() == self.temp_dir


if __name__ == '__main__':
    unittest.main()
