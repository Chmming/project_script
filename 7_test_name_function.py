import unittest
from nm_fun import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试nm_fun.py"""
    def test_first_last_name(self):
        """能够正确地处理像janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('Janis','joplin')
        self.assertEqual(formatted_name,'Sanis joplin')
unittest.main()