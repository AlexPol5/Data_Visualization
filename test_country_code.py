import unittest
from country_code import get_country_code


class CodeTestCase(unittest.TestCase):
    """Тест для 'country_code.py'."""

    def test_country_code(self):
        """
        Возвращает ли для заданной страны её код Pygal,
        состоящий из 2 букв?
        """
        country_code = get_country_code('Russian Federation')
        self.assertEqual(country_code, 'ru')


unittest.main()
