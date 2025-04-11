import unittest
from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
    unittest.TextTestRunner(verbosity=2).run(suite)
