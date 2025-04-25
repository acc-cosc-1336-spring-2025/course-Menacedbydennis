import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):
    def test_roll_returns_value_between_1_and_6(self):
        die = Die()
        for _ in range(3):  # Test 3 rolls
            die.roll()
            val = die.get_rolled_value()
            self.assertGreaterEqual(val, 1)
            self.assertLessEqual(val, 6)
