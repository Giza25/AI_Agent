import unittest
from functions.get_files_info import get_files_info
from functions.get_files_content import get_files_content
from functions.write_file import write_file

"""
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


class TestGetFilesContent(unittest.TestCase):
    def test_main(self):
        print(f'\nResult for "main.py" file:')
        result = get_files_content("calculator", "main.py")
        print(result)
        self.assertTrue(f'def main():' in result)

    def test_file_in_directory(self):
        print(f'\nResult for "pkg/calculator.py" file:')
        result = get_files_content("calculator", "pkg/calculator.py")
        print(result)
        self.assertTrue(f'class Calculator:' in result)

    def test_directory(self):
        print(f'\nResult for "/pkg" directory:')
        result = get_files_content("calculator", "pkg")
        print(result)
        self.assertTrue(f'Error: ' in result)

    def test_not_exists(self):
        print(f'\nResult for "pkg/file_does_not_exist.py" file:')
        result = get_files_content("calculator", "pkg/file_does_not_exist.py")
        print(result)
        self.assertTrue(f'Error: ' in result)
"""

class TestWriteToFile(unittest.TestCase):
    def test_lorem(self):
        print(f'\nResult for "lorem.txt" file:')
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
        self.assertTrue(f'28 characters written' in result)

    def test_lorem_in_dir(self):
        print(f'\nResult for "pkg/morelorem.txt" file:')
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
        self.assertTrue(f'26 characters written' in result)
    
    def test_invalid(self):
        print(f'\nResult for "/tmp/temp.txt" file:')
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        self.assertTrue(f'Error:' in result)

if __name__ == "__main__":
    unittest.main()