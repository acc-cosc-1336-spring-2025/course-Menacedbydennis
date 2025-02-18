import unittest
from tests.homework.d_repetition import test_repetition

suite = unittest.TestLoader().loadTestsFromModule(test_repetition)
unittest.TextTestRunner().run(suite)
