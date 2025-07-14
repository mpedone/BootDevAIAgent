# tests in the main folder

import unittest, os
from functions.write_file_content import write_file
# from functions.get_file_content import get_file_content
# from functions.get_files_info import get_files_info


def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for current directory:")
    print(result)
    print("")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for current directory:")
    print(result)
    print("")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for current directory:")
    print(result)
    print("")

    """ result = get_file_content("calculator", "lorem.txt")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_file_content("calculator", "main.py")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print("Result for current directory:")
    print(result)
    print("") """

    """ 
    class TestGetFilesInfo(unittest.TestCase):
        def test_simple(self):
        test_output = get_files_info("calculator", "pkg")
        expected = "- __pycache__: file_size=4096 bytes, is_dir=True\n- render.py: file_size=766 bytes, is_dir=False\n- calculator.py: file_size=1737 bytes, is_dir=False"
        print(test_output)
        self.assertEqual(test_output, expected)
    
    def test_same_dir(self):
        test_output = get_files_info("calculator", ".")
        expected = "- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False\n- tests.py: file_size=1342 bytes, is_dir=False"
        print(test_output)
        self.assertEqual(test_output, expected)

    def test_not_in_dir(self):
        test_output = get_files_info("calculator", "/bin")
        expected = 'Error: Cannot list "/bin" as it is outside the permitted working directory'
        print(test_output)
        self.assertEqual(test_output, expected)

    def test_parent_not_in_dir(self):
        test_output = get_files_info("calculator", "../")
        expected = 'Error: Cannot list "../" as it is outside the permitted working directory'
        print(test_output)
        self.assertEqual(test_output, expected)
    
    def test_not_a_dir(self):
        test_output = get_files_info("calculator", "main.py")
        expected = 'Error: "main.py" is not a directory'
        self.assertEqual(test_output, expected)

    def test_subdir(self):
        test_output = get_files_info("calculator/pkg", "__pycache__")
        self.assertIn("calculator.cpython", test_output)
    
    def test_absolute_path(self):
        test_output = get_files_info("/home/mattpedone/workspace/GITHUB", "mpedone")
        self.assertIn("BootDevAIAgent", test_output)

    def test_absolute_path_self_ref(self):
        test_output = get_files_info("/home/mattpedone/workspace/GITHUB/mpedone", ".")
        self.assertIn("BootDevAIAgent", test_output)

    def test_no_target(self):
        test_output = get_files_info("calculator")
        expected = "- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False\n- tests.py: file_size=1342 bytes, is_dir=False"
        self.assertEqual(test_output, expected)
    
    def test_blank_target(self):
        test_output = get_files_info("calculator", "")
        expected = "- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False\n- tests.py: file_size=1342 bytes, is_dir=False"
        self.assertEqual(test_output, expected)
    
    def test_space_target(self):
        test_output = get_files_info("calculator", " ")
        expected = 'Error: Cannot list " " as it is outside the permitted working directory'
        self.assertEqual(test_output, expected)
    
    def test_blank_working_directory(self):
        test_output = get_files_info("anything", "calculator")
        expected = f'Error: No such file or directory: "anything"'
        self.assertEqual(test_output, expected)

    def test_working_directory_not_dir(self):
        test_output = get_files_info("main.py", "calculator")
        expected = f'Error: "main.py" is not a directory'
        self.assertEqual(test_output, expected) """
    
    """ def test_abs_path(self):
        test_output = get_files_info("/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent", "/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent/calculator")
        expected = "- pkg: file_size=4096 bytes, is_dir=True\n- main.py: file_size=575 bytes, is_dir=False\n- tests.py: file_size=1342 bytes, is_dir=False"
        self.assertEqual(test_output, expected)

get_files_info("/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent", "/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent/calculator")

get_files_info("/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent", "/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent/.")

get_files_info("/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent/calculator", "/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent")

get_files_info("/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent", "/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent/..")

get_files_info("/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent", "/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent/main.py")

get_files_info("/home/mattpedone/workspace/GITHUB/mpedone/BootDevAIAgent", "/home/mattpedone/workspace/GITHUB/mpedone/StaticSite/Public") """


if __name__ == "__main__":
    test()