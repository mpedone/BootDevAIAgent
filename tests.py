# tests in the main folder

import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_simple(self):
        test_output = get_files_info("calculator", "pkg")
        expected = "- __pycache__: file_size=4096 bytes, is_dir=True\n- render.py: file_size=766 bytes, is_dir=False\n- calculator.py: file_size=1737 bytes, is_dir=False"
        print(test_output)
        print(expected)
        self.assertEqual(test_output, expected)
    
    def test_same_dir(self):
        test_output = get_files_info("calculator", ".")
        expected = "- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False\n- tests.py: file_size=1342 bytes, is_dir=False"
        print(test_output)
        print(expected)
        self.assertEqual(test_output, expected)


if __name__ == "__main__":
    unittest.main()