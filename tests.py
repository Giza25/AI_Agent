import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_default(self):
        print("\nResult for current directory:")
        result = get_files_info("calculator")
        print(result)
        self.assertTrue('pkg' in result and 'main.py' in result and 'tests.py' in result)

    def test_pkg(self):
        print("\nResult for 'pkg' directory:")
        result = get_files_info("calculator", "pkg")
        print(result)
        self.assertTrue('calculator.py' in result and 'render.py' in result)

    def test_bin(self):
        print("\nResult for '/bin' directory:")
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertTrue('Error:' in result)

    def test_traverse(self):
        print("\nResult for '../' directory:")
        result = get_files_info("calculator", "../")
        print(result)
        self.assertTrue('Error:' in result)

    def test_file(self):
        print("\nResult for 'calculator' directory:")
        result = get_files_info("calculator", "calculator")
        print(result)
        self.assertTrue('Error:' in result)

if __name__ == "__main__":
    unittest.main()