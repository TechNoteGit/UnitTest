import unittest
import file_operation
import pickle
from datetime import datetime
from unittest.mock import Mock
from unittest.mock import patch, mock_open


class TestFileOperation(unittest.TestCase):
    def test_file_read(self):
        current_time = datetime.now()
        read_data = pickle.dumps(current_time)
        mock = mock_open(read_data=read_data)
        with patch('builtins.open', mock):
            ret = file_operation.file_read('test_file')

        self.assertEqual(current_time, ret)

    def test_file_write(self):
        mock = mock_open()
        with patch('builtins.open', mock):
            file_operation.file_write('test_file')

        mock.assert_called_once_with('test_file', 'wb')


if __name__ == '__main__':
    unittest.main()
