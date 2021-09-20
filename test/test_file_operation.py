import unittest
import file_operation


class TestFileOperation(unittest.TestCase):
    def test_file_read(self):
        ret = file_operation.file_read()
        self.assertEqual(0, ret)

    def test_file_write(self):
        ret = file_operation.file_write()
        self.assertEqual(0, ret)


if __name__ == '__main__':
    unittest.main()
