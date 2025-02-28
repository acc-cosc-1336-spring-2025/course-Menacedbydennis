import unittest

from src.homework.e_functions.value_return import get_hour
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds

class Test_Config(unittest.TestCase):
    def test_get_hour(self):
        self.assertEqual(get_hour(3800), 1) # 3800 seconds = 1 hour and 0 minutes 
        self.assertEqual(get_hour(3600), 1) # 3600 seconds = exactly 1 hour

    def test_get_minutes(self):
        self.assertEqual(get_minutes(3800), 3) # 3800 seconds = 1 hour and 0 minutes  20 seconds
        self.assertEqual(get_minutes(3600), 0) # 3600 seconds = exactly 1 hour 

    def test_get_seconds(self):
        self.assertEqual(get_seconds(3800), 20) # 3800 seconds = 1 hour , 0 minutes, and 20 seconds 
        self.assertEqual(get_seconds(3600), 0) # 3600 seconds = exactly 1 hour 

if __name__ == '__main__':
    unittest.main()
